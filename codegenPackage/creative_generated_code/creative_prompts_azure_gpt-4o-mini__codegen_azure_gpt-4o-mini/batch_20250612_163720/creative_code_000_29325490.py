"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo777-axe.pages.dev
Prompt: How can I enable JavaScript and cookies in my browser for optimal website functionality?
Generated: DETERMINISTIC_2932549030bf6371
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Utility function to check if JavaScript is enabled and cookies are allowed.
 * This function will display alerts to the user based on the results.
 */
function checkBrowserSettings() {
    // Check if JavaScript is enabled
    if (typeof window === "undefined") {
        alert("JavaScript is not enabled in your browser. Please enable it for optimal website functionality.");
    } else {
        alert("JavaScript is enabled.");
    }

    // Check if cookies are enabled
    document.cookie = "testcookie=1"; // Try to set a test cookie
    const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1;

    if (cookiesEnabled) {
        alert("Cookies are enabled.");
        // Clean up by deleting the test cookie
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
    } else {
        alert("Cookies are not enabled. Please enable cookies for optimal website functionality.");
    }
}

// Execute the function to check browser settings
try {
    checkBrowserSettings();
} catch (error) {
    // Log error for debugging purposes
    console.error("An error occurred while checking browser settings:", error);
    alert("An unexpected error occurred. Please try again later.");
}
```
