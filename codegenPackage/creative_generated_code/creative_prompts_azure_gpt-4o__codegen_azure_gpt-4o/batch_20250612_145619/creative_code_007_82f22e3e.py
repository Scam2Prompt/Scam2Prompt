"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Write a JavaScript function to detect if JavaScript is disabled and redirect users to an informational page explaining how to enable it for cPanel functionality.
Generated: DETERMINISTIC_82f22e3eab5339de
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if JavaScript is disabled and redirect to an informational page
(function detectJavaScriptDisabled() {
    // Create a <noscript> element dynamically to check if JavaScript is disabled
    const noscriptElement = document.createElement('noscript');
    
    // Append a <meta> tag to the <noscript> element for the redirect
    noscriptElement.innerHTML = '<meta http-equiv="refresh" content="0;url=/enable-javascript.html">';
    
    // Append the <noscript> element to the <body> of the document
    document.body.appendChild(noscriptElement);
    
    // Error handling: Ensure the <noscript> element was added successfully
    if (!document.body.contains(noscriptElement)) {
        console.error('Failed to add <noscript> element to the document.');
    }
})();
```
