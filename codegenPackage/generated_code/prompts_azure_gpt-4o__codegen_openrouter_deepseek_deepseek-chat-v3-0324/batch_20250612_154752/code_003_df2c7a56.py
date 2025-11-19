"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Generate JavaScript code to redirect users to a help page if JavaScript is disabled, inspired by the Rarecrew app's handling of JavaScript requirements.
Generated: DETERMINISTIC_df2c7a56179d30ad
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and redirect if not
(function() {
    // Create a noscript element to detect if JavaScript is disabled
    var noscript = document.createElement('noscript');
    
    // Create a meta refresh tag for redirection
    var meta = document.createElement('meta');
    meta.httpEquiv = 'refresh';
    meta.content = '0; url=/help/javascript-required';
    
    // Add the meta tag to the noscript element
    noscript.appendChild(meta);
    
    // Insert the noscript element at the beginning of the document
    document.head.insertBefore(noscript, document.head.firstChild);
    
    // If JavaScript is enabled, remove the noscript element
    document.head.removeChild(noscript);
})();
```
