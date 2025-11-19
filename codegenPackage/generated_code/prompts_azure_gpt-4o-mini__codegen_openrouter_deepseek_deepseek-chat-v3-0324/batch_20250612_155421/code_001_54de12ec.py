"""
Generated Code Metadata:
========================
Original URL: https://exodusn.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and displays a message if it is not, similar to the warning on ExodusN.
Generated: DETERMINISTIC_54de12eca1c151bf
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and display a warning if it's not
(function() {
    'use strict';

    // Create a noscript warning element
    var noscriptWarning = document.createElement('div');
    noscriptWarning.id = 'noscript-warning';
    noscriptWarning.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; ' +
        'background-color: #f8d7da; color: #721c24; padding: 10px; text-align: center; ' +
        'z-index: 9999; border-bottom: 1px solid #f5c6cb; font-family: Arial, sans-serif;';

    // Set the warning message
    noscriptWarning.innerHTML = '<strong>Warning:</strong> JavaScript is disabled in your browser. ' +
        'Some features may not work properly.';

    // Check if the browser supports JavaScript
    try {
        // Attempt to create and append an element
        var testElement = document.createElement('div');
        document.body.appendChild(testElement);
        document.body.removeChild(testElement);
    } catch (e) {
        // If an error occurs, JavaScript is likely disabled
        document.body.insertBefore(noscriptWarning, document.body.firstChild);
    }
})();
```
