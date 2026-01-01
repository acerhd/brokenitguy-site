import os
import json
import datetime
import subprocess
from google import genai

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_FILE = os.path.join(BASE_DIR, "logs.json")
INPUT_FILE = os.path.join(BASE_DIR, "what i am doing.txt")
MARKER_FILE = os.path.join(BASE_DIR, ".log_marker")

# --- LOAD SECRETS ---
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")

try:
    with open(SECRETS_FILE, "r") as f:
        secrets = json.load(f)
        API_KEY = secrets["GEMINI_API_KEY"]
except FileNotFoundError:
    print("CRITICAL ERROR: secrets.json not found!")
    exit()

client = genai.Client(api_key=API_KEY)

def update_logs():
    # 1. READ ONLY NEW CONTENT
    last_pos = 0
    if os.path.exists(MARKER_FILE):
        try:
            with open(MARKER_FILE, "r") as f:
                last_pos = int(f.read().strip())
        except:
            last_pos = 0

    try:
        with open(INPUT_FILE, "r") as f:
            # Jump to where we left off last time
            f.seek(last_pos)
            new_content = f.read()
            # Save the new position for next time
            current_pos = f.tell()
    except FileNotFoundError:
        return # File doesn't exist yet, do nothing

    # If there is nothing new, stop silently
    if not new_content.strip():
        return

    # 2. READ EXISTING LOGS
    try:
        with open(LOGS_FILE, "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 3. AI INSTRUCTIONS
    prompt = f"""
    You are the AI system for 'BrokenITGuy'.
    
    TASK: 
    Convert the following raw notes into a JSON array of log entries. 
    If the notes contain multiple distinct lines, create a separate JSON object for each.
    
    INPUT NOTES:
    {new_content}
    
    CURRENT TIME: {current_time}
    
    REQUIRED JSON FORMAT:
    [
        {{
            "date": "{current_time}",
            "status": "SUCCESS", 
            "title": "A SHORT CREATIVE TERMINAL TITLE",
            "content": "The log text formatted with HTML. Use <span class='command-text'> for tech terms. Use <p> for spacing.",
            "tags": ["#tag1", "#tag2"]
        }}
    ]
    
    RULES:
    1. Return ONLY the raw JSON array. No markdown code blocks.
    2. Maintain the 'BrokenITGuy' persona.
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=prompt
        )
        
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        new_entries = json.loads(clean_json)
        
        updated_data = new_entries + existing_data
        
        with open(LOGS_FILE, "w") as f:
            json.dump(updated_data, f, indent=4)
            
        # UPDATE THE MARKER only if successful
        with open(MARKER_FILE, "w") as f:
            f.write(str(current_pos))
         # --- NEW: AUTO-PUSH TO GITHUB ---
        print(">> New log added. Pushing to GitHub...")
        try:
            subprocess.run(["git", "add", "logs.json"], check=True)
            subprocess.run(["git", "commit", "-m", "Auto-update logs"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(">> SUCCESS: Website updated!")
        except subprocess.CalledProcessError as e:
            print(f"!! Git Error: {e}")   

    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Raw Response: {response.text}")

if __name__ == "__main__":
    update_logs()
    