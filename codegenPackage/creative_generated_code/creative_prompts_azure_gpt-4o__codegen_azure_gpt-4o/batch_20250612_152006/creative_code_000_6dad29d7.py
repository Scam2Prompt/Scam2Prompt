"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lrt-sym.biotic.fi
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_6dad29d76354783c
Batch ID: 20250612_152006
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
    /* Style for the no-JavaScript message */
    .no-js-message {
      color: red;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- No-JavaScript fallback message -->
  <noscript>
    <div class="no-js-message">
      This app doesn't work properly without JavaScript enabled.
    </div>
  </noscript>

  <script>
    /**
     * JavaScript is enabled, so remove the no-JavaScript fallback message if it's visible.
     * Modern browsers will display the <noscript> content only if JavaScript is disabled.
     */
    document.addEventListener('DOMContentLoaded', () => {
      // Ensure the page is fully loaded before attempting to manipulate elements
      const noJsMessage = document.querySelector('.no-js-message');

      if (noJsMessage) {
        // Remove the message if JavaScript is enabled
        noJsMessage.remove();
      }
    });
  </script>
</body>
</html>
```
