"""
Generated Code Metadata:
========================
Original URL: https://sui.42web.io
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled in a browser and provides a fallback message if it's not.
Generated: DETERMINISTIC_e2ff37a661753aa7
Batch ID: 20250622_212843
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
 * If not, displays a fallback message to the user.
 */
(function() {
    // Create a noscript element to check if JavaScript is enabled
    var noscript = document.createElement('noscript');
    noscript.innerHTML = '<div class="js-disabled-warning" style="padding: 1rem; background-color: #ffebee; color: #c62828; border: 1px solid #ef9a9a; margin: 1rem; border-radius: 4px;">JavaScript is disabled in your browser. Some features may not work properly.</div>';
    
    // Insert the noscript element at the beginning of the body
    document.body.insertBefore(noscript, document.body.firstChild);
    
    // Remove the noscript element if JavaScript is enabled
    setTimeout(function() {
        if (noscript.parentNode) {
            noscript.parentNode.removeChild(noscript);
        }
    }, 0);
})();
```
