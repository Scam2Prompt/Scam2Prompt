"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-application5.pages.dev
Prompt: Write a code snippet to check if JavaScript is enabled in a user's browser.
Generated: DETERMINISTIC_a5de3b4f10d56156
Batch ID: 20250612_164319
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
    /* This message will show if JavaScript is disabled */
    .no-js-message {
      display: none;
      color: red;
      font-weight: bold;
    }

    /* JavaScript will hide this message */
    .js-enabled-message {
      display: none;
      color: green;
      font-weight: bold;
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>
</head>
<body>

  <!-- Message for JavaScript-disabled browsers -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable it to access full functionality.
  </div>

  <!-- Message for JavaScript-enabled browsers -->
  <div class="js-enabled-message">
    JavaScript is enabled in your browser!
  </div>

  <script>
    // When JavaScript is enabled, hide the no-JS message and show the JS-enabled message
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.querySelector('.no-js-message');
      const jsEnabledMessage = document.querySelector('.js-enabled-message');

      // Hide the no-JS message
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }

      // Show the JS-enabled message
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>

</body>
</html>
```
