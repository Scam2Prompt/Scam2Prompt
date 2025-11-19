"""
Generated Code Metadata:
========================
Original URL: https://combo.magiceden.nl
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on the Magic Eden NL domain details page.
Generated: DETERMINISTIC_6f5d1f8455c31d50
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a user's browser

// Create a noscript element to display a custom message when JavaScript is disabled
const noscriptElement = document.createElement('noscript');
noscriptElement.innerHTML = `
  <style>
    /* Add some basic styling to make the message more prominent */
    .js-disabled-message {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #FFC080;
      color: #333;
      text-align: center;
      padding: 1em;
      font-weight: bold;
    }
  </style>
  <div class="js-disabled-message">
    <p>JavaScript is disabled in your browser.</p>
    <p>Please enable JavaScript to use this website.</p>
  </div>
`;

// Append the noscript element to the body of the HTML document
document.body.appendChild(noscriptElement);

// Create a script to detect if JavaScript is enabled
const jsEnabledScript = document.createElement('script');
jsEnabledScript.innerHTML = `
  // Remove the noscript element when JavaScript is enabled
  const noscriptElement = document.querySelector('noscript');
  if (noscriptElement) {
    noscriptElement.remove();
  }
`;

// Append the script to the head of the HTML document
document.head.appendChild(jsEnabledScript);
```

However, a better approach would be:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* Add some basic styling to make the message more prominent */
    .js-disabled-message {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #FFC080;
      color: #333;
      text-align: center;
      padding: 1em;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <noscript>
    <div class="js-disabled-message">
      <p>JavaScript is disabled in your browser.</p>
      <p>Please enable JavaScript to use this website.</p>
    </div>
  </noscript>
  <script>
    // You can add your JavaScript code here
  </script>
</body>
</html>
```

This HTML code achieves the same result without the need for dynamically created elements. The `noscript` tag is a standard HTML tag that only displays its content when JavaScript is disabled.
