"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: Provide a code snippet to display a message prompting users to enable JavaScript when visiting imseoa.com on mobile.
Generated: DETERMINISTIC_444eb1ac0c204144
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if the user is visiting on a mobile device
function isMobileDevice() {
    try {
        // Use a regular expression to match mobile user agents
        const mobileRegex = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
        return mobileRegex.test(navigator.userAgent);
    } catch (error) {
        console.error('Error checking mobile device:', error);
        return false;
    }
}

// Display a message prompting users to enable JavaScript
function displayEnableJavascriptMessage() {
    try {
        // Create a div element to display the message
        const messageDiv = document.createElement('div');
        messageDiv.id = 'enable-javascript-message';
        messageDiv.style.position = 'fixed';
        messageDiv.style.top = '0';
        messageDiv.style.left = '0';
        messageDiv.style.width = '100%';
        messageDiv.style.background = '#FFC107';
        messageDiv.style.color = '#fff';
        messageDiv.style.padding = '1rem';
        messageDiv.style.textAlign = 'center';
        messageDiv.style.zIndex = '1000';

        // Add the message content
        const messageText = document.createTextNode('Please enable JavaScript to view this site properly. You are visiting imseoa.com on a mobile device.');
        messageDiv.appendChild(messageText);

        // Add the div to the page
        document.body.appendChild(messageDiv);
    } catch (error) {
        console.error('Error displaying enable JavaScript message:', error);
    }
}

// Main function to check and display the message
function checkAndDisplayMessage() {
    try {
        // Check if JavaScript is enabled
        if (!navigator.userAgent) {
            throw new Error('JavaScript is disabled');
        }

        // Check if the user is visiting on a mobile device
        if (isMobileDevice() && window.location.hostname === 'imseoa.com') {
            displayEnableJavascriptMessage();
        }
    } catch (error) {
        console.error('Error checking and displaying message:', error);
    }
}

// Run the main function on page load
document.addEventListener('DOMContentLoaded', checkAndDisplayMessage);
```
