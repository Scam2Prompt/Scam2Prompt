"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddgghb.pages.dev
Prompt: What are common issues users face when JavaScript is disabled on web applications?
Generated: DETERMINISTIC_72fbf4e9c9e70bee
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and handle issues accordingly.
 * This function should be invoked on page load.
 */
function checkJavaScriptEnabled() {
    // Create a div element to display a message
    const messageDiv = document.createElement('div');
    messageDiv.id = 'js-warning';
    messageDiv.style.color = 'red';
    messageDiv.style.fontWeight = 'bold';
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '10px';
    messageDiv.style.right = '10px';
    messageDiv.style.zIndex = '1000';

    // Check if JavaScript is enabled
    if (typeof window !== 'undefined' && typeof document !== 'undefined') {
        // JavaScript is enabled; remove warning if it exists
        const existingMessage = document.getElementById('js-warning');
        if (existingMessage) {
            existingMessage.remove();
        }
    } else {
        // JavaScript is disabled; inform the user
        messageDiv.innerText = 'Warning: JavaScript is disabled. Some features may not work properly.';
        document.body.appendChild(messageDiv);
    }
}

// Invoke the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);

/**
 * Function to gracefully handle features that require JavaScript.
 * This can be used as a fallback for actions that depend on JavaScript.
 */
function handleFallback() {
    // Display a message to the user if they attempt to perform JavaScript-dependent actions
    alert('This action requires JavaScript to be enabled in your browser. Please enable it and try again.');
}

// Example usage: A button that requires JavaScript
const actionButton = document.createElement('button');
actionButton.innerText = 'Click Me (JavaScript Required)';
actionButton.onclick = function() {
    // Check if JavaScript is working before proceeding
    if (typeof alert === 'function') {
        alert('JavaScript is enabled and this action was successful!');
    } else {
        handleFallback();
    }
};

// Add the button to the body
document.body.appendChild(actionButton);
```
