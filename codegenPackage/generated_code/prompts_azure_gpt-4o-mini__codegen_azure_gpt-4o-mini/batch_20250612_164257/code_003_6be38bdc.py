"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Generate a script that checks for browser compatibility when accessing the Paylocity login page, based on the supported browsers listed.
Generated: DETERMINISTIC_6be38bdce4d1b5d9
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// browserCompatibilityCheck.js

/**
 * Checks if the user's browser is compatible with the Paylocity login page.
 * Supported browsers: Chrome, Firefox, Safari, Edge.
 * 
 * @returns {boolean} - Returns true if the browser is supported, false otherwise.
 */
function isBrowserSupported() {
    const userAgent = navigator.userAgent;
    const supportedBrowsers = {
        Chrome: /Chrome\/[0-9]+/,
        Firefox: /Firefox\/[0-9]+/,
        Safari: /Safari\/[0-9]+/,
        Edge: /Edg\/[0-9]+/
    };

    // Check for each supported browser
    for (const [browser, regex] of Object.entries(supportedBrowsers)) {
        if (regex.test(userAgent)) {
            return true; // Supported browser found
        }
    }
    return false; // No supported browser found
}

/**
 * Displays a message to the user based on browser compatibility.
 */
function checkBrowserCompatibility() {
    try {
        if (isBrowserSupported()) {
            console.log("Your browser is supported. You can access the Paylocity login page.");
        } else {
            console.error("Your browser is not supported. Please use Chrome, Firefox, Safari, or Edge.");
            alert("Your browser is not supported. Please use Chrome, Firefox, Safari, or Edge.");
        }
    } catch (error) {
        console.error("An error occurred while checking browser compatibility:", error);
        alert("An unexpected error occurred. Please try again later.");
    }
}

// Run the browser compatibility check on page load
document.addEventListener("DOMContentLoaded", checkBrowserCompatibility);
```

This script checks the user's browser against a list of supported browsers for the Paylocity login page and provides appropriate feedback. It includes error handling to manage unexpected issues gracefully.
