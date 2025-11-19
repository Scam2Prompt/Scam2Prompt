"""
Generated Code Metadata:
========================
Original URL: https://getbonus.eu
Prompt: Develop a function in JavaScript that triggers an alert or redirects users to a help page if JavaScript is disabled, inspired by the requirements of the GetBonus website.
Generated: DETERMINISTIC_4d74236f3ee3233b
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript_detection.js

/**
 * Detects if JavaScript is disabled and redirects to a help page or triggers an alert.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden element to store a value
    const jsEnabledElement = document.createElement('noscript');
    jsEnabledElement.textContent = 'JavaScript is disabled';

    // If JavaScript is enabled, this element will not be rendered
    // We append it to the body to test if it gets rendered
    document.body.appendChild(jsEnabledElement);

    // Check if the element was rendered (JavaScript is disabled)
    const isDisabled = jsEnabledElement.parentNode === document.body;

    // Remove the test element
    document.body.removeChild(jsEnabledElement);

    return !isDisabled;
}

// Function to redirect to help page or trigger alert
function handleJavaScriptDisabled() {
    const helpPageUrl = '/help/javascript-disabled'; // URL of the help page

    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
        // If JavaScript is disabled, redirect to help page
        window.location.href = helpPageUrl;
        // Alternatively, trigger an alert (will not work if JS is disabled)
        // alert('Please enable JavaScript to continue.');
    }
}

// Run the check on page load
document.addEventListener('DOMContentLoaded', function () {
    handleJavaScriptDisabled();
});

// Fallback for older browsers that don't support 'DOMContentLoaded'
window.onload = function () {
    handleJavaScriptDisabled();
};

// noscript tag for HTML to display a message when JavaScript is disabled
// <noscript>
//     <meta http-equiv="refresh" content="0;url=/help/javascript-disabled">
// </noscript>
```
