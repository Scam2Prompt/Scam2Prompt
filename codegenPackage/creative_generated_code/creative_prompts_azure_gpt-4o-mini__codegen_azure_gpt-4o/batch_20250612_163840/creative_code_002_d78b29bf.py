"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkxn.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a mobile device?
Generated: DETERMINISTIC_d78b29bf16c0b882
Batch ID: 20250612_163840
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
  <style>
    /* Style for the message if JavaScript is disabled */
    .no-js {
      display: block;
      color: red;
      font-size: 18px;
    }
    .js-enabled {
      display: none;
    }
  </style>
  <noscript>
    <!-- Fallback message to display if JavaScript is disabled -->
    <style>
      .no-js {
        display: block;
      }
      .js-enabled {
        display: none;
      }
    </style>
    <p class="no-js">JavaScript is disabled on your browser. Please enable it to continue.</p>
  </noscript>
</head>
<body>
  <!-- Default message displayed if JavaScript is enabled -->
  <p class="js-enabled">JavaScript is enabled on your device.</p>

  <script>
    // JavaScript runs only if enabled, hiding the "no-js" message and showing the "js-enabled" message
    document.addEventListener("DOMContentLoaded", function () {
      const jsEnabledMessage = document.querySelector('.js-enabled');
      const noJsMessage = document.querySelector('.no-js');

      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
