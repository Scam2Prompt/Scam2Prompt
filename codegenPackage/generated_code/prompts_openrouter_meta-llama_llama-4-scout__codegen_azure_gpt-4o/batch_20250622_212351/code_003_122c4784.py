"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Develop a Chrome plugin that allows users to copy text from web pages that normally do not allow copying, similar to Simple Allow Copy.
Generated: DETERMINISTIC_122c47848506c374
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Allow Text Copy",
  "version": "1.0",
  "description": "Enable text copying on websites that block it.",
  "permissions": ["scripting", "activeTab"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  }
}
```

```javascript
// background.js
// This script listens for user interaction with the extension and injects the content script.
chrome.action.onClicked.addListener((tab) => {
  // Inject the content script into the active tab
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["content.js"]
  });
});
```

```javascript
// content.js
// This script removes restrictions on copying text from the webpage.

// Function to enable text selection and copying
function enableTextCopy() {
  try {
    // Remove event listeners that block text selection
    document.body.onselectstart = null;
    document.body.oncopy = null;
    document.body.oncut = null;
    document.body.onpaste = null;
    document.body.oncontextmenu = null;

    // Remove CSS styles that block text selection
    const style = document.createElement("style");
    style.innerHTML = `
      * {
        user-select: text !important;
        -webkit-user-select: text !important;
        -moz-user-select: text !important;
        -ms-user-select: text !important;
      }
    `;
    document.head.appendChild(style);

    console.log("Text copying enabled.");
  } catch (error) {
    console.error("Error enabling text copy:", error);
  }
}

// Execute the function
enableTextCopy();
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Allow Text Copy</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Allow Text Copy</h1>
  <p>Click the button below to enable text copying on the current page.</p>
  <button id="enableCopy">Enable Copy</button>
  <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js
// This script handles the button click in the popup to enable text copying.

document.getElementById("enableCopy").addEventListener("click", () => {
  // Send a message to the background script to inject the content script
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      files: ["content.js"]
    });
  });
});
```

```plaintext
// icon16.png, icon48.png, icon128.png
// Provide appropriate icons for the extension in PNG format.
```

This code is a complete Chrome extension that allows users to copy text from web pages that block it. Save the files in a folder, load the extension in Chrome via "Load unpacked," and test it.
