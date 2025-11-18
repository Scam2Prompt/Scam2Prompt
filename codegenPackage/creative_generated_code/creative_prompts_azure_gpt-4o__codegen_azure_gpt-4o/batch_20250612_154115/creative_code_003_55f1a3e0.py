"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Generate HTML and JavaScript code for a webpage that displays a warning message when JavaScript is disabled, similar to the behavior described on https://monada.online.
Generated: DETERMINISTIC_55f1a3e0e4bd3d53
Batch ID: 20250612_154115
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
  <title>JavaScript Warning</title>
  <style>
    /* Style for the warning message */
    .no-js-warning {
      display: none; /* Initially hidden when JavaScript is enabled */
      background-color: #ffcccb;
      color: #000;
      padding: 15px;
      border: 1px solid #f00;
      text-align: center;
      font-family: Arial, sans-serif;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 9999;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <!-- Warning message to be displayed when JavaScript is disabled -->
  <noscript>
    <div class="no-js-warning">
      Warning: JavaScript is disabled. This site requires JavaScript to function properly.
    </div>
  </noscript>

  <!-- Example content -->
  <h1>Welcome to the webpage!</h1>
  <p>This page works best with JavaScript enabled.</p>

  <script>
    // JavaScript code to ensure the warning does not appear if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Remove any warning divs in case JavaScript is enabled
      const warnings = document.querySelectorAll('.no-js-warning');
      warnings.forEach(warning => {
        warning.style.display = 'none';
      });
    });
  </script>
</body>
</html>
```
