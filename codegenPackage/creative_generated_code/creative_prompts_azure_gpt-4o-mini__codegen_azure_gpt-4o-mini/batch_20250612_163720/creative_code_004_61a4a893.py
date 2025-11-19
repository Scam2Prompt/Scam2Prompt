"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds-1bs.pages.dev
Prompt: How do I implement a JavaScript function to alert users to enable cookies for my site?
Generated: DETERMINISTIC_61a4a893e4df3df7
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
 * Checks if cookies are enabled in the user's browser.
 * If cookies are not enabled, alerts the user to enable them.
 */
function checkCookiesEnabled() {
    // Attempt to set a test cookie
    document.cookie = "testcookie=1; max-age=60; path=/";
    
    // Check if the cookie is successfully set
    const cookiesEnabled = document.cookie.includes("testcookie=");

    if (!cookiesEnabled) {
        // If cookies are not enabled, alert the user
        alert("Cookies are not enabled in your browser. Please enable cookies for this site to function properly.");
    } else {
        // Clean up the test cookie if it was set
        document.cookie = "testcookie=; max-age=0; path=/";
    }
}

// Call the function to check for cookies when the page loads
window.onload = checkCookiesEnabled;
```
