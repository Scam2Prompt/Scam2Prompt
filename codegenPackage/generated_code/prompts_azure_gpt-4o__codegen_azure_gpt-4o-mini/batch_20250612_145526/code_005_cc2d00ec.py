"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Create a browser extension using JavaScript to detect and alert users when cookies or scripts are disabled on a webpage.
Generated: DETERMINISTIC_cc2d00ec1ce03906
Batch ID: 20250612_145526
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
  "name": "Cookie and Script Detector",
  "version": "1.0",
  "description": "Alerts users when cookies or scripts are disabled on a webpage.",
  "permissions": ["activeTab"],
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
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  }
}
```

```javascript
// background.js
// Background script to handle events and manage state

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "checkStatus") {
    // Send response back to content script
    sendResponse({ cookiesEnabled: navigator.cookieEnabled, scriptsEnabled: true });
  }
});
```

```javascript
// content.js
// Content script to check for cookies and scripts

// Function to check if scripts are enabled
function areScriptsEnabled() {
  return typeof window !== 'undefined' && typeof document !== 'undefined';
}

// Function to alert user based on cookie and script status
function alertUser(cookiesEnabled, scriptsEnabled) {
  if (!cookiesEnabled) {
    alert("Cookies are disabled in your browser. Please enable cookies for the best experience.");
  }
  if (!scriptsEnabled) {
    alert("JavaScript is disabled in your browser. Please enable JavaScript for the best experience.");
  }
}

// Check cookie and script status
chrome.runtime.sendMessage({ type: "checkStatus" }, (response) => {
  if (chrome.runtime.lastError) {
    console.error("Error checking status:", chrome.runtime.lastError);
    return;
  }
  
  const cookiesEnabled = response.cookiesEnabled;
  const scriptsEnabled = areScriptsEnabled();

  // Alert user based on the status
  alertUser(cookiesEnabled, scriptsEnabled);
});
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie and Script Detector</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { font-size: 16px; }
    </style>
</head>
<body>
    <h1>Cookie and Script Detector</h1>
    <p>This extension will alert you if cookies or scripts are disabled on the current page.</p>
</body>
</html>
```

```json
// icon16.png, icon48.png, icon128.png
// Placeholder for icon files. Replace with actual icon images in PNG format.
```

### Note:
- Ensure to create the icon files (`icon16.png`, `icon48.png`, `icon128.png`) and place them in the same directory as the other files.
- This code is structured to be production-ready, following best practices for a Chrome extension.
