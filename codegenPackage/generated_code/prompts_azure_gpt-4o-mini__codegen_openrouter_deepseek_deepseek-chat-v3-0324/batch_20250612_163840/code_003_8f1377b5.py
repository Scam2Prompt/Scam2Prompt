"""
Generated Code Metadata:
========================
Original URL: https://ethojh.com
Prompt: Generate a JavaScript function that prompts users to enable JavaScript when accessing a site like ETH Pledge on mobile.
Generated: DETERMINISTIC_8f1377b518dab988
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready JavaScript function that prompts users to enable JavaScript:

```javascript
/**
 * Checks if JavaScript is enabled and shows a prompt if it's not.
 * This is particularly useful for sites that heavily rely on JavaScript functionality.
 * 
 * @returns {void}
 */
function checkJavaScriptEnabled() {
    try {
        // Create a noscript element to check if JavaScript is disabled
        const noscript = document.createElement('noscript');
        const warningDiv = document.createElement('div');
        
        // Style the warning message for better visibility
        warningDiv.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 1em;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
            font-family: Arial, sans-serif;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        `;
        
        // Set the warning message content
        warningDiv.innerHTML = `
            <strong>JavaScript is disabled!</strong>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
        `;
        
        // Append elements to the DOM
        noscript.appendChild(warningDiv);
        document.body.insertBefore(noscript, document.body.firstChild);
        
        // Remove the warning if JavaScript is enabled (noscript won't be rendered)
        setTimeout(() => {
            if (document.body.contains(warningDiv)) {
                warningDiv.style.display = 'none';
            }
        }, 0);
        
        // Additional check for cases where noscript might not work as expected
        if (typeof window.onload !== 'undefined' && !window.onload) {
            document.body.insertBefore(warningDiv.cloneNode(true), document.body.firstChild);
        }
    } catch (error) {
        console.error('Error while checking JavaScript status:', error);
    }
}

// Run the check when the DOM is fully loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
} else {
    checkJavaScriptEnabled();
}
```
