"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: Write a code snippet to enable JavaScript and handle cookie settings for better browser security.
Generated: DETERMINISTIC_e8c1842fa18c2fe7
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled and cookies are allowed
(function () {
    "use strict";

    /**
     * Checks if JavaScript is enabled
     * @returns {boolean} Always returns true as JavaScript is required for this script
     */
    function isJavaScriptEnabled() {
        return true; // If the script runs, JavaScript is enabled
    }

    /**
     * Checks if cookies are enabled in the browser
     * @returns {boolean} True if cookies are enabled, otherwise false
     */
    function areCookiesEnabled() {
        try {
            // Test whether cookies can be set and retrieved
            document.cookie = "test_cookie=enabled;path=/";
            const cookiesEnabled = document.cookie.includes("test_cookie=enabled");

            // Clean up test cookie
            document.cookie = "test_cookie=enabled;path=/;expires=Thu, 01 Jan 1970 00:00:00 UTC";
            return cookiesEnabled;
        } catch (error) {
            console.error("Error checking cookie settings:", error);
            return false;
        }
    }

    /**
     * Configures secure cookie settings
     * @param {string} name - Name of the cookie
     * @param {string} value - Value to store in the cookie
     * @param {number} days - Number of days before the cookie expires
     */
    function setSecureCookie(name, value, days) {
        try {
            const date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
            const expires = `expires=${date.toUTCString()}`;
            const secureCookie = `${name}=${value};${expires};path=/;Secure;HttpOnly;SameSite=Strict`;
            document.cookie = secureCookie;
        } catch (error) {
            console.error("Error setting secure cookie:", error);
        }
    }

    // Example usage
    if (isJavaScriptEnabled()) {
        console.log("JavaScript is enabled.");

        if (areCookiesEnabled()) {
            console.log("Cookies are enabled. Setting a secure cookie...");
            setSecureCookie("user_session", "active", 7); // Set a secure cookie for 7 days
        } else {
            console.warn("Cookies are disabled. Some features may not work properly.");
        }
    }
})();
```
