"""
Generated Code Metadata:
========================
Original URL: https://mybonkbox.web.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior of BONKBOXES.
Generated: DETERMINISTIC_4cc08b7b0ace4d3b
Batch ID: 20250612_152249
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
 * Detects if JavaScript is disabled in the browser and displays a message prompting the user to enable it.
 */

// Get the noscript element
const noscriptElement = document.getElementById('noscript-message');

/**
 * Check if JavaScript is enabled by checking if the noscript element is hidden.
 * If it's not hidden, it means JavaScript is disabled.
 */
function checkJavascriptEnabled() {
  try {
    // If JavaScript is enabled, this will throw an error
    if (noscriptElement.style.display !== 'none') {
      // JavaScript is disabled, show the message
      showMessage();
    }
  } catch (error) {
    // If an error occurs, it's likely because JavaScript is disabled
    showMessage();
  }
}

/**
 * Displays the message prompting the user to enable JavaScript.
 */
function showMessage() {
  // Get the body element
  const body = document.body;

  // Create a message element if it doesn't exist
  if (!noscriptElement) {
    const messageElement = document.createElement('div');
    messageElement.id = 'noscript-message';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#FF0000';
    messageElement.style.color = '#FFFFFF';
    messageElement.style.padding = '1em';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '1000';

    // Set the message text
    messageElement.innerText = 'JavaScript is disabled. Please enable it to use this site.';

    // Add the message element to the body
    body.appendChild(messageElement);
  } else {
    // Show the existing message element
    noscriptElement.style.display = 'block';
  }
}

// Check if JavaScript is enabled on page load
document.addEventListener('DOMContentLoaded', checkJavascriptEnabled);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BONKBOXES-like JavaScript Detection</title>
  <style>
    #noscript-message {
      display: none;
    }
  </style>
</head>
<body>
  <script src="noscript.js" defer></script>
</body>
</html>
```
