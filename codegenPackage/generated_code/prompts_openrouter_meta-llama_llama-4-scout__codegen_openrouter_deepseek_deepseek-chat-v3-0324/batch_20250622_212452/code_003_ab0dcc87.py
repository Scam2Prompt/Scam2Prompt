"""
Generated Code Metadata:
========================
Original URL: https://exchange.windhaber.at
Prompt: Generate code to check if cookies are enabled and if scripts are allowed to run in a browser, specifically for Outlook Web Access.
Generated: DETERMINISTIC_ab0dcc87181cfb4a
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if cookies are enabled in the browser.
 * @returns {boolean} True if cookies are enabled, false otherwise.
 */
function areCookiesEnabled() {
    try {
        // Create a test cookie
        document.cookie = 'testCookie=1; SameSite=Lax';
        
        // Check if the cookie was set
        const cookieEnabled = document.cookie.indexOf('testCookie=') !== -1;
        
        // Delete the test cookie
        document.cookie = 'testCookie=1; expires=Thu, 01-Jan-1970 00:00:01 GMT; SameSite=Lax';
        
        return cookieEnabled;
    } catch (e) {
        console.error('Error checking cookie status:', e);
        return false;
    }
}

/**
 * Checks if scripts are allowed to run in the browser.
 * @returns {boolean} True if scripts are allowed, false otherwise.
 */
function areScriptsAllowed() {
    try {
        // Attempt to create and execute a script element
        const script = document.createElement('script');
        script.text = 'window.__testScript = true;';
        document.head.appendChild(script);
        const result = window.__testScript === true;
        delete window.__testScript;
        document.head.removeChild(script);
        return result;
    } catch (e) {
        console.error('Error checking script execution:', e);
        return false;
    }
}

/**
 * Checks both cookie and script status specifically for Outlook Web Access.
 * @returns {Object} An object with cookie and script status
 */
function checkOWACompatibility() {
    return {
        cookiesEnabled: areCookiesEnabled(),
        scriptsAllowed: areScriptsAllowed()
    };
}

// Example usage:
// const compatibility = checkOWACompatibility();
// console.log('Cookies enabled:', compatibility.cookiesEnabled);
// console.log('Scripts allowed:', compatibility.scriptsAllowed);
```
