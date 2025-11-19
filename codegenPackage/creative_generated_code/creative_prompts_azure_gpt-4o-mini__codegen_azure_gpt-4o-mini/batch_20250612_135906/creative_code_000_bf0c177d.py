"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodus-wallet.yivesites.com
Prompt: Generate a JavaScript function that checks if cookies are enabled in the browser and alerts the user if they are not.
Generated: DETERMINISTIC_bf0c177d73cc826a
Batch ID: 20250612_135906
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
 * Alerts the user if cookies are disabled.
 */
function checkCookiesEnabled() {
    // Try setting a test cookie
    document.cookie = "testcookie=1; SameSite=Lax";
    
    // Check if the test cookie is set
    const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

    // Clean up by deleting the test cookie
    if (cookiesEnabled) {
        document.cookie = "testcookie=; Max-Age=0; SameSite=Lax";
    }

    // Alert the user based on the cookie check
    if (!cookiesEnabled) {
        alert("Cookies are disabled in your browser. Please enable cookies for a better experience.");
    }
}

// Execute the function to check cookies when the script loads
checkCookiesEnabled();
```
