"""
Generated Code Metadata:
========================
Original URL: https://blur.si
Prompt: Create a JavaScript snippet that checks for JavaScript enablement and redirects users to a specific page if JavaScript is disabled, as seen on https://blur.si.
Generated: DETERMINISTIC_082c01483c66682b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and redirect if disabled
(function() {
    // Create a noscript element to detect if JavaScript is disabled
    var noscript = document.createElement('noscript');
    var redirectUrl = '/nojs.html'; // Change this to your desired redirect URL
    
    // Add a meta refresh tag inside noscript for immediate redirect
    noscript.innerHTML = '<meta http-equiv="refresh" content="0; url=' + redirectUrl + '">';
    
    // Append to head to trigger the check
    document.head.appendChild(noscript);
    
    // Remove the noscript element after appending (only happens if JS is enabled)
    document.head.removeChild(noscript);
})();
```
