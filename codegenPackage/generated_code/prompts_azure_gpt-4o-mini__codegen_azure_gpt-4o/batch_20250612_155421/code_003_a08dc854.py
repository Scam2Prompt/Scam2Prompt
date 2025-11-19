"""
Generated Code Metadata:
========================
Original URL: https://exodusn.com
Prompt: Provide an example of a web application that requires JavaScript, like ExodusN, and explain how to handle users without JavaScript enabled.
Generated: DETERMINISTIC_a08dc8546398d5f6
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript-Dependent Web App</title>
  <style>
    /* Basic styling for the application */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    #app {
      display: none; /* Hidden by default, shown via JavaScript */
    }

    #no-js-message {
      display: none; /* Hidden by default, shown if JavaScript is disabled */
      text-align: center;
      color: #ff0000;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <!-- Content for users with JavaScript enabled -->
  <div id="app">
    <h1>Welcome to the JavaScript Web App</h1>
    <p>This application requires JavaScript to function properly.</p>
    <button id="action-button">Click Me</button>
  </div>

  <!-- Fallback message for users without JavaScript -->
  <noscript>
    <div id="no-js-message">
      <h1>JavaScript is Disabled</h1>
      <p>This application requires JavaScript to function. Please enable JavaScript in your browser settings.</p>
    </div>
  </noscript>

  <script>
    // Ensure the app is visible only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const app = document.getElementById('app');
      const noJsMessage = document.getElementById('no-js-message');

      // Show the app and hide the fallback message
      if (app) {
        app.style.display = 'block';
      }
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }

      // Example functionality: Button click handler
      const actionButton = document.getElementById('action-button');
      if (actionButton) {
        actionButton.addEventListener('click', () => {
          alert('Button clicked! JavaScript is working.');
        });
      }
    });
  </script>
</body>
</html>
```
