"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fyatlux.com
Prompt: How do I check if JavaScript is enabled in my browser settings?
Generated: DETERMINISTIC_c42c3f021123be5e
Batch ID: 20250612_161616
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
    /* Default message for users with JavaScript disabled */
    #js-disabled-message {
      display: block;
      color: red;
      font-weight: bold;
    }
    /* Hide the disabled message when JavaScript is enabled */
    .js-enabled #js-disabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <div id="js-disabled-message">
    JavaScript is disabled in your browser settings.
  </div>

  <!-- Content shown if JavaScript is enabled -->
  <div id="js-enabled-message" style="display: none;">
    JavaScript is enabled in your browser settings.
  </div>

  <script>
    /*
      This script dynamically modifies the DOM to check if JavaScript is enabled.
    */
    (function () {
      try {
        // Add a class to the <body> to indicate JavaScript is enabled
        document.body.classList.add('js-enabled');

        // Show the message for users with JavaScript enabled
        const jsEnabledMessage = document.getElementById('js-enabled-message');
        if (jsEnabledMessage) {
          jsEnabledMessage.style.display = 'block';
        }
      } catch (error) {
        // Handle any errors gracefully
        console.error('Error while checking JavaScript status:', error);
      }
    })();
  </script>
</body>
</html>
```
