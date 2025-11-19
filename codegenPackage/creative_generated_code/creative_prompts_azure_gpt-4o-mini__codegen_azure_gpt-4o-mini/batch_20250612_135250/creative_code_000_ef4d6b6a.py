"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: How can I enable JavaScript in my browser to access the Arbitrum domain details page?
Generated: DETERMINISTIC_ef4d6b6a3f61a4f9
Batch ID: 20250612_135250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script checks if JavaScript is enabled in the browser.
// If the script runs, it indicates that JavaScript is enabled.

// Function to create a message element
function createMessageElement(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.style.fontSize = '18px';
    messageElement.style.color = 'green';
    messageElement.style.margin = '20px';
    return messageElement;
}

// Run when the document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    try {
        // Check for JavaScript enabled
        const message = "JavaScript is enabled in your browser! You can now access the Arbitrum domain details page.";
        const messageElement = createMessageElement(message);
        
        // Append the message to the body
        document.body.appendChild(messageElement);
    } catch (error) {
        console.error("An error occurred while checking JavaScript status:", error);
    }
});
```
