"""
Generated Code Metadata:
========================
Original URL: https://full-mint-website-master.pages.dev
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message accordingly, as seen in the React app at https://full-mint-website-master.pages.dev.
Generated: DETERMINISTIC_ddff7da2e811d8c8
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a message accordingly.
 * This function should be called when the page loads.
 */
function checkJavaScriptEnabled() {
    try {
        // Create a noscript element to check if JavaScript is enabled
        const noscriptElement = document.createElement('noscript');
        const messageElement = document.createElement('div');
        
        // Style the message element
        messageElement.style.position = 'fixed';
        messageElement.style.top = '0';
        messageElement.style.left = '0';
        messageElement.style.width = '100%';
        messageElement.style.padding = '1rem';
        messageElement.style.backgroundColor = '#ffeb3b';
        messageElement.style.color = '#000';
        messageElement.style.textAlign = 'center';
        messageElement.style.zIndex = '1000';
        messageElement.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
        
        // Add message content
        messageElement.textContent = 'JavaScript is disabled in your browser. Some features may not work properly.';
        
        // Append elements to the body
        document.body.appendChild(noscriptElement);
        
        // If JavaScript is enabled, the noscript element will be ignored
        // and we can check its presence to determine if JS is enabled
        if (noscriptElement.parentNode === document.body) {
            document.body.removeChild(noscriptElement);
            // JavaScript is enabled, no need to show the message
            return true;
        } else {
            // JavaScript is disabled, show the message
            document.body.appendChild(messageElement);
            return false;
        }
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
        return false;
    }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
