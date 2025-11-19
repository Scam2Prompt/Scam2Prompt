"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheesh.vc
Prompt: Write a function in JavaScript that checks if JavaScript is enabled and displays a message for users visiting a venture capital site.
Generated: DETERMINISTIC_52275446252f8dbb
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a message element to display to the user
    const messageElement = document.createElement('div');
    
    // Set the style of the message element for better visibility
    messageElement.style.position = 'fixed';
    messageElement.style.top = '10px';
    messageElement.style.right = '10px';
    messageElement.style.padding = '10px';
    messageElement.style.backgroundColor = '#4CAF50'; // Green background
    messageElement.style.color = '#ffffff'; // White text
    messageElement.style.zIndex = '1000'; // Ensure it appears on top

    // Function to display a message for users
    function displayMessage(message) {
        messageElement.textContent = message;
        document.body.appendChild(messageElement);
    }

    // Check if JavaScript is enabled
    try {
        // If this function is executed, it means JavaScript is enabled
        displayMessage('JavaScript is enabled. Welcome to our venture capital site!');
        
        // Optionally, you can add any additional functionality here
        // For example, initializing site-specific features
    } catch (error) {
        // Log error for debugging purposes
        console.error('Error displaying message:', error);
        
        // Display a fallback message for users if anything goes wrong
        displayMessage('There was an error displaying the message. Please try again.');
    }
}

// Call the function to check if JavaScript is enabled upon page load
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
