"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Generate code for a Chrome extension that enables dark mode for any website, similar to Dark Reader, using CSS filtering.
Generated: DETERMINISTIC_587f74c1f38f4834
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**manifest.json**
```json
{
  "manifest_version": 3,
  "name": "Dark Mode Extension",
  "version": "1.0",
  "description": "Enables dark mode for any website using CSS filtering",
  "permissions": ["activeTab"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon16.png",
      "48": "images/icon48.png",
      "128": "images/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["contentScript.js"]
    }
  ]
}
```

**contentScript.js**
```javascript
// Listen for messages from popup script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'toggleDarkMode') {
    toggleDarkMode();
  }
});

// Function to toggle dark mode
function toggleDarkMode() {
  // Check if dark mode is already enabled
  const isDarkModeEnabled = document.documentElement.classList.contains('dark-mode');
  
  // Toggle dark mode
  if (isDarkModeEnabled) {
    document.documentElement.classList.remove('dark-mode');
  } else {
    document.documentElement.classList.add('dark-mode');
  }
}

// Inject CSS filter when page loads
document.addEventListener('DOMContentLoaded', () => {
  const style = document.createElement('style');
  style.textContent = `
    .dark-mode {
      filter: invert(100%) hue-rotate(180deg);
    }
    .dark-mode img {
      filter: invert(100%) hue-rotate(180deg);
    }
    .dark-mode pre, .dark-mode code, .dark-mode pre *, .dark-mode code * {
      background-color: #2b2b2b;
      color: #fff;
    }
  `;
  document.head.appendChild(style);
});
```

**popup.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Dark Mode Extension</title>
    <style>
      body {
        width: 200px;
        height: 100px;
        font-family: Arial, sans-serif;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h1>Dark Mode Extension</h1>
    <button id="toggle-dark-mode">Toggle Dark Mode</button>
    <script src="popup.js"></script>
  </body>
</html>
```

**popup.js**
```javascript
// Get toggle button
const toggleButton = document.getElementById('toggle-dark-mode');

// Add event listener to toggle button
toggleButton.addEventListener('click', () => {
  // Send message to content script to toggle dark mode
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'toggleDarkMode' });
  });
});
```

**icon files:**
Create the following icon files and place them in the `images` directory:
- `icon16.png`
- `icon48.png`
- `icon128.png`
