"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the cPanel Webmail login page.
Generated: DETERMINISTIC_00e6b5fd5c1bd52d
Batch ID: 20250612_154651
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
  <title>JavaScript Disabled Warning</title>
  <style>
    /* Styles for the warning message */
    #js-warning {
      display: none; /* Initially hidden, will be shown if JS is disabled */
      background-color: #ffcccb;
      color: #000;
      padding: 10px;
      border: 1px solid #d9534f;
      font-family: Arial, sans-serif;
      font-size: 16px;
      text-align: center;
      margin: 20px;
    }
  </style>
  <noscript>
    <!-- Fallback content displayed when JavaScript is disabled -->
    <div id="js-warning">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>
</head>
<body>
  <div id="content">
    <!-- Main content of the website -->
    <h1>Welcome to the website</h1>
    <p>This is the main content of the page.</p>
  </div>
  <script>
    // Ensure that the warning message is not displayed when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      // Select the warning message element
      const jsWarning = document.getElementById('js-warning');

      // Check if the element exists and hide it (precautionary cleanup)
      if (jsWarning) {
        jsWarning.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
