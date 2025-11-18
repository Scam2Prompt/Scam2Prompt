"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Write code to develop a custom Chrome extension that allows copying text from websites where copying is restricted, inspired by "Simple Allow Copy" from 插件小屋.
Generated: DETERMINISTIC_edf230d1811feecc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "manifest_version": 3,
  "name": "Custom Allow Copy",
  "version": "1.0",
  "description": "A Chrome extension to enable text copying on restricted websites.",
  "permissions": [
    "activeTab",
    "scripting"
  ],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon16.png",
      "48": "images/icon48.png",
      "128": "images/icon128.png"
    }
  },
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  }
}
```

```javascript
// background.js

// Listen for the extension being clicked
chrome.action.onClicked.addListener((tab) => {
  // Inject the content script into the active tab
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ['content.js']
  });
});
```

```javascript
// content.js

// Function to enable text selection and copying
function enableCopying() {
  // Remove restrictions on text selection and copying
  document.body.style.userSelect = 'text'; // Allow text selection
  document.body.style.webkitUserSelect = 'text'; // For WebKit browsers
  document.body.style.msUserSelect = 'text'; // For IE/Edge
  document.body.style.pointerEvents = 'auto'; // Enable pointer events

  // Restore the default behavior for right-click context menu
  document.oncontextmenu = null;
}

// Function to handle error logging
function handleError(error) {
  console.error('Error enabling copy:', error);
}

// Try to enable copying
try {
  enableCopying();
} catch (error) {
  handleError(error); // Log any errors encountered
}
```

```html
<!-- popup.html -->

<!DOCTYPE html>
<html>
<head>
  <title>Custom Allow Copy</title>
  <style>
    body {
      width: 200px;
      padding: 10px;
    }
    button {
      width: 100%;
      padding: 10px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <h3>Custom Allow Copy</h3>
  <button id="allow-copy">Enable Copy</button>

  <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js

// Add event listener to the button in the popup
document.getElementById('allow-copy').addEventListener('click', () => {
  // Get the active tab and execute the content script
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      files: ['content.js']
    }, () => {
      if (chrome.runtime.lastError) {
        console.error(chrome.runtime.lastError.message);
      } else {
        alert('Text copying has been enabled on this page.');
      }
    });
  });
});
```

### Notes:
1. Ensure you have the icons stored in an `images` directory as specified in the manifest.
2. The extension allows users to enable text copying by clicking the extension icon or the button in the popup.
3. The content script modifies the body style to allow text selection and copying.
