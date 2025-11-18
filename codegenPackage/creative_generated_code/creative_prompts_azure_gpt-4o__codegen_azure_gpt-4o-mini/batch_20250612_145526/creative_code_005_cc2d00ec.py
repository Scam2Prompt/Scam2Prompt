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
// content.js - A simple browser extension to detect if cookies or scripts are disabled on a webpage

// Function to check if cookies are enabled
function areCookiesEnabled() {
    // Try to set a test cookie
    document.cookie = "testcookie=1; max-age=1; path=/";
    const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1;
    
    // Clean up the test cookie
    document.cookie = "testcookie=; max-age=0; path=/";
    
    return cookiesEnabled;
}

// Function to check if scripts are enabled
function areScriptsEnabled() {
    // Create a test script element
    const testScript = document.createElement('script');
    testScript.textContent = 'window.testScriptEnabled = true;';
    
    // Append script to the document and check if it executes
    document.head.appendChild(testScript);
    const scriptsEnabled = window.testScriptEnabled === true;
    
    // Remove the test script element
    document.head.removeChild(testScript);
    
    return scriptsEnabled;
}

// Function to alert the user based on the checks
function alertUser() {
    let messages = [];
    
    if (!areCookiesEnabled()) {
        messages.push("Cookies are disabled in your browser.");
    }
    
    if (!areScriptsEnabled()) {
        messages.push("JavaScript is disabled in your browser.");
    }
    
    // If there are any messages, alert the user
    if (messages.length > 0) {
        alert(messages.join("\n"));
    }
}

// Run the checks when the document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    try {
        alertUser();
    } catch (error) {
        console.error("Error during detection:", error);
        alert("An error occurred while checking for cookies and scripts. Please try again.");
    }
});
```

```json
// manifest.json - Manifest file for the browser extension

{
    "manifest_version": 3,
    "name": "Cookie and Script Detection",
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

```html
<!-- popup.html - Basic HTML for the extension's popup (if needed) -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie and Script Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 10px;
            width: 200px;
        }
    </style>
</head>
<body>
    <h3>Cookie and Script Detector</h3>
    <p>This extension alerts you if cookies or scripts are disabled.</p>
</body>
</html>
```

**Note:** Create an `images` folder with appropriate icons (icon16.png, icon48.png, icon128.png) for the extension.
