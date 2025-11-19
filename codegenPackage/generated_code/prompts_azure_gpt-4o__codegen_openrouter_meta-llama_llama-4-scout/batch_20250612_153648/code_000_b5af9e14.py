"""
Generated Code Metadata:
========================
Original URL: https://earndrop.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message prompting the user to enable it.
Generated: DETERMINISTIC_b5af9e14f0d94381
Batch ID: 20250612_153648
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
 * Detects if JavaScript is disabled in the browser and displays a custom message.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
  // Create a hidden element to store a JavaScript-generated value
  const jsEnabledElement = document.createElement('div');
  jsEnabledElement.style.display = 'none';
  jsEnabledElement.id = 'js-enabled';
  document.body.appendChild(jsEnabledElement);

  // Set a JavaScript-generated value
  jsEnabledElement.textContent = 'JavaScript is enabled';

  // Check if the value was set successfully
  return jsEnabledElement.textContent === 'JavaScript is enabled';
}

// Function to display a custom message if JavaScript is disabled
function displayMessageIfJsDisabled() {
  // Check if JavaScript is enabled
  if (!isJavaScriptEnabled()) {
    // Create a custom message element
    const messageElement = document.createElement('div');
    messageElement.id = 'js-disabled-message';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#FFC080';
    messageElement.style.color = '#333';
    messageElement.style.padding = '1em';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '1000';

    // Set the custom message
    messageElement.textContent = 'JavaScript is disabled. Please enable it to use this website properly.';

    // Append the message element to the body
    document.body.appendChild(messageElement);
  }
}

// Call the function to display the message if JavaScript is disabled
displayMessageIfJsDisabled();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Detection</title>
  <script src="noscript.js" defer></script>
</head>
<body>
  <!-- Your website content here -->
</body>
</html>
```
