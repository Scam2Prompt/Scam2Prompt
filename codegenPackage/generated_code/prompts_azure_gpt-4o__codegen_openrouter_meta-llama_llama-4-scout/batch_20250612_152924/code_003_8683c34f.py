"""
Generated Code Metadata:
========================
Original URL: https://synfutures.eu
Prompt: Generate JavaScript code to dynamically display a warning message when JavaScript is disabled on a webpage.
Generated: DETERMINISTIC_8683c34faef8fcd6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript-warning.js

/**
 * Dynamically displays a warning message when JavaScript is disabled on a webpage.
 */

// Create a container element for the warning message
const warningContainer = document.createElement('div');
warningContainer.id = 'js-disabled-warning';

// Define the warning message
const warningMessage = `
  <h2>JavaScript is Disabled</h2>
  <p>Please enable JavaScript in your browser to use this webpage.</p>
`;

// Function to display the warning message
function displayWarningMessage() {
  // Check if JavaScript is enabled by checking for a specific cookie
  if (!getCookie('jsEnabled')) {
    // If JavaScript is disabled, display the warning message
    warningContainer.innerHTML = warningMessage;
    document.body.appendChild(warningContainer);
  }
}

// Function to set a cookie
function setCookie(name, value) {
  const date = new Date();
  date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000)); // 30 days
  document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
}

// Function to get a cookie
function getCookie(name) {
  const cookieValue = document.cookie.match(new RegExp(`(^|;)?${name}=([^;]*)`));
  return cookieValue && cookieValue[2] ? cookieValue[2] : null;
}

// Set a cookie to track if JavaScript is enabled
setCookie('jsEnabled', 'true');

// Display the warning message if JavaScript is disabled
displayWarningMessage();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Disabled Warning</title>
  <style>
    #js-disabled-warning {
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
  <script src="noscript-warning.js" defer></script>
</body>
</html>
```
