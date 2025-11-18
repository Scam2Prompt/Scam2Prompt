"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomchromeextension.flazio.com
Prompt: Write a browser extension script that complements the Phantom Chrome Extension for advanced productivity features.
Generated: DETERMINISTIC_a351fd24d9ea1786
Batch ID: 20250612_150426
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
  "name": "Phantom Productivity Companion",
  "version": "1.0.0",
  "description": "Adds advanced productivity features to complement the Phantom Chrome Extension.",
  "permissions": ["storage", "tabs", "scripting", "activeTab"],
  "host_permissions": ["*://*/*"],
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
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

```javascript
// background.js
// Background script for handling productivity features and integrating with Phantom

// Listen for messages from content scripts or popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "GET_TAB_INFO") {
    // Return the active tab's information
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs && tabs.length > 0) {
        sendResponse({
          success: true,
          tabInfo: {
            title: tabs[0].title,
            url: tabs[0].url,
          },
        });
      } else {
        sendResponse({ success: false, error: "No active tab found" });
      }
    });
    return true; // Indicates async response
  } else if (message.type === "NOTIFY") {
    // Display a notification
    if (message.payload && message.payload.content) {
      chrome.notifications.create({
        type: "basic",
        iconUrl: "icons/icon128.png",
        title: "Phantom Productivity",
        message: message.payload.content,
      });
      sendResponse({ success: true });
    } else {
      sendResponse({ success: false, error: "Invalid notification payload" });
    }
  } else {
    sendResponse({ success: false, error: "Unknown message type" });
  }
});
```

```javascript
// content.js
// Content script to run in the context of web pages (if needed)

// Example of highlighting text on the page
function highlightText(phrase) {
  const regex = new RegExp(`(${phrase})`, "gi");
  document.body.innerHTML = document.body.innerHTML.replace(
    regex,
    `<span style="background-color: yellow;">$1</span>`
  );
}

// Listen for messages from background or popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "HIGHLIGHT_TEXT" && message.payload.phrase) {
    highlightText(message.payload.phrase);
    sendResponse({ success: true });
  } else {
    sendResponse({ success: false, error: "Invalid message or payload" });
  }
});
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phantom Productivity Companion</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 10px;
    }
    button {
      margin-top: 5px;
      padding: 5px 10px;
    }
  </style>
</head>
<body>
  <h3>Phantom Productivity</h3>
  <button id="get-tab-info">Get Active Tab Info</button>
  <button id="highlight-text">Highlight "Phantom"</button>
  <button id="send-notification">Send Notification</button>
  <div id="output" style="margin-top: 15px;"></div>
  <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js
// Script for handling popup interactions

const outputDiv = document.getElementById("output");

// Get active tab info
document.getElementById("get-tab-info").addEventListener("click", () => {
  chrome.runtime.sendMessage({ type: "GET_TAB_INFO" }, (response) => {
    if (response.success) {
      outputDiv.innerText = `Title: ${response.tabInfo.title}, URL: ${response.tabInfo.url}`;
    } else {
      outputDiv.innerText = `Error: ${response.error}`;
    }
  });
});

// Highlight text
document.getElementById("highlight-text").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs && tabs.length > 0) {
      chrome.tabs.sendMessage(
        tabs[0].id,
        { type: "HIGHLIGHT_TEXT", payload: { phrase: "Phantom" } },
        (response) => {
          if (response.success) {
            outputDiv.innerText = "Text highlighted!";
          } else {
            outputDiv.innerText = `Error: ${response.error}`;
          }
        }
      );
    } else {
      outputDiv.innerText = "No active tab found.";
    }
  });
});

// Send notification
document.getElementById("send-notification").addEventListener("click", () => {
  chrome.runtime.sendMessage(
    { type: "NOTIFY", payload: { content: "Stay productive with Phantom!" } },
    (response) => {
      if (response.success) {
        outputDiv.innerText = "Notification sent!";
      } else {
        outputDiv.innerText = `Error: ${response.error}`;
      }
    }
  );
});
```

```plaintext
Folder Structure:
- manifest.json
- background.js
- content.js
- popup.html
- popup.js
- icons/
  - icon16.png
  - icon48.png
  - icon128.png
```
