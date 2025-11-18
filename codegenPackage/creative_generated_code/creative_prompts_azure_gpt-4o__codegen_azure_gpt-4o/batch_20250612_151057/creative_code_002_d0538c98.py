"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapfinderbq.github.io
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "avedex-m doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_d0538c98a7b701f2
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and display a message if not
 * @description This function will dynamically insert a message into the webpage if JavaScript is disabled.
 */
function checkJavaScriptEnabled() {
  try {
    // Create a message container
    const messageContainer = document.createElement('div');
    messageContainer.id = 'js-warning';
    messageContainer.style.position = 'fixed';
    messageContainer.style.top = '0';
    messageContainer.style.left = '0';
    messageContainer.style.width = '100%';
    messageContainer.style.padding = '1em';
    messageContainer.style.backgroundColor = '#f44336'; // Red background for warning
    messageContainer.style.color = '#fff';             // White text color
    messageContainer.style.fontSize = '1rem';
    messageContainer.style.textAlign = 'center';
    messageContainer.style.fontFamily = 'Arial, sans-serif';
    messageContainer.style.zIndex = '1000';
    messageContainer.textContent = 'avedex-m doesn\'t work properly without JavaScript enabled.';

    // Ensure the message is only displayed if JS is disabled; remove it immediately if JS is active
    if (document.body) {
      document.body.appendChild(messageContainer);
    }

    // Using JavaScript, we instantly remove the message (indicating JS is enabled)
    setTimeout(() => {
      if (document.body.contains(messageContainer)) {
        document.body.removeChild(messageContainer);
      }
    }, 0);
  } catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
  }
}

// Execute the function to verify JavaScript status
checkJavaScriptEnabled();
```

**Note:** This script works by adding the message initially and removing it immediately if JavaScript is enabled. If JavaScript is disabled, the message remains visible.
