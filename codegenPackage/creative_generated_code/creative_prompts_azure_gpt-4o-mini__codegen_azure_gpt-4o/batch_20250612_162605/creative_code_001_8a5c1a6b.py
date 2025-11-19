"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.fi
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled on a webpage similar to the Polkadot domain details page.
Generated: DETERMINISTIC_8a5c1a6b2ca439b3
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if JavaScript is enabled on the webpage and displays a message accordingly.
 * This script can be embedded in the HTML file to notify users about JavaScript support.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Create a container element for the message
  const messageContainer = document.createElement('div');
  messageContainer.id = 'js-check-message';

  // Style the container for better visibility
  messageContainer.style.position = 'absolute';
  messageContainer.style.top = '10px';
  messageContainer.style.left = '10px';
  messageContainer.style.padding = '10px';
  messageContainer.style.backgroundColor = '#f8d7da';
  messageContainer.style.color = '#721c24';
  messageContainer.style.border = '1px solid #f5c6cb';
  messageContainer.style.borderRadius = '5px';
  messageContainer.style.fontFamily = 'Arial, sans-serif';
  messageContainer.style.fontSize = '14px';

  try {
    // Add a message indicating JavaScript is enabled
    messageContainer.innerText = 'JavaScript is enabled on this webpage.';
  } catch (error) {
    // Handle any unexpected errors gracefully
    console.error('An error occurred while checking JavaScript status:', error);
    messageContainer.innerText = 'An unexpected error occurred.';
  }

  // Append the container element to the body
  document.body.appendChild(messageContainer);
});

// Note:
// If JavaScript is disabled, this script will not run,
// and no message will be displayed on the webpage.
```
