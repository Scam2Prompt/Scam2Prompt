"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.eu
Prompt: Can you provide code snippets to check if JavaScript is enabled in a browser?
Generated: DETERMINISTIC_4dc0daab1549b7bd
Batch ID: 20250612_155840
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* Hide the "JavaScript is disabled" message by default */
    #js-disabled-message {
      display: none;
      color: red;
      font-weight: bold;
    }
  </style>
  <noscript>
    <!-- Display a message if JavaScript is disabled -->
    <style>
      #js-disabled-message {
        display: block;
      }
      #js-enabled-message {
        display: none;
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Message for JavaScript being disabled -->
  <p id="js-disabled-message">JavaScript is disabled in your browser. Please enable JavaScript for a better experience.</p>

  <!-- Message for JavaScript being enabled -->
  <p id="js-enabled-message">JavaScript is enabled!</p>

  <script>
    // Ensure the "JavaScript is enabled" message is displayed (in case of rare edge cases)
    window.addEventListener('load', function () {
      const jsEnabledMessage = document.getElementById('js-enabled-message');
      const jsDisabledMessage = document.getElementById('js-disabled-message');

      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }

      if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
