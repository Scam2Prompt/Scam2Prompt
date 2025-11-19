"""
Generated Code Metadata:
========================
Original URL: https://bigbonus.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it.
Generated: DETERMINISTIC_f867857d3fd3034b
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript.js

/**
 * Detects if JavaScript is disabled in the user's browser and displays a message prompting them to enable it.
 */

// Create a noscript element to display the message
const noscriptElement = document.createElement('noscript');
const messageElement = document.createElement('div');

// Set the message to be displayed
messageElement.textContent = 'JavaScript is disabled in your browser. Please enable it to use this application.';
messageElement.style.position = 'fixed';
messageElement.style.top = '0';
messageElement.style.left = '0';
messageElement.style.width = '100%';
messageElement.style.background = '#ff9800';
messageElement.style.color = '#fff';
messageElement.style.padding = '1em';
messageElement.style.textAlign = 'center';
messageElement.style.zIndex = '1000';

// Add the message element to the noscript element
noscriptElement.appendChild(messageElement);

// Add the noscript element to the page
document.body.appendChild(noscriptElement);

// Check if JavaScript is enabled by trying to set a cookie
try {
  // Set a test cookie
  document.cookie = 'javascriptEnabled=true; expires=Fri, 31 Dec 9999 23:59:59 GMT';

  // Check if the cookie was set
  const cookies = document.cookie.split('; ');
  const hasCookie = cookies.some(cookie => cookie.startsWith('javascriptEnabled=true'));

  // If the cookie was set, remove the noscript element
  if (hasCookie) {
    document.body.removeChild(noscriptElement);
  }
} catch (error) {
  // If an error occurs, log it and do nothing
  // console.error('Error checking JavaScript enabled:', error); // Commented out for production
}
```
