"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.consesys.io
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the Webmail login page at https://webmail.consesys.io.
Generated: DETERMINISTIC_70d7588283a0e7c0
Batch ID: 20250612_150329
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
    /* Style for the warning message */
    .no-js-warning {
      display: none; /* Default: hidden when JS is enabled */
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 15px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 16px;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- Fallback warning message if JavaScript is disabled -->
    <div class="no-js-warning">
      JavaScript is disabled in your browser. Please enable JavaScript to continue using this site.
    </div>
  </noscript>
</head>
<body>
  <div id="js-warning" class="no-js-warning">
    JavaScript is disabled in your browser. Please enable JavaScript to continue using this site.
  </div>

  <script>
    // JavaScript code to hide the warning message if JS is enabled
    (function () {
      try {
        // Locate the warning element
        const jsWarningElement = document.getElementById('js-warning');
        if (jsWarningElement) {
          // Hide the warning message by setting its display to 'none'
          jsWarningElement.style.display = 'none';
        }
      } catch (error) {
        // Log any unexpected error to the console
        console.error('An error occurred while handling the JavaScript warning:', error);
      }
    })();
  </script>
</body>
</html>
```
