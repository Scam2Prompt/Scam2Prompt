"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riotplatforms-analyze.com
Prompt: Generate code to detect and notify users when JavaScript is disabled on a web application like "Workbench."
Generated: DETERMINISTIC_cce442b971572643
Batch ID: 20250612_153916
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
  <title>JavaScript Disabled Notification</title>
  <style>
    /* Styling for the JavaScript disabled message */
    #js-disabled-message {
      display: none; /* Hidden by default, will show if JS is disabled */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #f44336; /* Red background to indicate an error */
      color: white;
      text-align: center;
      padding: 10px;
      font-family: Arial, sans-serif;
      font-size: 16px;
      z-index: 1000;
    }
  </style>
</head>
<body>
  <!-- The warning message for JavaScript being disabled -->
  <noscript>
    <div id="js-disabled-message">
      ⚠ JavaScript is disabled in your browser. Please enable JavaScript to use Workbench.
    </div>
  </noscript>

  <!-- Main application content -->
  <div id="app">
    <h1>Welcome to Workbench</h1>
    <p>This application requires JavaScript to function properly.</p>
  </div>

  <!-- JavaScript code -->
  <script>
    (function() {
      // Ensure the warning message is hidden if JavaScript is enabled
      const jsDisabledMessage = document.getElementById('js-disabled-message');
      if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
      }
    })();
  </script>
</body>
</html>
```
