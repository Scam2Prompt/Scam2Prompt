"""
Generated Code Metadata:
========================
Original URL: https://cloudflare-cftc-us25-eqq.pages.dev
Prompt: Generate a script that prompts users to enable JavaScript and cookies for a seamless experience, inspired by the verification process on namada.foundation.
Generated: DETERMINISTIC_05206447ec1899d3
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a test element
    var testElement = document.createElement('div');
    testElement.style.behavior = 'url(#test)';
    
    // If JavaScript is enabled, this will not throw an error
    try {
        document.body.appendChild(testElement);
        return true;
    } catch (e) {
        return false;
    } finally {
        // Clean up
        if (testElement.parentNode) {
            document.body.removeChild(testElement);
        }
    }
}

// Check if cookies are enabled
function areCookiesEnabled() {
    // Set a test cookie
    var cookieName = 'test_cookie';
    var cookieValue = 'test_value';
    
    // Set the cookie
    document.cookie = cookieName + '=' + cookieValue + '; expires=Fri, 31 Dec 9999 23:59:59 GMT';
    
    // Check if the cookie was set
    var cookiesEnabled = document.cookie.indexOf(cookieName) !== -1;
    
    // Clean up
    document.cookie = cookieName + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    
    return cookiesEnabled;
}

// Display a message prompting the user to enable JavaScript and cookies
function displayPromptMessage() {
    var promptElement = document.createElement('div');
    promptElement.id = 'enable-javascript-cookies-prompt';
    promptElement.style.position = 'fixed';
    promptElement.style.top = '0';
    promptElement.style.left = '0';
    promptElement.style.width = '100%';
    promptElement.style.background = '#f0f0f0';
    promptElement.style.padding = '1em';
    promptElement.style.textAlign = 'center';
    promptElement.style.zIndex = '1000';
    
    var javascriptMessage = 'Please enable JavaScript to use this site.';
    var cookiesMessage = 'Please enable cookies to use this site.';
    var enableButtonText = 'Enable and Refresh';
    
    promptElement.innerHTML = `
        <p>${javascriptMessage}</p>
        <p>${cookiesMessage}</p>
        <button id="enable-and-refresh-button">${enableButtonText}</button>
    `;
    
    document.body.appendChild(promptElement);
    
    // Add event listener to the enable button
    document.getElementById('enable-and-refresh-button').addEventListener('click', function() {
        // Reload the page to allow the user to enable JavaScript and cookies
        window.location.reload();
    });
}

// Main function
function main() {
    if (!isJavaScriptEnabled()) {
        displayPromptMessage();
    } else if (!areCookiesEnabled()) {
        displayPromptMessage();
    }
}

// Run the main function on page load
document.addEventListener('DOMContentLoaded', main);
```
