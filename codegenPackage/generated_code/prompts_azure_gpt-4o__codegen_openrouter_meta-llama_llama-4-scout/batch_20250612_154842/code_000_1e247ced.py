"""
Generated Code Metadata:
========================
Original URL: https://pns.paladin.coinbaseindexfund.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message instructing the user to enable it, similar to the functionality described on `pns.paladin.coinbaseindexfund.com`.
Generated: DETERMINISTIC_1e247ced8ab9566c
Batch ID: 20250612_154842
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
 * Detects if JavaScript is disabled in the browser and displays a message
 * instructing the user to enable it.
 */

// Get the noscript element
const noscriptElement = document.getElementById('noscript-message');

/**
 * Check if JavaScript is enabled by attempting to execute a simple script.
 * If the script runs, then JavaScript is enabled. Otherwise, it's disabled.
 */
function isJavaScriptEnabled() {
  try {
    // Try to execute a simple script
    return window.self !== window.top;
  } catch (e) {
    // If an error occurs, assume JavaScript is disabled
    return false;
  }
}

/**
 * Display a message instructing the user to enable JavaScript.
 */
function displayEnableJavascriptMessage() {
  if (noscriptElement) {
    noscriptElement.style.display = 'block';
  }
}

/**
 * Initialize the script and check if JavaScript is enabled.
 */
function init() {
  if (!isJavaScriptEnabled()) {
    displayEnableJavascriptMessage();
  } else {
    // If JavaScript is enabled, hide the noscript message
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
      background-color: #FFC080;
      border: 1px solid #FF9900;
      padding: 1em;
      text-align: center;
    }
  </style>
</head>
<body>
  <noscript id="noscript-message">
    <h2>JavaScript is Disabled</h2>
    <p>Please enable JavaScript in your browser to use this site.</p>
  </noscript>
  <script src="noscript.js" defer></script>
</body>
</html>
```
