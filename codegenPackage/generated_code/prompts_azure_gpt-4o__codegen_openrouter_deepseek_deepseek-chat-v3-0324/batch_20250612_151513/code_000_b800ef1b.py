"""
Generated Code Metadata:
========================
Original URL: https://ethff.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message if it is disabled, similar to the behavior described on the ETH 2.0 website.
Generated: DETERMINISTIC_b800ef1bc402efa4
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and display a message if it's disabled
(function() {
    // Create a noscript element to display the message
    var noscriptElement = document.createElement('noscript');
    noscriptElement.innerHTML = '<div style="position: fixed; top: 0; left: 0; right: 0; padding: 1em; background: #f8d7da; color: #721c24; text-align: center; z-index: 9999;">JavaScript is disabled in your browser. Some functionality may be limited.</div>';
    
    // Try to insert the noscript element at the beginning of the body
    try {
        document.body.insertBefore(noscriptElement, document.body.firstChild);
    } catch (e) {
        // Fallback if document.body isn't available yet
        document.addEventListener('DOMContentLoaded', function() {
            document.body.insertBefore(noscriptElement, document.body.firstChild);
        });
    }
})();
```
