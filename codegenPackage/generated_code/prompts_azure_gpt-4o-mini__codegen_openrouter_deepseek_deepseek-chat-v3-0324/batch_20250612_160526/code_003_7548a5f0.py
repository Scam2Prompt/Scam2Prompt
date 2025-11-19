"""
Generated Code Metadata:
========================
Original URL: https://gog.auction
Prompt: How do I create a JavaScript function that alerts users to enable JavaScript on GOG Auction?
Generated: DETERMINISTIC_7548a5f003a331cf
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and alerts the user if it's not.
 * This function should be called when the page loads.
 */
function checkJavaScriptEnabled() {
    try {
        // Create a noscript element to check if JavaScript is disabled
        const noscript = document.createElement('noscript');
        const alertDiv = document.createElement('div');
        alertDiv.className = 'js-alert';
        alertDiv.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 15px;
            background-color: #f8d7da;
            color: #721c24;
            text-align: center;
            z-index: 9999;
            border-bottom: 1px solid #f5c6cb;
        `;
        alertDiv.innerHTML = `
            <strong>Warning:</strong> JavaScript is disabled in your browser. 
            Please enable JavaScript to use GOG Auction properly.
        `;
        
        noscript.appendChild(alertDiv);
        document.body.insertBefore(noscript, document.body.firstChild);

        // If JavaScript is enabled, remove the noscript element
        setTimeout(() => {
            if (document.body.contains(noscript)) {
                document.body.removeChild(noscript);
            }
        }, 0);
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
    }
}

// Call the function when the page loads
window.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
