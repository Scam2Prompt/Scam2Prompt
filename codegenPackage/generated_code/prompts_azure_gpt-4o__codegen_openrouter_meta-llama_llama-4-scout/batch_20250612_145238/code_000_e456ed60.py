"""
Generated Code Metadata:
========================
Original URL: https://arkhamintelligence.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior on the Arkham Intelligence website.
Generated: DETERMINISTIC_e456ed609fbd2ab4
Batch ID: 20250612_145238
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
 * Check if JavaScript is enabled by trying to set a dummy variable.
 * If the variable is not set, it means JavaScript is disabled.
 */
function isJavaScriptEnabled() {
  try {
    // Try to set a dummy variable
    window.javascriptEnabled = true;
    return true;
  } catch (e) {
    // If an error occurs, it means JavaScript is disabled
    return false;
  }
}

/**
 * Display the noscript message to the user.
 */
function displayNoscriptMessage() {
  if (noscriptElement) {
    noscriptElement.style.display = 'block';
  }
}

/**
 * Initialize the script.
 */
function init() {
  // Check if JavaScript is enabled
  if (!isJavaScriptEnabled()) {
    // If not, display the noscript message
    displayNoscriptMessage();
  } else {
    // If JavaScript is enabled, try to remove the noscript message
    if (noscriptElement) {
      noscriptElement.style.display = 'none';
    }
  }
}

// Initialize the script on page load
document.addEventListener('DOMContentLoaded', init);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Detection</title>
  <style>
    #noscript-message {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #FFC080;
      color: #333;
      padding: 1em;
      text-align: center;
      z-index: 1000;
    }
  </style>
</head>
<body>
  <noscript id="noscript-message">
    <p>JavaScript is disabled. Please enable JavaScript to use this website.</p>
  </noscript>
  <script src="noscript.js" defer></script>
</body>
</html>
```
