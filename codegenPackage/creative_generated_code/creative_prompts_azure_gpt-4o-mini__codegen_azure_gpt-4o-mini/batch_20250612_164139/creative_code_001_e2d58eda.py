"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.juta-soft.hu
Prompt: Write a script that checks if cookies are enabled in a browser before attempting to sign in to Outlook.
Generated: DETERMINISTIC_e2d58eda0e9bdfb2
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// checkCookies.js

/**
 * Checks if cookies are enabled in the browser.
 * This function attempts to set a test cookie and then
 * checks if it can be retrieved. If both operations succeed,
 * it concludes that cookies are enabled.
 * 
 * @returns {boolean} - Returns true if cookies are enabled, false otherwise.
 */
function areCookiesEnabled() {
    // Create a test cookie
    document.cookie = "testcookie=1; SameSite=Strict; path=/";
    // Check if the cookie was successfully set
    const cookiesEnabled = document.cookie.includes("testcookie");

    // Clean up test cookie
    if (cookiesEnabled) {
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
    }

    return cookiesEnabled;
}

/**
 * Attempts to sign in to Outlook if cookies are enabled.
 * Displays an alert if cookies are not enabled.
 */
function signInToOutlook() {
    try {
        // Check if cookies are enabled before proceeding
        if (areCookiesEnabled()) {
            // Proceed with the sign-in process (placeholder for actual sign-in logic)
            console.log("Cookies are enabled. Proceeding to sign in to Outlook...");
            // TODO: Add actual sign-in logic here
        } else {
            // Notify the user that cookies must be enabled
            alert("Please enable cookies in your browser settings to sign in to Outlook.");
        }
    } catch (error) {
        // Log the error and notify the user
        console.error("An error occurred while checking cookies or signing in:", error);
        alert("An unexpected error occurred. Please try again later.");
    }
}

// Execute the sign-in check when the script is loaded
signInToOutlook();
```
