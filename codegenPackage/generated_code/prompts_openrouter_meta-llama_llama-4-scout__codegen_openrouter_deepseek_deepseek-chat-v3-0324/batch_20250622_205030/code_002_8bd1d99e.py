"""
Generated Code Metadata:
========================
Original URL: https://cur.ve.fi
Prompt: Write a basic JavaScript code snippet that checks if JavaScript is enabled on a webpage and displays a different message based on its status.
Generated: DETERMINISTIC_8bd1d99e80fc00f5
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and displays a message accordingly.
 * This function should be called when the DOM is fully loaded.
 */
function checkJavaScriptStatus() {
    // Create a message element
    const messageElement = document.createElement('div');
    messageElement.id = 'js-status-message';
    messageElement.style.padding = '1rem';
    messageElement.style.margin = '1rem 0';
    messageElement.style.borderRadius = '4px';
    
    // JavaScript is enabled - set success message
    messageElement.textContent = 'JavaScript is enabled on this page.';
    messageElement.style.backgroundColor = '#d4edda';
    messageElement.style.color = '#155724';
    messageElement.style.border = '1px solid #c3e6cb';
    
    // Add the message to the body
    document.body.insertBefore(messageElement, document.body.firstChild);
}

// Check if the DOM is already loaded
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    checkJavaScriptStatus();
} else {
    // Wait for DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', checkJavaScriptStatus);
}

// Fallback for browsers that don't support noscript
document.write('<noscript>JavaScript is disabled on this page.</noscript>');
```
