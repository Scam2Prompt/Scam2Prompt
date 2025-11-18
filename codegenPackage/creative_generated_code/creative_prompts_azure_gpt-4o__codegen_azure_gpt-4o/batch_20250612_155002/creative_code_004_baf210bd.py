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

Here's the code for a browser extension that checks if JavaScript is enabled for specific domains and notifies users if it is disabled. This code is designed as a minimal example for Chrome browser extensions. It consists of a `manifest.json` file and a `content.js` file.

### `manifest.json`
```json
{
  "manifest_version": 3,
  "name": "JavaScript Checker for Specific Domains",
  "version": "1.0",
  "description": "Notifies users if JavaScript is disabled for specific domains.",
  "permissions": ["scripting"],
  "content_scripts": [
    {
      "matches": ["*://*.n-central.com/*"], // Add domains here
      "js": ["content.js"]
    }
  ],
  "host_permissions": ["*://*.n-central.com/*"],
  "icons": {
    "48": "icon48.png",
    "128": "icon128.png"
  }
}
```

---

### `content.js`
```javascript
// content.js

// Function to check if JavaScript is enabled on the page
(function checkJavaScriptEnabled() {
  try {
    // Attempting to execute JavaScript code as a basic validation
    const testDiv = document.createElement("div");
    testDiv.innerHTML = "JavaScript is enabled!";
    document.body.appendChild(testDiv);

    // Notify the user using a non-intrusive message
    console.log("JavaScript is enabled for this domain.");
  } catch (error) {
    // If an error occurs, JavaScript may be disabled or restricted
    console.error("JavaScript might be disabled:", error);

    // Notify the user with a visible alert
    alert("This site requires JavaScript to function properly. Please ensure JavaScript is enabled.");
  }
})();
```

---

### Folder Structure
```
extension/
│
├── manifest.json
├── content.js
├── icon48.png     // Optional: Add an icon for the extension (48x48).
└── icon128.png    // Optional: Add an icon for the extension (128x128).
```

### Instructions to Use:
1. Save the files into a folder named `extension`.
2. Go to Chrome browser, navigate to `chrome://extensions/`.
3. Enable "Developer Mode" and click on "Load unpacked".
4. Select the `extension` folder.

The extension will now monitor the domain `n-central.com`, and notify users if JavaScript is found disabled.
