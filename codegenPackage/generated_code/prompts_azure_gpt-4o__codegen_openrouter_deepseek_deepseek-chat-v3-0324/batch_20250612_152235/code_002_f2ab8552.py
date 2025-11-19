"""
Generated Code Metadata:
========================
Original URL: https://shibonkgo.web.app
Prompt: Create a JavaScript function that displays an error message if JavaScript is disabled, similar to the behavior of the Shibonk Gang web app.
Generated: DETERMINISTIC_f2ab85520672376d
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays an error message if JavaScript is disabled in the browser.
 * The message is hidden by default and shown only when JS is disabled.
 */
(function() {
    // Create the error message element
    const errorMessage = document.createElement('div');
    errorMessage.id = 'js-disabled-error';
    errorMessage.style.display = 'none';
    errorMessage.style.position = 'fixed';
    errorMessage.style.top = '0';
    errorMessage.style.left = '0';
    errorMessage.style.width = '100%';
    errorMessage.style.padding = '1rem';
    errorMessage.style.backgroundColor = '#ff4444';
    errorMessage.style.color = 'white';
    errorMessage.style.textAlign = 'center';
    errorMessage.style.zIndex = '9999';
    errorMessage.innerHTML = `
        <strong>JavaScript is disabled!</strong>
        <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
    `;

    // Add the error message to the body
    document.body.insertBefore(errorMessage, document.body.firstChild);

    // Hide the error message if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function() {
        errorMessage.style.display = 'none';
    });

    // Fallback: If this script runs, JS is enabled, so hide the message
    errorMessage.style.display = 'none';

    // For noscript fallback
    const noscriptStyle = document.createElement('style');
    noscriptStyle.innerHTML = `
        noscript #js-disabled-error {
            display: block !important;
        }
    `;
    document.head.appendChild(noscriptStyle);
})();
```
