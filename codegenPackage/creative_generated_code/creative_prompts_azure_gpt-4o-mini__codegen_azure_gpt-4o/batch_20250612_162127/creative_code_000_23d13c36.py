"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Generate a code snippet for a Chrome extension that enhances user experience based on features discussed on Crx搜搜.
Generated: DETERMINISTIC_23d13c36b90570d7
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Enhanced UX Extension",
  "version": "1.0.0",
  "description": "A Chrome extension to enhance user experience based on Crx搜搜 features.",
  "permissions": ["storage", "activeTab", "scripting"],
  "host_permissions": ["<all_urls>"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "css": ["styles.css"]
    }
  ]
}
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Enhanced UX Extension</title>
  <link rel="stylesheet" href="popup.css">
</head>
<body>
  <h1>Enhanced UX</h1>
  <button id="apply-feature">Apply Feature</button>
  <script src="popup.js"></script>
</body>
</html>
```

```css
/* styles.css (For content scripts) */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
}

/* popup.css */
body {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 10px;
}

button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
```

```javascript
// background.js

// Background script to handle extension-wide events
chrome.runtime.onInstalled.addListener(() => {
  console.log("Enhanced UX Extension installed successfully!");
});

// Listener for any messages sent from other parts of the extension
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.command === "log") {
    console.log("Received log message:", message.data);
    sendResponse({ status: "success" });
  } else {
    sendResponse({ status: "unknown command" });
  }
});
```

```javascript
// content.js

// Content script to enhance UX on pages
try {
  console.log("Enhanced UX Content Script Loaded");

  // Example: Highlight all paragraphs on the page
  const paragraphs = document.querySelectorAll("p");
  paragraphs.forEach((p) => {
    p.style.backgroundColor = "yellow";
  });

  // Example: Send a message to the background script
  chrome.runtime.sendMessage(
    { command: "log", data: "Content script executed successfully" },
    (response) => {
      console.log("Background response:", response);
    }
  );
} catch (error) {
  console.error("Error in content script:", error);
}
```

```javascript
// popup.js

// Script for popup UI interaction
document.getElementById("apply-feature").addEventListener("click", () => {
  alert("Feature applied!");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const activeTab = tabs[0];
    chrome.scripting.executeScript({
      target: { tabId: activeTab.id },
      function: () => {
        // Example feature: Change background color of the page
        document.body.style.backgroundColor = "#e0f7fa";
      },
    });
  });
});
```

```json
{
  "icons": {
    "icon16.png": "Your 16x16 icon file",
    "icon48.png": "Your 48x48 icon file",
    "icon128.png": "Your 128x128 icon file"
  }
}
```
