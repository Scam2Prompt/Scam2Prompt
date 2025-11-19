"""
Generated Code Metadata:
========================
Original URL: https://freenft07.vercel.app
Prompt: Write JavaScript code to display a custom message when JavaScript is disabled, tailored for a web app like Fritzy v1.
Generated: DETERMINISTIC_fd0ff2321e1fa172
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noScript.js

/**
 * Displays a custom message when JavaScript is disabled.
 */

// Get the no script element
const noScriptElement = document.getElementById('no-script-message');

/**
 * Checks if JavaScript is enabled.
 * @returns {boolean} True if JavaScript is enabled, false otherwise.
 */
function isJavaScriptEnabled() {
  // Create a test element
  const testElement = document.createElement('div');
  testElement.style.display = 'none';

  // If the element is not displayed, JavaScript is enabled
  return testElement.style.display === 'none';
}

/**
 * Displays the custom message.
 */
function displayMessage() {
  // Check if no script element exists
  if (noScriptElement) {
    // Display the message
    noScriptElement.style.display = 'block';
  } else {
    // Log an error if no script element is not found
    console.error('No script element not found.');
  }
}

/**
 * Hides the custom message.
 */
function hideMessage() {
  // Check if no script element exists
  if (noScriptElement) {
    // Hide the message
    noScriptElement.style.display = 'none';
  }
}

// Check if JavaScript is enabled
if (isJavaScriptEnabled()) {
  // Hide the message if JavaScript is enabled
  hideMessage();

  // Add an event listener to handle page load
  window.addEventListener('load', () => {
    // Hide the message after page load
    hideMessage();
  });
} else {
  // Display the message if JavaScript is disabled
  displayMessage();
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fritzy v1</title>
  <style>
    #no-script-message {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ff9800;
      color: #fff;
      padding: 1em;
      text-align: center;
    }
  </style>
</head>
<body>
  <noscript id="no-script-message">
    <p>Please enable JavaScript to use Fritzy v1.</p>
  </noscript>

  <script src="noScript.js"></script>
</body>
</html>
```
