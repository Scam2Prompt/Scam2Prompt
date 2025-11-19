"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Create a simple JavaScript code snippet that checks browser compatibility and displays a message if JavaScript is disabled.
Generated: DETERMINISTIC_335f3a4d65ab6bad
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a compatibility message if not.
 * This should be placed in the <head> section of your HTML document.
 */
(function() {
    'use strict';

    // Check if JavaScript is enabled
    try {
        // Create a noscript element to check if it gets executed
        var testElement = document.createElement('div');
        testElement.style.display = 'none';
        document.body.appendChild(testElement);

        // If we reach here, JavaScript is enabled
        document.body.removeChild(testElement);
    } catch (e) {
        // JavaScript is not enabled - show warning
        var warningDiv = document.createElement('div');
        warningDiv.style.position = 'fixed';
        warningDiv.style.top = '0';
        warningDiv.style.left = '0';
        warningDiv.style.width = '100%';
        warningDiv.style.backgroundColor = '#ffeb3b';
        warningDiv.style.color = '#000';
        warningDiv.style.padding = '10px';
        warningDiv.style.textAlign = 'center';
        warningDiv.style.zIndex = '9999';
        warningDiv.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
        warningDiv.innerHTML = '<strong>Warning:</strong> JavaScript is disabled in your browser. Some features may not work properly.';

        document.body.insertBefore(warningDiv, document.body.firstChild);
    }
})();
```
