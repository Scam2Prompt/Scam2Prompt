"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Write JavaScript code to check if browser cookies are enabled and display a message prompting the user to enable cookies if they are disabled.
Generated: DETERMINISTIC_47332f79afed33ba
Batch ID: 20250612_145526
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
        // Try to set a test cookie
        document.cookie = 'testCookie=1; SameSite=Lax';
        
        // Check if the cookie was set
        const cookiesEnabled = document.cookie.indexOf('testCookie=') !== -1;
        
        // Clean up by removing the test cookie
        document.cookie = 'testCookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; SameSite=Lax';
        
        return cookiesEnabled;
    } catch (e) {
        console.error('Error checking cookie status:', e);
        return false;
    }
}

/**
 * Displays a message prompting the user to enable cookies.
 */
function showCookieMessage() {
    const message = document.createElement('div');
    message.style.position = 'fixed';
    message.style.bottom = '0';
    message.style.left = '0';
    message.style.right = '0';
    message.style.backgroundColor = '#ffcccc';
    message.style.padding = '10px';
    message.style.textAlign = 'center';
    message.style.zIndex = '1000';
    message.style.borderTop = '1px solid #ff9999';
    
    message.innerHTML = `
        <p>Cookies are disabled in your browser. Please enable cookies to use this website properly.</p>
        <button onclick="this.parentNode.style.display='none'" 
                style="padding: 5px 10px; background: #ff9999; border: none; border-radius: 3px; cursor: pointer;">
            Dismiss
        </button>
    `;
    
    document.body.appendChild(message);
}

// Check cookies on page load
document.addEventListener('DOMContentLoaded', function() {
    if (!areCookiesEnabled()) {
        showCookieMessage();
    }
});
```
