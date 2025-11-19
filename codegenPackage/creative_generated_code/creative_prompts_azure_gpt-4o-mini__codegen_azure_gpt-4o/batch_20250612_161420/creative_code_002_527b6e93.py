"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visit-echo.pages.dev
Prompt: Can you provide a code snippet that demonstrates how to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_527b6e93746eb1a8
Batch ID: 20250612_161420
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
    /* Default styling assumes JavaScript is disabled */
    #js-disabled-message {
      display: block;
      color: red;
      font-weight: bold;
    }

    #js-enabled-message {
      display: none;
      color: green;
      font-weight: bold;
    }
  </style>
  <noscript>
    <!-- Fallback message if JavaScript is disabled -->
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
  <!-- Message indicating JavaScript is disabled -->
  <div id="js-disabled-message">JavaScript is disabled in your browser.</div>

  <!-- Message indicating JavaScript is enabled -->
  <div id="js-enabled-message">JavaScript is enabled in your browser.</div>

  <script>
    // JavaScript code runs only if JavaScript is enabled in the browser
    document.addEventListener('DOMContentLoaded', () => {
      // Hide the "JavaScript Disabled" message
      const jsDisabledMessage = document.getElementById('js-disabled-message');
      if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
      }

      // Show the "JavaScript Enabled" message
      const jsEnabledMessage = document.getElementById('js-enabled-message');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
