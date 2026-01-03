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
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")
FEED_FILE = os.path.join(BASE_DIR, "feed.xml")

# --- LOAD SECRETS ---
try:
    with open(SECRETS_FILE, "r") as f:
        secrets = json.load(f)
        API_KEY = secrets["GEMINI_API_KEY"]
except FileNotFoundError:
    print("CRITICAL ERROR: secrets.json not found!")
    exit()

# Initialize Client
client = genai.Client(api_key=API_KEY)

# --- HELPER FUNCTION: GENERATE RSS FEED ---
def generate_rss(all_logs):
    """Generates an RSS feed from the logs.json data."""
    rss_content = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>BrokenITGuy Updates</title>
 <description>Live log entries from the headless pipeline.</description>
 <link>https://brokenitguy.com</link>
 <language>en-us</language>
"""
    # Loop through logs and add them as items
    # We take the last 10 entries to keep the feed clean
    for entry in all_logs[:10]:
        rss_content += f""" <item>
  <title>Update: {entry.get('timestamp', 'No Date')}</title>
  <description>{entry.get('content', 'No Content')}</description>
  <link>https://brokenitguy.com</link>
  <guid>{entry.get('timestamp', '')}</guid>
 </item>
"""
    rss_content += "</channel>\n</rss>"
    
    # Write the file to disk
    with open(FEED_FILE, "w") as f:
        f.write(rss_content)
    print("✅ feed.xml generated successfully.")

# --- MAIN UPDATE SCRIPT ---
def update_logs():
    # 1. CHECK FOR NEW CONTENT
    last_pos = 0
    if os.path.exists(MARKER_FILE):
        try:
            with open(MARKER_FILE, "r") as f:
                last_pos = int(f.read().strip())
        except:
            last_pos = 0

    new_content = ""
    current_pos = 0
    
    try:
        with open(INPUT_FILE, "r") as f:
            f.seek(last_pos)
            new_content = f.read()
            current_pos = f.tell()
    except FileNotFoundError:
        print("Waiting for input file...")
        return

    # If nothing new, stop silently
    if not new_content.strip():
        return

    print(f"🔹 New content detected: {len(new_content)} chars")

    # 2. READ EXISTING LOGS
    existing_data = []
    if os.path.exists(LOGS_FILE):
        try:
            with open(LOGS_FILE, "r") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    # 3. GENERATE ENTRY WITH GEMINI
    # (Using a standard prompt to format the raw text into a clean log entry)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            Format the following raw text into a clean JSON log entry for a developer changelog.
            Return ONLY raw JSON (no markdown formatting).
            Format:
            {{
                "date": "{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "status": "SUCCESS",
                "title": "GENERATE_A_COOL_TECH_TITLE_HERE",
                "content": "Summarized version of the update (use <br> for new lines)",
                "tags": ["#automated", "#update", "#brokenitguy"]
            }}
            
            Raw Text:
            {new_content}
            """
        )
        
        # Clean up response to ensure it's valid JSON
        cleaned_response = response.text.replace("```json", "").replace("```", "").strip()
        new_entry = json.loads(cleaned_response)
        
        # Add to the TOP of the list
        updated_data = [new_entry] + existing_data

    except Exception as e:
        print(f"⚠️ AI Generation failed: {e}")
        return

    # 4. SAVE EVERYTHING
    
    # Save JSON Logs
    with open(LOGS_FILE, "w") as f:
        json.dump(updated_data, f, indent=4)
    print("✅ logs.json updated.")

    # Generate RSS Feed (The new fix!)
    generate_rss(updated_data)

    # Update Marker (so we don't re-read the same text)
    with open(MARKER_FILE, "w") as f:
        f.write(str(current_pos))

    # 5. AUTO-PUSH TO GITHUB
    print(">> New log added. Pushing to GitHub...")
    try:
        subprocess.run(["git", "add", "logs.json", "feed.xml"], check=True) # Added feed.xml to git add
        subprocess.run(["git", "commit", "-m", "Auto-update logs & feed"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(">> SUCCESS: Website updated!")
    except subprocess.CalledProcessError as e:
        print(f"!! Git Error: {e}")

if __name__ == "__main__":
    update_logs()
