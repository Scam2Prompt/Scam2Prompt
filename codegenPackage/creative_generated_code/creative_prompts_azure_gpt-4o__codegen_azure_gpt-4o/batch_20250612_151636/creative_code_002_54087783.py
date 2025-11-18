"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcium.de
Prompt: Create a JavaScript function that checks if JavaScript is enabled in a browser and displays a message similar to the one on https://arcium.de.
Generated: DETERMINISTIC_5408778381d75f1c
Batch ID: 20250612_151636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the browser
 * and display a message on the page accordingly.
 */
function checkJavaScriptEnabled() {
  try {
    // Create a container element for the message
    const messageContainer = document.createElement('div');
    messageContainer.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      padding: 10px;
      background-color: #f8d7da;
      color: #721c24;
      text-align: center;
      border: 1px solid #f5c6cb;
      font-family: Arial, sans-serif;
      font-size: 16px;
      z-index: 9999;
    `;

    // Text content indicating JavaScript is enabled
    messageContainer.innerText =
      'JavaScript is enabled in your browser. Enjoy the full functionality of this site!';

    // Append the message container to the body
    document.body.appendChild(messageContainer);

    // Automatically hide the message after 5 seconds
    setTimeout(() => {
      messageContainer.style.display = 'none';
    }, 5000);
  } catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
  }
}

// Run the function to display the message
checkJavaScriptEnabled();
```
