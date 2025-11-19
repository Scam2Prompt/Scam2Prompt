"""
Generated Code Metadata:
========================
Original URL: https://cpanel.sophon.am
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_681a5bf1d2db80bc
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to detect if JavaScript is disabled and display a warning message
function detectJavascriptDisabled() {
    // Create a warning message element
    const warningMessage = document.createElement('div');
    warningMessage.id = 'js-disabled-warning';
    warningMessage.textContent = 'Warning: JavaScript is disabled. Please enable JavaScript to use this site.';
    warningMessage.style.position = 'fixed';
    warningMessage.style.top = '0';
    warningMessage.style.left = '0';
    warningMessage.style.width = '100%';
    warningMessage.style.background = '#FFC080';
    warningMessage.style.color = '#666';
    warningMessage.style.padding = '10px';
    warningMessage.style.textAlign = 'center';
    warningMessage.style.zIndex = '1000';

    // Check if JavaScript is enabled by trying to access localStorage
    try {
        // If localStorage is not available, JavaScript is disabled
        if (typeof Storage === 'undefined') {
            throw new Error('Storage is undefined');
        }
        localStorage.setItem('test', 'test');
        localStorage.removeItem('test');
    } catch (error) {
        // If an error occurs, JavaScript is disabled, so display the warning message
        document.body.appendChild(warningMessage);
        return;
    }

    // If JavaScript is enabled, check if the warning message is already displayed
    const existingWarning = document.getElementById('js-disabled-warning');
    if (existingWarning) {
        existingWarning.remove();
    }
}

// Run the detection function on page load
document.addEventListener('DOMContentLoaded', detectJavascriptDisabled);
```
