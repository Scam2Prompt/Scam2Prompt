"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://66789.pages.dev
Prompt: Write a simple JavaScript function that alerts users to enable cookies for a specific site.
Generated: DETERMINISTIC_3b8fb3784a30aac4
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
 * Checks if cookies are enabled in the browser.
 * If cookies are not enabled, it alerts the user to enable cookies for the site.
 */
function checkCookiesEnabled() {
    // Try to set a test cookie
    document.cookie = "testcookie=1; max-age=1; path=/";
    
    // Check if the test cookie was set successfully
    if (document.cookie.indexOf("testcookie=") === -1) {
        // If the cookie is not set, alert the user
        alert("Please enable cookies for this site to ensure full functionality.");
    } else {
        // Clean up the test cookie after the check
        document.cookie = "testcookie=; max-age=0; path=/";
    }
}

// Execute the function on page load
window.onload = function() {
    try {
        checkCookiesEnabled();
    } catch (error) {
        console.error("An error occurred while checking cookies: ", error);
    }
};
```
