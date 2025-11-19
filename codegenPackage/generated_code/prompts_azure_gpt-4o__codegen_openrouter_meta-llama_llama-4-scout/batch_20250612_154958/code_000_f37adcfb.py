"""
Generated Code Metadata:
========================
Original URL: https://aubi.online
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the behavior on the "aubi.online" domain details page.
Generated: DETERMINISTIC_f37adcfbec78c53f
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScriptEnabledChecker.js

/**
 * Checks if JavaScript is enabled in the browser and displays a custom message if it's disabled.
 */

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
  // Create a hidden element to store the message
  const messageElement = document.createElement('div');
  messageElement.style.display = 'none';
  messageElement.id = 'js-disabled-message';

  // Append the message element to the body
  document.body.appendChild(messageElement);

  // Check if JavaScript is enabled by trying to access the element
  try {
    // If JavaScript is enabled, this line will execute without errors
    const jsEnabledTest = document.getElementById('js-enabled-test');
    if (jsEnabledTest) {
      // JavaScript is enabled, remove the message element
      messageElement.remove();
    } else {
      // JavaScript is disabled, display the custom message
      displayDisabledMessage();
    }
  } catch (error) {
    // If an error occurs, JavaScript is likely disabled
    displayDisabledMessage();
  }
}

// Function to display a custom message if JavaScript is disabled
function displayDisabledMessage() {
  const messageElement = document.getElementById('js-disabled-message');
  if (messageElement) {
    // Set the custom message
    messageElement.textContent = 'JavaScript is disabled. Please enable JavaScript to use this website.';
    messageElement.style.display = 'block';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#FFC080';
    messageElement.style.color = '#333';
    messageElement.style.padding = '1em';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '1000';
  }
}

// Run the check on page load
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Enabled Checker</title>
  <style>
    /* Add some basic styling to the page */
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <!-- Add a test element to check if JavaScript is enabled -->
  <noscript id="js-enabled-test">JavaScript is disabled</noscript>
  <script src="JavaScriptEnabledChecker.js"></script>
</body>
</html>
```
