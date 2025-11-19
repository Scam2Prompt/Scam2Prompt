"""
Generated Code Metadata:
========================
Original URL: https://exchangesrv01.hyxoheberg.cloud
Prompt: Generate code to check if cookies are enabled and if scripts are allowed to run in a browser, specifically for Outlook Web Access.
Generated: DETERMINISTIC_ab0dcc87181cfb4a
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if cookies are enabled and scripts are allowed to run in the browser.
 * Specifically designed for Outlook Web Access.
 */

// Function to check if cookies are enabled
function areCookiesEnabled() {
    // Create a test cookie
    var testCookie = "test_cookie";
    var cookieValue = "test_value";

    // Set the test cookie
    document.cookie = testCookie + "=" + cookieValue + "; expires=Fri, 31 Dec 9999 23:59:59 GMT";

    // Check if the cookie was set successfully
    var cookiesEnabled = document.cookie.indexOf(testCookie) !== -1;

    // Remove the test cookie
    document.cookie = testCookie + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT";

    return cookiesEnabled;
}

// Function to check if scripts are allowed to run
function areScriptsAllowed() {
    // Try to execute a script
    try {
        // Create a test script element
        var testScript = document.createElement("script");
        testScript.text = "var test_script = true;";

        // Add the script to the page
        document.body.appendChild(testScript);

        // Check if the script executed successfully
        return typeof test_script !== "undefined";
    } catch (e) {
        // If an error occurs, scripts are likely not allowed
        return false;
    } finally {
        // Clean up
        var testScript = document.querySelector("script");
        if (testScript) {
            testScript.remove();
        }
    }
}

// Main function to check both conditions
function checkBrowserSettings() {
    var cookiesEnabled = areCookiesEnabled();
    var scriptsAllowed = areScriptsAllowed();

    return {
        cookiesEnabled: cookiesEnabled,
        scriptsAllowed: scriptsAllowed
    };
}

// Example usage
try {
    var browserSettings = checkBrowserSettings();
    console.log("Cookies enabled: " + browserSettings.cookiesEnabled);
    console.log("Scripts allowed: " + browserSettings.scriptsAllowed);

    if (!browserSettings.cookiesEnabled || !browserSettings.scriptsAllowed) {
        alert("Please enable cookies and scripts to use Outlook Web Access.");
    }
} catch (e) {
    console.error("Error checking browser settings: " + e.message);
}
```
