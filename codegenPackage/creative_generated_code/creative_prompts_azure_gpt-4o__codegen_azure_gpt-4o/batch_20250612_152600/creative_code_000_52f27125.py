"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlast.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a warning message, similar to the behavior described on the ETH Pledge website.
Generated: DETERMINISTIC_52f271250ab965a0
Batch ID: 20250612_152600
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
  <title>JavaScript Detection</title>
  <style>
    /* Style for the warning message */
    #js-warning {
      display: none; /* Hidden by default */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ffcccb;
      color: #000;
      text-align: center;
      padding: 10px;
      font-size: 16px;
      z-index: 9999;
    }
  </style>
  <noscript>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <style>
      #js-warning { display: block; }
    </style>
  </noscript>
</head>
<body>
  <!-- Warning message container -->
  <div id="js-warning">
    Warning: JavaScript is disabled in your browser. This website may not function properly.
  </div>

  <script>
    // Ensure the warning is hidden if JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      try {
        // Get the warning message element
        const jsWarning = document.getElementById('js-warning');
        if (jsWarning) {
          // Hide the warning message if JavaScript is enabled
          jsWarning.style.display = 'none';
        }
      } catch (error) {
        console.error('Error while hiding JavaScript warning:', error);
      }
    });
  </script>
</body>
</html>
```
