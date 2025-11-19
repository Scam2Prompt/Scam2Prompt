"""
Generated Code Metadata:
========================
Original URL: https://foxylinea.presale.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and prompts the user to enable it if not.
Generated: DETERMINISTIC_286390ba9bb8104d
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser.
 * If not, prompts the user to enable it.
 */
// Check if JavaScript is enabled by trying to set a cookie
function isJavaScriptEnabled() {
    try {
        // Try to set a test cookie
        document.cookie = 'javascriptEnabled=1; expires=Fri, 31 Dec 9999 23:59:59 GMT';
        
        // Check if the cookie was set successfully
        return document.cookie.indexOf('javascriptEnabled=1') !== -1;
    } catch (error) {
        // If an error occurs, assume JavaScript is disabled
        return false;
    }
}

/**
 * Prompts the user to enable JavaScript.
 */
function promptEnableJavaScript() {
    // Create a div element to display the message
    const messageDiv = document.createElement('div');
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = '#ff9800';
    messageDiv.style.color = '#fff';
    messageDiv.style.padding = '1em';
    messageDiv.style.textAlign = 'center';
    messageDiv.style.zIndex = '1000';

    // Set the message text
    messageDiv.innerText = 'JavaScript is disabled. Please enable it to use this site.';

    // Add the div to the page
    document.body.appendChild(messageDiv);
}

// Check if JavaScript is enabled
if (!isJavaScriptEnabled()) {
    // If not, prompt the user to enable it
    promptEnableJavaScript();
}
```
