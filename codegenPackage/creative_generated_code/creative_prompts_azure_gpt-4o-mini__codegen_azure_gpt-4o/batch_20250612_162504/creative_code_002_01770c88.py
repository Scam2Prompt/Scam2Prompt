"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytest.vercel.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Claytest?
Generated: DETERMINISTIC_01770c8835b5f52e
Batch ID: 20250612_162504
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
  <title>JavaScript Check</title>
  <style>
    /* Default message indicating JavaScript is disabled */
    .no-js {
      display: block;
      color: red;
      font-weight: bold;
    }
    .js-enabled {
      display: none;
    }
  </style>
  <script>
    // If JavaScript is enabled, toggle visibility of elements
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.querySelector('.no-js');
      const jsEnabledMessage = document.querySelector('.js-enabled');

      if (noJsMessage && jsEnabledMessage) {
        noJsMessage.style.display = 'none'; // Hide "JavaScript Disabled" message
        jsEnabledMessage.style.display = 'block'; // Show "JavaScript Enabled" message
      }
    });
  </script>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <div class="no-js">
    JavaScript is disabled or not supported in your browser. Please enable it for better user experience.
  </div>

  <!-- Message shown if JavaScript is enabled -->
  <div class="js-enabled">
    JavaScript is enabled! Enjoy your experience on this web application.
  </div>
</body>
</html>
```
