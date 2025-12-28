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

