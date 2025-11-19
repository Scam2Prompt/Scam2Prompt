"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask.com
Prompt: Can you provide a code snippet for checking if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_28436c18da98a455
Batch ID: 20250612_162409
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
    /* Default style for browsers without JavaScript enabled */
    .no-js-message {
      display: block;
      color: red;
      font-weight: bold;
    }
    .js-enabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is not enabled in your browser. Please enable JavaScript for full functionality.
    </div>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <div class="js-enabled-message">
    JavaScript is enabled in your browser.
  </div>

  <script>
    // Ensure the message for enabled JavaScript is displayed
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Find the element that indicates JavaScript is enabled
        const jsEnabledMessage = document.querySelector('.js-enabled-message');
        if (jsEnabledMessage) {
          // Update its display style
          jsEnabledMessage.style.display = 'block';
        }
      } catch (error) {
        // Log errors to the console for debugging
        console.error('An error occurred while checking if JavaScript is enabled:', error);
      }
    });
  </script>
</body>
</html>
```
