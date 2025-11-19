"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Write code to develop a custom Chrome extension that allows copying text from websites where copying is restricted, inspired by "Simple Allow Copy" from 插件小屋.
Generated: DETERMINISTIC_edf230d1811feecc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "manifest_version": 3,
  "name": "Custom Allow Copy",
  "version": "1.0",
  "description": "A Chrome extension to allow copying text from websites where copying is restricted.",
  "permissions": [
    "activeTab",
    "scripting"
  ],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

```javascript
// background.js
chrome.runtime.onInstalled.addListener(() => {
  console.log("Custom Allow Copy extension installed.");
});
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Allow Copy</title>
    <style>
        body { width: 200px; }
        button { width: 100%; padding: 10px; }
    </style>
</head>
<body>
    <button id="enable-copy">Enable Copy</button>
    <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js
document.getElementById('enable-copy').addEventListener('click', () => {
    // Send a message to the content script to enable copying
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "enableCopy" });
    });
});
```

```javascript
// content.js
// Listen for messages from the popup to enable copying
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "enableCopy") {
        enableCopy();
        sendResponse({ status: "Copying enabled" });
    }
});

// Function to enable copying on the page
function enableCopy() {
    // Remove any restrictions on text selection
    document.body.style.userSelect = 'text';
    document.body.style.pointerEvents = 'auto';

    // Remove any event listeners that prevent copying
    const preventCopyEvents = ['copy', 'cut', 'paste', 'contextmenu'];
    preventCopyEvents.forEach(event => {
        document.body.removeEventListener(event, preventDefault);
    });

    // Log to console for debugging
    console.log("Copying enabled on this page.");
}

// Prevent default behavior for copy, cut, paste, and context menu events
function preventDefault(e) {
    e.preventDefault();
}
```

### Icons
- Place your icon images in an `icons` folder with the names `icon16.png`, `icon48.png`, and `icon128.png`.

### Notes
- Ensure that you have the necessary permissions and that your extension complies with Chrome Web Store policies.
- Test the extension thoroughly on various websites to ensure it works as intended.
