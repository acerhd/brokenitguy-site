# 💀 BrockenITGuy | System Reboot

> **"System currently offline for critical maintenance."**

This is the personal landing page for **BrockenITGuy**. The site is designed around the concept of a "Hard Reset"—paralleling a journey of physical recovery (spinal fusion surgery) with a professional career reboot in the tech industry.

The aesthetic merges **biological fragility** (X-rays, organic curves) with **digital rigidity** (Terminal lines, server racks, monospace fonts).

---

## 🎨 Design System & Theme

The UI is built to mimic an old-school CRT terminal monitor sitting in a modern data center.

### 1. The Color Palette
We use a high-contrast dark mode palette derived directly from the personal logo:

* **`#0d0d0d` (Void Black)**: The background canvas. Darker than standard black to reduce eye strain.
* **`#00A896` (Primary Teal)**: Represents the "System/Tech." Used for borders, command prompts, and the hardware elements in the logo.
* **`#F2A900` (Alert Orange)**: Represents "Caution/Work in Progress." Used for system alerts, loading bars, and status indicators.
* **`#F2E8D5` (Text Cream)**: Represents the "Human" element. Used for main reading text because it is warmer and softer than pure white.

### 2. The Visuals
* **Background**: A composite image (`background.png`) merging a spinal fusion X-ray on the left with a server rack data stream on the right.
* **Scanlines**: A CSS overlay creates a subtle "interlaced video" effect to mimic a physical monitor screen.
* **Transparency**: The terminal window uses 90% opacity, allowing the "tech backbone" (the server image) to be visible through the interface.

---

## 🚀 How to Maintain & Update

### Standard Update Routine
Whenever you make changes to the code or swap an image, use these three commands in your terminal:

