"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.falai.it
Prompt: Can you provide a code snippet to check if cookies are enabled in a web application for Outlook access?
Generated: DETERMINISTIC_1028eff36390b3df
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if cookies are enabled in the user's browser.
 * This snippet can be used in a web application to determine cookie availability.
 */
function areCookiesEnabled() {
    try {
        // Attempt to set a test cookie
        document.cookie = "test_cookie=1; SameSite=Strict";

        // Check if the cookie was successfully set
        const isCookieSet = document.cookie.indexOf("test_cookie=1") !== -1;

        // Clean up: delete the test cookie
        document.cookie = "test_cookie=1; SameSite=Strict; expires=Thu, 01 Jan 1970 00:00:00 UTC";

        // Return the result
        return isCookieSet;
    } catch (error) {
        // Log error for debugging purposes
        console.error("Error while checking cookies:", error);

        // Return false if an error occurs
        return false;
    }
}

/**
 * Example usage: Check if cookies are enabled and display a message to the user.
 */
if (areCookiesEnabled()) {
    console.log("Cookies are enabled! Outlook access should work correctly.");
} else {
    console.log("Cookies are disabled! Please enable cookies for Outlook access.");
}
```
