"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hvneh.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_162217
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
  <title>Check JavaScript Enabled</title>
  <noscript>
    <!-- This message will display if JavaScript is disabled -->
    <style>
      .js-enabled { display: none; }
      .no-js { display: block; color: red; font-weight: bold; }
    </style>
    <div class="no-js">JavaScript is disabled in your browser. Please enable it for full functionality.</div>
  </noscript>
  <script>
    // This script will hide the no-js message and show the js-enabled content
    document.addEventListener("DOMContentLoaded", function () {
      const noJsMessage = document.querySelector('.no-js');
      const jsEnabledMessage = document.querySelector('.js-enabled');
      
      // Hide the no-js message
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
      
      // Show the js-enabled message
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>
</head>
<body>
  <div class="no-js">JavaScript is disabled in your browser.</div>
  <div class="js-enabled" style="display: none;">JavaScript is enabled and working correctly!</div>
</body>
</html>
```
