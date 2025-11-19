"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a user's browser and display a message prompting them to enable it if it is disabled.
Generated: DETERMINISTIC_b2ec5b13b0870605
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the user's browser.
 * If disabled, displays a message prompting the user to enable it.
 */
(function() {
    // Create a noscript element to detect if JavaScript is disabled
    const noscript = document.createElement('noscript');
    const messageDiv = document.createElement('div');
    
    // Style the message for better visibility
    messageDiv.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 20px;
        background-color: #ffeb3b;
        color: #000;
        text-align: center;
        z-index: 9999;
        font-family: Arial, sans-serif;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    `;
    
    messageDiv.textContent = 'JavaScript is disabled in your browser. Please enable JavaScript for full functionality.';
    
    // Add the message to the noscript element
    noscript.appendChild(messageDiv);
    
    // Insert the noscript element at the beginning of the body
    document.body.insertBefore(noscript, document.body.firstChild);
    
    // Remove the noscript element if JavaScript is enabled
    setTimeout(function() {
        if (document.body.contains(noscript)) {
            document.body.removeChild(noscript);
        }
    }, 0);
})();
```
