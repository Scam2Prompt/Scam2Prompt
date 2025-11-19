"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iron-oil.com
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_15713815df06a2aa
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML Code to check if JavaScript is enabled -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Enabled Checker</title>
  <style>
    /* Message for when JavaScript is disabled */
    .no-js-message {
      display: block;
      color: red;
      font-weight: bold;
    }

    /* JavaScript will hide this message */
    .js-enabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message that appears only if JavaScript is disabled -->
  <noscript>
    <p class="no-js-message">JavaScript is disabled in your browser. Please enable it to view this content.</p>
  </noscript>

  <!-- Message for when JavaScript is enabled -->
  <p class="js-enabled-message">JavaScript is enabled in your browser!</p>

  <script>
    // JavaScript to hide the disabled message and show the enabled message
    document.addEventListener("DOMContentLoaded", function () {
      try {
        // Select the elements
        var jsEnabledMessage = document.querySelector('.js-enabled-message');
        var noJsMessage = document.querySelector('.no-js-message');

        // Show "JavaScript is enabled" message
        if (jsEnabledMessage) {
          jsEnabledMessage.style.display = 'block';
        }

        // Hide "JavaScript is disabled" message
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        console.error("An error occurred while checking JavaScript status:", error);
      }
    });
  </script>
</body>
</html>
```
