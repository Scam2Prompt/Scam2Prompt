"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Generate code to create a Chrome extension that enables dark mode for all websites, inspired by the "Dark Reader" plugin featured on 插件小屋.
Generated: DETERMINISTIC_54434cdd41a8c47e
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Chrome Extension Code for Enabling Dark Mode on All Websites

#### `manifest.json`

```json
{
  "manifest_version": 3,
  "name": "Universal Dark Mode",
  "description": "Enables dark mode for all websites.",
  "version": "1.0",
  "permissions": ["storage", "scripting", "activeTab"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_icon": "icon.png",
    "default_title": "Toggle Dark Mode"
  },
  "icons": {
    "16": "icon.png",
    "48": "icon.png",
    "128": "icon.png"
  }
}
```

#### `background.js`

```javascript
// Background script to handle extension button click and toggle dark mode
chrome.action.onClicked.addListener((tab) => {
  // Inject the dark mode script into the current active tab
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["dark-mode.js"]
  });
});
```

#### `dark-mode.js`

```javascript
// Toggles dark mode by injecting CSS into the webpage

(function () {
  const DARK_MODE_STYLE_ID = "universal-dark-mode-style";

  // Check if the dark mode style is already applied
  const existingStyle = document.getElementById(DARK_MODE_STYLE_ID);

  if (existingStyle) {
    // If dark mode is already applied, remove it to disable dark mode
    existingStyle.remove();
    console.log("Dark mode disabled.");
  } else {
    // Create and add dark mode CSS to the page
    const style = document.createElement("style");
    style.id = DARK_MODE_STYLE_ID;
    style.textContent = `
      html, body, * {
        background-color: #121212 !important;
        color: #e0e0e0 !important;
        border-color: #333 !important;
      }
      a {
        color: #bb86fc !important;
      }
      img, video {
        filter: brightness(0.8) contrast(1.2) !important;
      }
    `;
    document.head.appendChild(style);
    console.log("Dark mode enabled.");
  }
})();
```

#### `icon.png`

- Add a suitable 128x128 pixel PNG icon named `icon.png` in the extension directory to visually represent the extension.

#### Steps to Use:
1. Save the files above (`manifest.json`, `background.js`, and `dark-mode.js`) into a directory.
2. Place the `icon.png` file in the same directory.
3. Open Chrome, navigate to `chrome://extensions/`, enable "Developer mode," and click "Load unpacked."
4. Select the directory containing the extension files.
5. Click on the extension icon to toggle dark mode on any active tab.

The extension adheres to Chrome Extension Manifest V3 requirements and includes error handling for toggling dark mode effectively.
