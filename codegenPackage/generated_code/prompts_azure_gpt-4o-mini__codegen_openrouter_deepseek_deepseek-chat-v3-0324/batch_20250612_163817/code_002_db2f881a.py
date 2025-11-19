"""
Generated Code Metadata:
========================
Original URL: https://devoursol.com
Prompt: Generate code to enable JavaScript and cookies in a web application to improve user experience during security checks.
Generated: DETERMINISTIC_db2f881ad041449e
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and cookies are supported in the browser.
 * If not, displays a warning message to the user.
 * 
 * @returns {boolean} True if both JavaScript and cookies are enabled, false otherwise.
 */
function checkBrowserFeatures() {
    try {
        // Check if JavaScript is enabled (this code itself wouldn't run if it wasn't)
        const jsEnabled = true;

        // Check if cookies are enabled
        let cookiesEnabled = false;
        document.cookie = "testCookie=1; SameSite=Lax; path=/";
        if (document.cookie.indexOf("testCookie=") !== -1) {
            cookiesEnabled = true;
            // Clean up test cookie
            document.cookie = "testCookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        }

        if (!cookiesEnabled) {
            showFeatureWarning("cookies");
            return false;
        }

        return true;
    } catch (error) {
        console.error("Error checking browser features:", error);
        showFeatureWarning("unknown");
        return false;
    }
}

/**
 * Displays a warning message to the user about required browser features.
 * 
 * @param {string} feature - The feature that's not supported ('cookies' or 'unknown')
 */
function showFeatureWarning(feature) {
    try {
        const warningElement = document.createElement("div");
        warningElement.style.position = "fixed";
        warningElement.style.top = "0";
        warningElement.style.left = "0";
        warningElement.style.right = "0";
        warningElement.style.backgroundColor = "#ffcc00";
        warningElement.style.color = "#000";
        warningElement.style.padding = "10px";
        warningElement.style.textAlign = "center";
        warningElement.style.zIndex = "1000";

        let message = "";
        if (feature === "cookies") {
            message = "Please enable cookies in your browser settings for optimal experience.";
        } else {
            message = "Please enable JavaScript and cookies in your browser settings for optimal experience.";
        }

        warningElement.textContent = message;
        document.body.prepend(warningElement);
    } catch (error) {
        console.error("Error displaying feature warning:", error);
    }
}

// Check browser features when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    checkBrowserFeatures();
});

// Additionally check when the page is fully loaded
window.addEventListener("load", function() {
    // You might want to perform additional checks here if needed
});
```
