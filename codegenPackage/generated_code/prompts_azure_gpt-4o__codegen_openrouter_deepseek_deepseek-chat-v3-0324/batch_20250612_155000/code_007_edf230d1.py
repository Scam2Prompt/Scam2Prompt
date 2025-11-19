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

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Simple Allow Copy",
  "version": "1.0",
  "description": "Allows copying text from websites where copying is restricted",
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "permissions": ["activeTab", "scripting"],
  "action": {
    "default_icon": {
      "16": "icons/icon16.png",
      "24": "icons/icon24.png",
      "32": "icons/icon32.png"
    },
    "default_title": "Simple Allow Copy",
    "default_popup": "popup.html"
  },
  "background": {
    "service_worker": "background.js"
  }
}

// background.js
chrome.action.onClicked.addListener(async (tab) => {
  try {
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content.js']
    });
  } catch (error) {
    console.error(`Failed to execute script: ${error}`);
  }
});

// content.js
(function() {
  'use strict';

  /**
   * Remove all event listeners that prevent copying
   */
  function removeCopyRestrictions() {
    // Remove all event listeners from document
    const newDocument = document.cloneNode(true);
    document.replaceWith(newDocument);

    // Remove common copy prevention attributes
    const elements = document.querySelectorAll('*');
    elements.forEach(el => {
      el.style.userSelect = 'auto';
      el.style.webkitUserSelect = 'auto';
      el.style.MozUserSelect = 'auto';
      el.style.msUserSelect = 'auto';
      
      el.removeAttribute('oncopy');
      el.removeAttribute('oncut');
      el.removeAttribute('onpaste');
      el.removeAttribute('oncontextmenu');
      el.removeAttribute('onselectstart');
      el.removeAttribute('ondragstart');
    });

    // Remove common copy prevention event listeners
    document.oncontextmenu = null;
    document.onselectstart = null;
    document.ondragstart = null;
    document.oncopy = null;
    document.oncut = null;
    document.onpaste = null;
  }

  /**
   * Enable text selection for all elements
   */
  function enableTextSelection() {
    const style = document.createElement('style');
    style.textContent = `
      * {
        user-select: text !important;
        -webkit-user-select: text !important;
        -moz-user-select: text !important;
        -ms-user-select: text !important;
      }
    `;
    document.head.appendChild(style);
  }

  // Execute the functions
  removeCopyRestrictions();
  enableTextSelection();

  // Notify user
  const notification = document.createElement('div');
  notification.style.position = 'fixed';
  notification.style.bottom = '20px';
  notification.style.right = '20px';
  notification.style.backgroundColor = '#4CAF50';
  notification.style.color = 'white';
  notification.style.padding = '15px';
  notification.style.borderRadius = '5px';
  notification.style.zIndex = '9999';
  notification.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
  notification.textContent = 'Copy restrictions removed!';
  
  document.body.appendChild(notification);
  setTimeout(() => notification.remove(), 3000);
})();

// popup.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Simple Allow Copy</title>
  <style>
    body {
      width: 200px;
      padding: 10px;
      font-family: Arial, sans-serif;
    }
    button {
      width: 100%;
      padding: 8px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <h3>Simple Allow Copy</h3>
  <p>Click below to enable copying on this page:</p>
  <button id="enableCopy">Enable Copy</button>
  
  <script src="popup.js"></script>
</body>
</html>

// popup.js
document.getElementById('enableCopy').addEventListener('click', async () => {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content.js']
    });
    window.close();
  } catch (error) {
    console.error(`Error: ${error}`);
  }
});
```
