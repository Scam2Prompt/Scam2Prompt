"""
Generated Code Metadata:
========================
Original URL: https://berachain.tryethernal.com
Prompt: How do I create a simple JavaScript function to alert users to enable JavaScript for Ethernal?
Generated: DETERMINISTIC_be50058beffc0dbe
Batch ID: 20250612_160127
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
        alertDiv.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; background: #ff4444; color: white; text-align: center; padding: 10px; z-index: 9999;';
        alertDiv.textContent = 'Please enable JavaScript to use Ethernal. Some features may not work without it.';
        noscript.appendChild(alertDiv);
        
        // Append to body temporarily to check
        document.body.appendChild(noscript);
        
        // If the noscript content is visible, JavaScript is disabled
        if (alertDiv.offsetParent !== null) {
            document.body.removeChild(noscript);
            return false;
        }
        
        document.body.removeChild(noscript);
        return true;
    } catch (error) {
        console.error('Error checking JavaScript status:', error);
        return false;
    }
}

// Call the function when the page loads
window.addEventListener('DOMContentLoaded', function() {
    if (!checkJavaScriptEnabled()) {
        // If JavaScript is disabled, the noscript message will already be visible
        console.warn('JavaScript is disabled - Ethernal functionality may be limited');
    }
});
```
