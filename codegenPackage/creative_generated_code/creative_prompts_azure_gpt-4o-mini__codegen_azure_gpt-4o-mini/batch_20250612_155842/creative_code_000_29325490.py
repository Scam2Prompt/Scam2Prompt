"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7473441704.pages.dev
Prompt: How can I enable JavaScript and cookies in my browser for optimal website functionality?
Generated: DETERMINISTIC_2932549030bf6371
Batch ID: 20250612_155842
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
 * This function checks the current state of the user's browser settings.
 */
function checkBrowserSettings() {
    const isJavaScriptEnabled = (function() {
        // Create a dummy element and try to set a property
        try {
            return (function() {
                // This will run if JavaScript is enabled
                return true;
            })();
        } catch (e) {
            return false; // If an error occurs, JS is likely disabled
        }
    })();

    // Check if cookies are enabled
    const areCookiesEnabled = (() => {
        // Try to set and read a cookie
        document.cookie = "testcookie=1; SameSite=Lax"; // Set a test cookie
        const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1; // Check if we can read the test cookie
        document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT"; // Clean up test cookie
        return cookiesEnabled;
    })();

    // Return the results in a structured format
    return {
        isJavaScriptEnabled: isJavaScriptEnabled,
        areCookiesEnabled: areCookiesEnabled
    };
}

/**
 * Function to display the status of JavaScript and cookies to the user.
 */
function displayBrowserSettingsStatus() {
    const settingsStatus = checkBrowserSettings();

    // Display the results
    if (settingsStatus.isJavaScriptEnabled && settingsStatus.areCookiesEnabled) {
        console.log("JavaScript is enabled and cookies are allowed. You can enjoy optimal website functionality.");
    } else {
        console.warn("JavaScript might be disabled or cookies are not allowed. Please enable them for optimal website functionality.");
        if (!settingsStatus.isJavaScriptEnabled) {
            console.warn("To enable JavaScript: Check your browser settings to turn on JavaScript.");
        }
        if (!settingsStatus.areCookiesEnabled) {
            console.warn("To enable cookies: Check your browser settings and allow cookies.");
        }
    }
}

// Run the function to check browser settings and display the result
displayBrowserSettingsStatus();
```
