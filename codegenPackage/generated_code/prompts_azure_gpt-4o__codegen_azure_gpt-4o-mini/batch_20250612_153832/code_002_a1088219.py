"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-three.vercel.app
Prompt: Generate code for detecting if the user is running Chrome and displaying a message if the browser is incompatible, as described on the OpenSea clone website.
Generated: DETERMINISTIC_a10882195a689b7c
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to detect if the user is running Google Chrome
function isChrome() {
    // Check the user agent string for 'Chrome'
    const userAgent = navigator.userAgent;
    const isChromeBrowser = /Chrome/.test(userAgent) && /Google Inc/.test(navigator.vendor);

    return isChromeBrowser;
}

// Function to display an alert message if the browser is incompatible
function checkBrowserCompatibility() {
    // Check if the browser is not Chrome
    if (!isChrome()) {
        // Display an alert message to the user
        alert("Your browser is incompatible. Please use Google Chrome for the best experience.");
    }
}

// Execute the browser compatibility check on page load
window.onload = function() {
    try {
        checkBrowserCompatibility();
    } catch (error) {
        console.error("An error occurred while checking browser compatibility:", error);
    }
};
```
