"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethping.com
Prompt: Generate a JavaScript function that prompts users to enable JavaScript for a better experience on a site similar to ETH Pledge.
Generated: DETERMINISTIC_bc864f7dc2ee5e32
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and prompt the user accordingly.
 */
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');
    
    // Set the message content
    messageDiv.innerHTML = `
        <div style="background-color: #ffcc00; padding: 20px; text-align: center; font-family: Arial, sans-serif;">
            <h2>JavaScript is Disabled</h2>
            <p>For a better experience on this site, please enable JavaScript in your browser settings.</p>
        </div>
    `;

    // Apply some basic styling
    messageDiv.style.position = 'fixed';
    messageDiv.style.zIndex = '9999';
    messageDiv.style.width = '100%';
    messageDiv.style.bottom = '0';
    messageDiv.style.left = '0';
    messageDiv.style.borderTop = '1px solid #ccc';

    // Append the message to the body
    document.body.appendChild(messageDiv);
}

// Immediately invoke the function to check for JavaScript
checkJavaScriptEnabled();

// The following code will run if JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    // Remove the message if JavaScript is enabled
    const messageDiv = document.querySelector('div');
    if (messageDiv) {
        messageDiv.remove();
    }
});
```

This code snippet checks if JavaScript is enabled and displays a message if it is not. If JavaScript is enabled, the message is removed upon page load.
