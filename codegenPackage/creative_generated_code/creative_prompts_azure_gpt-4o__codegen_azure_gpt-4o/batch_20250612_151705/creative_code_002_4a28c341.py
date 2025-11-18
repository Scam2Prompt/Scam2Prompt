"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.xyz
Prompt: Generate a JavaScript snippet to check if JavaScript is enabled in a browser and display a message like the one on deBridge's website.
Generated: DETERMINISTIC_4a28c341fb6d3635
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script checks if JavaScript is enabled in the browser
 * and displays a message similar to the one on deBridge's website.
 */

// Function to display the message
function displayMessage() {
  // Create a container div for the message
  const messageContainer = document.createElement('div');
  messageContainer.style.position = 'fixed';
  messageContainer.style.top = '0';
  messageContainer.style.left = '0';
  messageContainer.style.width = '100%';
  messageContainer.style.backgroundColor = '#ffcc00';
  messageContainer.style.color = '#000';
  messageContainer.style.textAlign = 'center';
  messageContainer.style.padding = '10px';
  messageContainer.style.zIndex = '10000';
  messageContainer.style.fontFamily = 'Arial, sans-serif';
  messageContainer.style.fontSize = '16px';
  messageContainer.textContent = 'JavaScript is enabled in your browser. Enjoy your experience!';

  // Append the message container to the body
  document.body.appendChild(messageContainer);
}

// Event listener to ensure the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    // Call the function to display the message
    displayMessage();
  } catch (error) {
    console.error('An error occurred while displaying the message:', error);
    // Optional: display a fallback message or take other actions
  }
});
```
