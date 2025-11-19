"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds-chy.pages.dev
Prompt: What are the steps to troubleshoot JavaScript and cookie issues on a webpage?
Generated: DETERMINISTIC_c950caebe926311e
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Troubleshooting JavaScript and cookie issues on a webpage.
 * This script provides utility functions to debug JavaScript errors, 
 * check cookie settings, and verify browser compatibility.
 */

/**
 * Function to check for JavaScript errors in the console.
 * Captures errors and logs them for debugging purposes.
 */
window.onerror = function (message, source, lineno, colno, error) {
    console.error("JavaScript Error detected:");
    console.error(`Message: ${message}`);
    console.error(`Source: ${source}`);
    console.error(`Line: ${lineno}, Column: ${colno}`);
    console.error(`Error Object:`, error);
    alert("A JavaScript error occurred. Please check the console for details.");
};

/**
 * Function to verify that cookies are enabled in the browser.
 * Logs the status and alerts the user if cookies are disabled.
 */
function checkCookiesEnabled() {
    if (navigator.cookieEnabled) {
        console.log("Cookies are enabled.");
    } else {
        console.error("Cookies are disabled in this browser.");
        alert("Cookies are disabled. Please enable cookies for this site to work correctly.");
    }
}

/**
 * Function to debug existing cookies on the webpage.
 * Logs all cookies and their values to the console.
 */
function listCookies() {
    if (document.cookie) {
        console.log("Listing all cookies:");
        const cookies = document.cookie.split(";").map(cookie => cookie.trim());
        cookies.forEach((cookie, index) => {
            console.log(`Cookie ${index + 1}: ${cookie}`);
        });
    } else {
        console.log("No cookies found on this webpage.");
    }
}

/**
 * Function to test cookie creation and retrieval.
 * Verifies that the browser allows cookie operations.
 */
function testCookieFunctionality() {
    try {
        const testCookieName = "test_cookie";
        const testCookieValue = "test_value";
        document.cookie = `${testCookieName}=${testCookieValue}; path=/`;

        if (document.cookie.includes(`${testCookieName}=${testCookieValue}`)) {
            console.log("Cookie functionality works correctly.");
        } else {
            throw new Error("Cookie creation failed.");
        }

        // Clean up test cookie
        document.cookie = `${testCookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    } catch (error) {
        console.error("Error during cookie functionality test:", error);
        alert("There was an issue testing cookie functionality. Please check the console for details.");
    }
}

/**
 * Function to check browser compatibility for JavaScript and cookies.
 * Provides information about the browser and its capabilities.
 */
function checkBrowserCompatibility() {
    console.log("Browser Information:");
    console.log(`User Agent: ${navigator.userAgent}`);
    console.log(`JavaScript Enabled: ${typeof window !== "undefined" && typeof document !== "undefined"}`);
    console.log(`Cookies Enabled: ${navigator.cookieEnabled}`);
}

// Run all debugging functions to troubleshoot issues
checkCookiesEnabled();
listCookies();
testCookieFunctionality();
checkBrowserCompatibility();
```
