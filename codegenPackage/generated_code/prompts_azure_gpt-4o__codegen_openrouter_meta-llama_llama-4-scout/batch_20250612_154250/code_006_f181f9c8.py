"""
Generated Code Metadata:
========================
Original URL: https://greendotinstallerportaluat.crm.com
Prompt: Create JavaScript code to display a warning message if JavaScript is disabled, as seen in the GreenDot Installer Portal.
Generated: DETERMINISTIC_f181f9c8ecc67e73
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled by attempting to set a test cookie
function checkJavascriptEnabled() {
    // Create a test cookie
    const testCookieName = 'javascriptEnabledTest';
    const testCookieValue = 'true';

    // Try to set the test cookie
    try {
        // Set the test cookie
        document.cookie = `${testCookieName}=${testCookieValue}; expires=Fri, 31 Dec 9999 23:59:59 GMT`;

        // Check if the test cookie was set successfully
        const cookies = document.cookie.split(';');
        let cookieEnabled = false;
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(`${testCookieName}=`)) {
                cookieEnabled = true;
                break;
            }
        }

        // If the test cookie was not set, display the warning message
        if (!cookieEnabled) {
            displayWarningMessage();
        }
    } catch (error) {
        // If an error occurs while trying to set the test cookie, display the warning message
        console.error('Error checking JavaScript enabled:', error);
        displayWarningMessage();
    } finally {
        // Clean up the test cookie
        document.cookie = `${testCookieName}=; expires=Thu, 01 Jan 1970 00:00:00 GMT`;
    }
}

// Display a warning message if JavaScript is disabled
function displayWarningMessage() {
    // Create the warning message element
    const warningMessageElement = document.createElement('div');
    warningMessageElement.className = 'javascript-disabled-warning';
    warningMessageElement.innerHTML = `
        <strong>Warning: JavaScript is disabled.</strong>
        <p>Please enable JavaScript in your browser settings to use this portal.</p>
    `;

    // Add the warning message to the page
    const bodyElement = document.body;
    bodyElement.insertBefore(warningMessageElement, bodyElement.firstChild);
}

// Run the check on page load
document.addEventListener('DOMContentLoaded', checkJavascriptEnabled);
```

```css
/* Add this CSS to your stylesheet to display the warning message */
/* You can adjust the styles as needed */
.javascript-disabled-warning {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ffc080;
    color: #666;
    padding: 1em;
    text-align: center;
    z-index: 1000;
}
```
