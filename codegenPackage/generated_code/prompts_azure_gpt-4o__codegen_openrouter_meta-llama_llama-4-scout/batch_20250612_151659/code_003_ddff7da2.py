"""
Generated Code Metadata:
========================
Original URL: https://full-mint-website-master.pages.dev
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message accordingly, as seen in the React app at https://full-mint-website-master.pages.dev.
Generated: DETERMINISTIC_ddff7da2e811d8c8
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a message accordingly.
 */

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
  // Create a noscript element to display a message when JavaScript is disabled
  const noscriptElement = document.createElement('noscript');
  const messageElement = document.createElement('div');

  // Set the message to display when JavaScript is disabled
  messageElement.textContent = 'Please enable JavaScript to view this website properly.';
  messageElement.style.color = 'red';
  messageElement.style.fontWeight = 'bold';
  messageElement.style.textAlign = 'center';
  messageElement.style.padding = '1rem';

  // Append the message element to the noscript element
  noscriptElement.appendChild(messageElement);

  // Append the noscript element to the body
  document.body.appendChild(noscriptElement);

  // Check if the noscript element is still present after page load
  window.addEventListener('load', () => {
    if (noscriptElement.parentNode) {
      // If the noscript element is still present, JavaScript is enabled, so remove it
      document.body.removeChild(noscriptElement);
    } else {
      // If the noscript element is not present, JavaScript is enabled, so display a success message
      const successMessageElement = document.createElement('div');
      successMessageElement.textContent = 'JavaScript is enabled.';
      successMessageElement.style.color = 'green';
      successMessageElement.style.fontWeight = 'bold';
      successMessageElement.style.textAlign = 'center';
      successMessageElement.style.padding = '1rem';
      document.body.appendChild(successMessageElement);
    }
  });
}

// Call the function to check if JavaScript is enabled
checkJavaScriptEnabled();
```
