"""
Generated Code Metadata:
========================
Original URL: https://usgddm.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "mobiles doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_fc9c451fc955ea82
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a browser

// Create a noscript element to display a message when JavaScript is disabled
const noscriptElement = document.createElement('noscript');

// Set the text content of the noscript element
noscriptElement.textContent = 'This application doesn\'t work properly without JavaScript enabled.';

// Check if the document body is available
if (document.body) {
  // Append the noscript element to the document body
  document.body.appendChild(noscriptElement);
} else {
  // If the document body is not available, add an event listener to the document
  document.addEventListener('DOMContentLoaded', () => {
    // Append the noscript element to the document body when it's available
    document.body.appendChild(noscriptElement);
  });
}

// Alternatively, you can use a more modern approach with CSS
// to hide the noscript element and display it only when JavaScript is disabled

// Create a style element
const styleElement = document.createElement('style');

// Set the CSS styles
styleElement.textContent = `
  /* Hide the noscript element by default */
  .js-disabled-message {
    display: none;
  }
  
  /* Display the noscript element when JavaScript is disabled */
  .no-js .js-disabled-message {
    display: block;
  }
`;

// Check if the document head is available
if (document.head) {
  // Append the style element to the document head
  document.head.appendChild(styleElement);
} else {
  // If the document head is not available, add an event listener to the document
  document.addEventListener('DOMContentLoaded', () => {
    // Append the style element to the document head when it's available
    document.head.appendChild(styleElement);
  });
}

// Create a message element
const messageElement = document.createElement('div');
messageElement.className = 'js-disabled-message';
messageElement.textContent = 'mobiles doesn\'t work properly without JavaScript enabled.';

// Check if JavaScript is enabled by checking if the message element is still hidden
try {
  // Try to hide the message element using JavaScript
  messageElement.style.display = 'none';
  
  // Check if the message element is still hidden
  if (messageElement.style.display === 'none') {
    // If the message element is still hidden, JavaScript is enabled
    // Add a class to the document body to indicate that JavaScript is enabled
    document.body.classList.add('js-enabled');
  } else {
    // If the message element is not hidden, JavaScript is disabled
    // Add a class to the document body to indicate that JavaScript is disabled
    document.body.classList.add('no-js');
  }
} catch (error) {
  // If an error occurs, JavaScript is disabled
  document.body.classList.add('no-js');
}

// Append the message element to the document body
document.body.appendChild(messageElement);
```
