"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Create a browser extension using JavaScript to detect and alert users when cookies or scripts are disabled on a webpage.
Generated: DETERMINISTIC_cc2d00ec1ce03906
Batch ID: 20250612_145526
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
  "name": "Cookies and Scripts Detector",
  "version": "1.0",
  "description": "Alerts users if cookies or scripts are disabled on a webpage.",
  "permissions": ["scripting", "tabs"],
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
  }
}
```

```javascript
// background.js
// Runs in the background of the browser to check for cookies and script functionality.
chrome.runtime.onInstalled.addListener(() => {
  console.log("Cookies and Scripts Detector extension installed.");
});

chrome.action.onClicked.addListener((tab) => {
  // Inject content script to check for cookies and JavaScript status.
  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      files: ["content.js"],
    },
    () => {
      if (chrome.runtime.lastError) {
        console.error("Error injecting content script:", chrome.runtime.lastError.message);
      }
    }
  );
});
```

```javascript
// content.js
// Content script to detect if cookies or JavaScript are disabled on the current webpage.
(function () {
  try {
    // Check for cookies functionality
    document.cookie = "testcookie=1";
    const cookiesEnabled = document.cookie.indexOf("testcookie=1") !== -1;

    // Clean up the test cookie
    document.cookie = "testcookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

    // Check for script functionality
    const scriptsEnabled = true; // If this script runs, JavaScript is enabled.

    // Prepare the alert message
    let alertMessage = "";
    if (!cookiesEnabled) alertMessage += "Warning: Cookies are disabled.\n";
    if (!scriptsEnabled) alertMessage += "Warning: JavaScript is disabled.\n";

    // Notify the user if any feature is disabled
    if (alertMessage) {
      alert(alertMessage.trim());
    }
  } catch (error) {
    console.error("Error detecting cookies or scripts:", error);
    alert("An error occurred while checking cookies or script functionality.");
  }
})();
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cookies and Scripts Detector</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 10px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Cookies and Scripts Detector</h1>
  <p>Click the extension icon to check if cookies or scripts are disabled.</p>
</body>
</html>
```

```json
// icons directory should include the following icons:
// - icons/icon16.png
// - icons/icon48.png
// - icons/icon128.png
// Ensure these files exist and are appropriately designed for the extension.
```