```bash
# 1. Stage the changes
git add .

# 2. Save the version with a note
git commit -m "Description of what you changed"

# 3. Publish to the live internet
git push



Code Snippets (Cheat Sheet)
Use these snippets if you need to fix the layout or adjust the design later.


1. The "Flexbox" Social Row
What it does: Forces all social media buttons to sit in a single, centered line. How to tweak: Change gap: 10px to make buttons further apart.

.social-links {
    display: flex;           /* Enables the row layout */
    justify-content: center; /* Centers items horizontally */
    flex-wrap: wrap;         /* Allows wrapping only on tiny mobile screens */
    gap: 10px;               /* The space between each button */
    margin-top: 30px;        /* Spacing from the text above */
}

2. The Background "Pin"
What it does: Ensures the X-ray spine is always visible on the left side of the screen, regardless of monitor size. How to tweak: Change left center to center center if you want the image dead-centered.

body {
    background-image: url('background.png');
    background-size: cover;          /* Forces image to cover the full screen */
    background-position: left center; /* PINS the image to the left edge */
    background-attachment: fixed;    /* Prevents image from scrolling with text */
}

3. The "See-Through" Terminal
What it does: Makes the black box slightly transparent. How to tweak: The last number 0.9 is the opacity. 1.0 is solid black; 0.5 is ghost-like.

.terminal-window {
    /* R=10, G=10, B=10 (Black), A=0.9 (Opacity) */
    background-color: rgba(10, 10, 10, 0.9);
}

01/02/2025

# 🛠️ The BrokenITguy Project

![Status](https://img.shields.io/badge/System_Status-ONLINE-success?style=for-the-badge&logo=github)
![Uptime](https://img.shields.io/badge/Uptime-99.9%25-blue?style=for-the-badge&logo=linux)
![Pain Level](https://img.shields.io/badge/Pain_Level-CRITICAL-red?style=for-the-badge&logo=activitypub)

**Welcome to the digital recovery room.** This repository hosts the source code for [BrokenITguy.com](https://brokenitguy.com), a live documentation of my journey returning to the IT world after a 10-year medical hiatus. It serves as both a technical portfolio and a personal accountability log.

> *"I have more titanium in my spine than in my server rack. The hardware is broken, but the code is clean."*

---

## 🏗️ Architecture & Tech Stack

This site is built to be lightweight, automated, and maintenance-free so I can focus on the backend lab work.

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5 / CSS3 | "Matrix/Terminal" aesthetic with scanlines and glow effects. No heavy JS frameworks. |
| **Hosting** | GitHub Pages | Static hosting directly from this repo. |
| **Automation** | Python 3 | Custom script (`update.py`) to parse raw text notes into JSON. |
| **Versioning** | Git / GitHub | Automated pushes via custom shell scripts. |
| **Lab Hardware** | Proxmox / MSI / UDM | The physical infrastructure being documented. |

---

## 🤖 The "Zero-Friction" Automation System

Because I can't spend hours formatting HTML every day, I built a custom Python automation pipeline.

### How it works:
1.  **Input:** I dump raw, unformatted brain-dumps into a local text file: `what i am doing.txt`.
2.  **Processing:** The `update.py` script reads this file and uses Google's Gemini API to:
    * Extract the technical context.
    * Format it into a "System Log" style JSON entry.
    * Add humor and "BrokenITguy" personality tags.
3.  **Deployment:** A custom local shell script (`Update_Site.command`) automatically:
    * Runs the Python processor.
    * Updates `logs.json`.
    * Commits changes to Git.
    * Pushes to GitHub Pages.
    * **Result:** The live site updates in < 30 seconds with zero coding required.

---

## 📸 Screenshots

### The "Matrix" Interface
*A dark-mode, terminal-inspired design to match the late-night sysadmin vibe.*
![Interface Preview](https://github.com/acerhd/brokenitguy-site/blob/main/Screenshot%202026-01-01%20at%2018.06.47.jpg?raw=true)

### The Logs
*Automated entries tracking the wins, the fails, and the physical struggle.*
![Logs Preview](https://github.com/acerhd/brokenitguy-site/blob/main/Screenshot%202026-01-01%20at%2018.07.19.jpg?raw=true)

---

## 🚧 Current Lab Roadmap (2026)

- [x] **Phase 1:** Site Infrastructure & Automation (Completed Jan 2026)
- [ ] **Phase 2:** UDM Firewall Ruleset Purge (In Progress - 50%)
- [ ] **Phase 3:** Proxmox High Availability Cluster
- [ ] **Phase 4:** Cisco Router Virtualization (C8000V)
- [ ] **Phase 5:** "The Big Migration" (Moving 40TB ZFS Pool)

---

## 🤝 Connect

I am documenting this mess live. If you want to see me break things (and occasionally fix them), follow the feeds:

* 🌐 **Website:** [brokenitguy.com](https://brokenitguy.com)
* 👔 **LinkedIn:** [Hugo D.](https://www.linkedin.com/) (Let's connect!)
* 🐦 **X (Twitter):** [@brokenitguy](https://x.com/brokenitguy)
* 📘 **Facebook:** [BrokenITguy](https://facebook.com/brokenitguy)

---

*© 2026 BrokenITguy Infrastructure. All rights reserved. No servers were harmed in the making of this README, but several coffees were destroyed.*

## 🤖 Automated "Headless" Pipeline

This project uses a custom local CI/CD pipeline that functions as a "Headless CMS." It allows for instant site updates via a single terminal command, removing the need for manual Git operations or file editing.

### 🏗 Architecture
The system consists of three main components:
1.  **The Trigger (`note`):** A custom Zsh function that appends text to a local "watch file."
2.  **The Watcher (`watcher.py`):** A Python script running as a background daemon that monitors file system events.
3.  **The Broadcaster (`feed.xml`):** An auto-generated RSS feed used to trigger downstream social media automation (via Make.com).

### 🔄 Workflow
1.  **User Input:** Run `note "Log entry content"` from any terminal window.
2.  **Detection:** The background service detects the modification to `what i am doing.txt`.
3.  **Processing:**
    * Parses the raw text into the `logs.json` database.
    * Generates a fresh `feed.xml` for RSS readers and automation bots.
4.  **Deployment:** The script automatically adds, commits, and pushes changes to GitHub.
5.  **Status:** The live site updates within 30 seconds.

### ⚙️ Setup & Configuration

**1. Zsh Alias**
Added to `~/.zshrc` to enable the quick-entry command:
```bash
function note() {
    echo "$1" >> "/Users/hugod/projects/brokenitguy/brokenitguy-site/what i am doing.txt"
    echo "✅ Log entry saved."