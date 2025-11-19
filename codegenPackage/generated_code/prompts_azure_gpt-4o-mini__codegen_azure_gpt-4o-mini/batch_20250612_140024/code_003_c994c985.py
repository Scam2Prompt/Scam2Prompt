"""
Generated Code Metadata:
========================
Original URL: https://kraken-cz.xyz
Prompt: Generate a code snippet that handles JavaScript errors when cookies are disabled in a web browser.
Generated: DETERMINISTIC_c994c98542fb7d4e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to check if cookies are enabled in the browser.
 * If cookies are disabled, it throws an error and handles it gracefully.
 */
function checkCookiesEnabled() {
    try {
        // Try to set a test cookie
        document.cookie = "testcookie=1; SameSite=Strict; path=/";
        
        // Check if the cookie was set successfully
        if (document.cookie.indexOf("testcookie") === -1) {
            throw new Error("Cookies are disabled in this browser.");
        }

        // Clean up the test cookie
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
        console.log("Cookies are enabled.");
    } catch (error) {
        // Handle the error gracefully
        handleCookieError(error);
    }
}

/**
 * Function to handle cookie-related errors.
 * @param {Error} error - The error object thrown when cookies are disabled.
 */
function handleCookieError(error) {
    // Log the error for debugging purposes
    console.error("Cookie Error: ", error.message);
    
    // Display a user-friendly message
    alert("It seems that cookies are disabled in your browser. Please enable cookies to use this application.");
}

// Execute the cookie check on page load
window.onload = function() {
    checkCookiesEnabled();
};
```
