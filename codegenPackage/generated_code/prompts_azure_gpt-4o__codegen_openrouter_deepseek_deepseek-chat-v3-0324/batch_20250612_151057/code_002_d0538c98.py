"""
Generated Code Metadata:
========================
Original URL: https://swapfinderbq.github.io
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "avedex-m doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_d0538c98a7b701f2
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a message if it's not.
 * @function checkJavaScriptEnabled
 */
function checkJavaScriptEnabled() {
    try {
        // Create a noscript element to check if JavaScript is enabled
        const noscript = document.createElement('noscript');
        const message = document.createElement('div');
        
        // Style the message for better visibility
        message.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1em;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
            font-family: Arial, sans-serif;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        `;
        
        message.textContent = 'avedex-m doesn\'t work properly without JavaScript enabled.';
        
        // Add the message to the noscript element
        noscript.appendChild(message);
        
        // Append the noscript element to the body
        document.body.appendChild(noscript);
        
        // If JavaScript is enabled, remove the noscript element immediately
        setTimeout(() => {
            if (document.body.contains(noscript)) {
                document.body.removeChild(noscript);
            }
        }, 0);
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
    }
}

// Call the function when the DOM is fully loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
} else {
    checkJavaScriptEnabled();
}
```
