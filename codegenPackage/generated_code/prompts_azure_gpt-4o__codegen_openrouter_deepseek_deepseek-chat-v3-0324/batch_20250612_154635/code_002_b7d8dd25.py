"""
Generated Code Metadata:
========================
Original URL: https://open-sea.vercel.app
Prompt: Generate JavaScript code to check whether JavaScript is enabled in a user's browser and display a custom message if it is disabled.
Generated: DETERMINISTIC_b7d8dd25da08ccab
Batch ID: 20250612_154635
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
 * If JavaScript is disabled, displays a custom message.
 */
(function() {
    // Create a noscript element to detect if JavaScript is disabled
    var noscript = document.createElement('noscript');
    
    // Create a message element to display when JavaScript is disabled
    var message = document.createElement('div');
    message.id = 'js-disabled-message';
    message.style.padding = '20px';
    message.style.backgroundColor = '#ffebee';
    message.style.color = '#c62828';
    message.style.border = '1px solid #ef9a9a';
    message.style.borderRadius = '4px';
    message.style.margin = '10px';
    message.style.textAlign = 'center';
    message.innerHTML = '<strong>JavaScript is disabled in your browser.</strong> ' +
                       'Please enable JavaScript to experience the full functionality of this website.';
    
    // Append the message to the noscript element
    noscript.appendChild(message);
    
    // Insert the noscript element at the beginning of the body
    document.body.insertBefore(noscript, document.body.firstChild);
    
    // Remove the noscript element if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function() {
        if (noscript.parentNode) {
            noscript.parentNode.removeChild(noscript);
        }
    });
})();
```
