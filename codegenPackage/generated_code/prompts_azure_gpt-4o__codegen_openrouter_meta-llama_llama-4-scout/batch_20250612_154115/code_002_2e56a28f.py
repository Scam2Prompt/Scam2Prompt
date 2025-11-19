"""
Generated Code Metadata:
========================
Original URL: https://celestiacelestiia.com
Prompt: Create a script to detect whether JavaScript is enabled in a browser and display a message prompting users to enable it for "Glow Node" to work properly.
Generated: DETERMINISTIC_2e56a28f55ca2a7a
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// detect-javascript.js

/**
 * Detects whether JavaScript is enabled in the browser and displays a message
 * prompting users to enable it for "Glow Node" to work properly.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
  // If JavaScript is disabled, this function will not be executed.
  // We use a noscript element to display a message when JavaScript is disabled.
  return true;
}

// Function to display a message prompting users to enable JavaScript
function displayEnableJavascriptMessage() {
  const messageElement = document.getElementById('enable-javascript-message');
  if (messageElement) {
    messageElement.style.display = 'block';
  }
}

// Main function to check JavaScript status and display message if needed
function checkJavaScriptStatus() {
  try {
    // Check if JavaScript is enabled by trying to access the document object
    if (typeof document !== 'undefined') {
      if (!isJavaScriptEnabled()) {
        displayEnableJavascriptMessage();
      }
    } else {
      // If document object is undefined, JavaScript is likely disabled
      displayEnableJavascriptMessage();
    }
  } catch (error) {
    console.error('Error checking JavaScript status:', error);
    displayEnableJavascriptMessage();
  }
}

// Run the main function on page load
document.addEventListener('DOMContentLoaded', checkJavaScriptStatus);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Glow Node</title>
  <style>
    #enable-javascript-message {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ff9800;
      color: #fff;
      padding: 1em;
      text-align: center;
      z-index: 1000;
    }
  </style>
</head>
<body>
  <noscript id="enable-javascript-message">
    <p>Please enable JavaScript in your browser for Glow Node to work properly.</p>
  </noscript>
  <script src="detect-javascript.js" defer></script>
</body>
</html>
```
