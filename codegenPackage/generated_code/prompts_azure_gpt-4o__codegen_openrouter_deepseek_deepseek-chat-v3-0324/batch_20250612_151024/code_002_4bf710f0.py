"""
Generated Code Metadata:
========================
Original URL: https://ham-drops.pages.dev
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as seen in "Hamster Kombat."
Generated: DETERMINISTIC_4bf710f012295a30
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects if JavaScript is disabled in the browser and displays a custom message.
 * This script should be placed in the <noscript> tag or run immediately in the <head>.
 */

(function() {
    // Check if JavaScript is enabled by attempting to modify the DOM
    try {
        // Create a test element
        var testElement = document.createElement('div');
        testElement.style.display = 'none';
        document.body.appendChild(testElement);
        
        // If we reach here, JavaScript is enabled
        document.body.removeChild(testElement);
    } catch (e) {
        // JavaScript is disabled - this block won't execute since the script wouldn't run
    }

    // Function to show the no-JS message
    function showNoJSMessage() {
        var message = document.createElement('div');
        message.id = 'no-js-message';
        message.style.position = 'fixed';
        message.style.top = '0';
        message.style.left = '0';
        message.style.width = '100%';
        message.style.padding = '20px';
        message.style.backgroundColor = '#ff0000';
        message.style.color = '#ffffff';
        message.style.textAlign = 'center';
        message.style.zIndex = '9999';
        message.innerHTML = 'JavaScript is disabled in your browser. Please enable JavaScript to play Hamster Kombat.';
        
        document.body.insertBefore(message, document.body.firstChild);
    }

    // The noscript tag alternative (this is the primary method)
    // This script should be accompanied by:
    // <noscript><style>#no-js-message { display: block !important; }</style></noscript>
    
    // Create the message element (hidden by default)
    var messageElement = document.createElement('div');
    messageElement.id = 'no-js-message';
    messageElement.style.display = 'none';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.padding = '20px';
    messageElement.style.backgroundColor = '#ff0000';
    messageElement.style.color = '#ffffff';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '9999';
    messageElement.innerHTML = 'JavaScript is disabled in your browser. Please enable JavaScript to play Hamster Kombat.';
    
    document.body.insertBefore(messageElement, document.body.firstChild);
})();
```
