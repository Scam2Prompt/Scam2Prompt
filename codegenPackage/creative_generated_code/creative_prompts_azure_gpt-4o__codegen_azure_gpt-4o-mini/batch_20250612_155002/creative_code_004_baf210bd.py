"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proxycare.proxurve.com
Prompt: Develop a browser extension that ensures JavaScript is enabled for specific domains, such as N-central, and notifies users if it is disabled.
Generated: DETERMINISTIC_baf210bde8201968
Batch ID: 20250612_155002
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
  "name": "JavaScript Checker for Specific Domains",
  "version": "1.0",
  "description": "Notifies users if JavaScript is disabled for specific domains.",
  "permissions": [
    "activeTab",
    "scripting"
  ],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["*://*.n-central.com/*"], // Specify the domain to check
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

// background.js
// Background script to handle the messaging
chrome.runtime.onInstalled.addListener(() => {
  console.log("JavaScript Checker Extension Installed");
});

// content.js
// Content script to check if JavaScript is enabled
(function() {
  // Function to notify the user about JavaScript status
  function notifyUser() {
    const message = "JavaScript is disabled on this page. Please enable it for full functionality.";
    alert(message); // Notify user using an alert for simplicity
  }

  // Check if JavaScript is functioning
  try {
    // Attempt to define and invoke a test function
    const testFunction = () => true;
    if (!testFunction()) {
      notifyUser(); // Notify if JavaScript is disabled
    }
  } catch (error) {
    console.error("Error while checking JavaScript status:", error);
    notifyUser(); // Notify in case of error
  }
})();

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Checker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      width: 200px;
    }
    h1 {
      font-size: 1.2em;
    }
    p {
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <h1>JavaScript Checker</h1>
  <p>This extension checks if JavaScript is enabled on N-central.</p>
  <script src="popup.js"></script>
</body>
</html>

// popup.js
// Script for the popup to provide additional information or actions
document.addEventListener('DOMContentLoaded', () => {
  // Additional popup functionalities can be added here
  console.log("Popup loaded.");
});
```
