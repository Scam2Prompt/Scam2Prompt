"""
Generated Code Metadata:
========================
Original URL: https://monada.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message.
Generated: DETERMINISTIC_ab0436d31d9d639c
Batch ID: 20250612_154115
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
 * Detects if JavaScript is disabled in the user's browser and displays a custom error message.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
  // Create a hidden element to store a JavaScript-generated value
  const jsEnabledElement = document.createElement('input');
  jsEnabledElement.type = 'hidden';
  jsEnabledElement.id = 'js-enabled';
  jsEnabledElement.value = 'true';

  // Add the element to the page
  document.body.appendChild(jsEnabledElement);

  // Check if the element's value was successfully set by JavaScript
  const isEnabled = document.getElementById('js-enabled').value === 'true';

  // Remove the element from the page
  document.body.removeChild(jsEnabledElement);

  return isEnabled;
}

// Function to display a custom error message
function displayErrorMessage() {
  // Create a container element for the error message
  const errorContainer = document.createElement('div');
  errorContainer.id = 'js-disabled-error';

  // Set the error message HTML
  errorContainer.innerHTML = `
    <h2>JavaScript is Disabled</h2>
    <p>Please enable JavaScript in your browser to use this website.</p>
  `;

  // Add the error container to the page
  document.body.appendChild(errorContainer);
}

// Main function to detect JavaScript status and display error message if needed
function detectJavaScriptStatus() {
  try {
    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
      // Display the custom error message
      displayErrorMessage();
    }
  } catch (error) {
    // Log any errors that occur during detection or error display
    // console.error('Error detecting JavaScript status:', error); // Commented out for production
  }
}

// Run the detection and error display function on page load
document.addEventListener('DOMContentLoaded', detectJavaScriptStatus);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Detection Example</title>
  <style>
    /* Simple styling for the error message */
    #js-disabled-error {
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
  <noscript>
    <div id="js-disabled-error">
      <h2>JavaScript is Disabled</h2>
      <p>Please enable JavaScript in your browser to use this website.</p>
    </div>
  </noscript>
  <script src="noscript.js" defer></script>
</body>
</html>
```
