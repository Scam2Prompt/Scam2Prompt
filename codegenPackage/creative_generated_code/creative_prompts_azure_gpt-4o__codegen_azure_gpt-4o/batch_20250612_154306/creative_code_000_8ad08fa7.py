"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as suggested by the functionality described on the Step App domain page.
Generated: DETERMINISTIC_8ad08fa70cebd9a2
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Styling for the JavaScript disabled message */
    #js-disabled-message {
      display: none; /* Hide the message by default */
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message for users if JavaScript is disabled -->
  <noscript>
    <div id="js-disabled-message">
      JavaScript is disabled in your browser. Please enable it to fully use this website.
    </div>
  </noscript>

  <!-- Main content of the page -->
  <h1>Welcome to the Step App Page!</h1>
  <p>Enjoy exploring the functionalities offered here.</p>

  <script>
    // JavaScript code runs only if JavaScript is enabled in the browser
    document.addEventListener('DOMContentLoaded', () => {
      // Locate the JavaScript disabled message element
      const jsDisabledMessage = document.getElementById('js-disabled-message');

      // Ensure the message is hidden (should already be hidden by CSS)
      if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
      }

      // Additional logic for your app can be added here
    });

    // Error handling - ensure the script runs safely
    try {
      console.log('JavaScript is enabled in this browser.');
    } catch (error) {
      console.error('An error occurred:', error);
    }
  </script>
</body>
</html>
```
