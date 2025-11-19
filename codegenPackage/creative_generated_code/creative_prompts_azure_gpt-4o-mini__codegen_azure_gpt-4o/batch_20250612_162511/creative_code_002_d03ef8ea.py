"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.heheepro.com
Prompt: Can you provide a code snippet to detect if JavaScript is enabled in a web application like HEHEE Pro?
Generated: DETERMINISTIC_d03ef8ea188bd2b7
Batch ID: 20250612_162511
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
    /* Default message for when JavaScript is disabled */
    .js-disabled {
      display: block;
      color: red;
      font-weight: bold;
    }

    .js-enabled {
      display: none;
      color: green;
      font-weight: bold;
    }
  </style>
</head>

<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <p class="js-disabled">JavaScript is disabled. Please enable it for full functionality.</p>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <div class="js-enabled">JavaScript is enabled!</div>

  <script>
    // When JavaScript runs, toggle visibility to show the "enabled" message
    (function () {
      try {
        // Select the elements
        const jsEnabledMessage = document.querySelector('.js-enabled');
        const jsDisabledMessage = document.querySelector('.js-disabled');

        // Ensure the 'enabled' message is visible and 'disabled' message is hidden
        if (jsEnabledMessage && jsDisabledMessage) {
          jsEnabledMessage.style.display = 'block';
          jsDisabledMessage.style.display = 'none';
        }
      } catch (error) {
        console.error('An error occurred while detecting JavaScript:', error);
      }
    })();
  </script>
</body>

</html>
```
