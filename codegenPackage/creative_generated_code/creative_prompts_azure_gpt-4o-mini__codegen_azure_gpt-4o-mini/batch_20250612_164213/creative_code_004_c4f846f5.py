"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catalysts.in
Prompt: Write a JavaScript function to dynamically update a message on a website that is under construction.
Generated: DETERMINISTIC_c4f846f51bda9afd
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates the construction message on the webpage dynamically.
 * @param {string} message - The message to display.
 * @param {number} duration - The duration in seconds before the message changes.
 */
function updateConstructionMessage(message, duration) {
    // Get the message container element
    const messageContainer = document.getElementById('construction-message');

    // Validate input parameters
    if (!messageContainer) {
        console.error('Message container not found.');
        return;
    }
    if (typeof message !== 'string' || message.trim() === '') {
        console.error('Invalid message. It must be a non-empty string.');
        return;
    }
    if (typeof duration !== 'number' || duration <= 0) {
        console.error('Invalid duration. It must be a positive number.');
        return;
    }

    // Update the message content
    messageContainer.textContent = message;

    // Set a timeout to clear the message after the specified duration
    setTimeout(() => {
        messageContainer.textContent = 'Thank you for your patience! We are under construction.';
    }, duration * 1000);
}

// Example usage: Update the construction message to 'Website is coming soon!' for 5 seconds.
updateConstructionMessage('Website is coming soon!', 5);
```

Make sure to include a corresponding HTML element for this script to work. For example:

```html
<div id="construction-message"></div>
```
