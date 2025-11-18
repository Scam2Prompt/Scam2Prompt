"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the behavior described on the mtec.cyou webpage.
Generated: DETERMINISTIC_82b48da5070ed64e
Batch ID: 20250612_150446
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
    /* Styling for the warning message */
    .no-js-message {
      display: none; /* Hidden by default */
      color: white;
      background-color: red;
      padding: 15px;
      text-align: center;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Warning message shown if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>
  </noscript>

  <script>
    // JavaScript is enabled, so we ensure the <noscript> fallback is not visible
    // This script is only executed if JavaScript is enabled
    (function() {
      // Attempt to look for the no-js-message element to handle any edge cases
      try {
        const noJsMessage = document.querySelector('.no-js-message');
        if (noJsMessage) {
          noJsMessage.style.display = 'none'; // Hide the fallback message
        }
      } catch (error) {
        console.error("Error handling the no-js message:", error);
      }
    })();
  </script>
</body>
</html>
```
