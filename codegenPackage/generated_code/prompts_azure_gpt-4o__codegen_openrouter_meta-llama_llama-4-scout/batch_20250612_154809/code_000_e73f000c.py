"""
Generated Code Metadata:
========================
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the behavior described on coinbase.co.za.
Generated: DETERMINISTIC_e73f000cf34e9737
Batch ID: 20250612_154809
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
    /* Style the noscript container to take up full width and height */
    .js-disabled {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
  </style>
  <div class="js-disabled">
    <h1>JavaScript is Disabled</h1>
    <p>Please enable JavaScript in your browser to use this website.</p>
  </div>
`;

// Append the noscript element to the body
document.body.appendChild(noscriptElement);

// Create a script to detect if JavaScript is enabled
const jsEnabledScript = document.createElement('script');
jsEnabledScript.innerHTML = `
  // Remove the noscript element when JavaScript is enabled
  document.addEventListener('DOMContentLoaded', function() {
    const noscriptElement = document.querySelector('noscript');
    if (noscriptElement) {
      noscriptElement.remove();
    }
  });
`;

// Append the script to the head
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
  <title>JavaScript Detection</title>
  <style>
    /* Style the js-disabled container to take up full width and height */
    .js-disabled {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
  </style>
</head>
<body>
  <noscript>
    <div class="js-disabled">
      <h1>JavaScript is Disabled</h1>
      <p>Please enable JavaScript in your browser to use this website.</p>
    </div>
  </noscript>
  <script>
    // No need for any JavaScript code here
  </script>
</body>
</html>
```
