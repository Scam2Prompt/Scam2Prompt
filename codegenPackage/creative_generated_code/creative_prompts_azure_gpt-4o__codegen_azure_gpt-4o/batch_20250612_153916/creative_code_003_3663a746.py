"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-dex-contest-nine.vercel.app
Prompt: Write code to check if JavaScript is enabled in a user's browser and display a message if it is disabled.
Generated: DETERMINISTIC_3663a7465a0d4b14
Batch ID: 20250612_153916
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
    /* Default message for browsers without JavaScript enabled */
    .no-js-message {
      display: block;
      color: red;
      font-weight: bold;
    }
    .js-message {
      display: none; /* Hidden by default, only shown if JavaScript is enabled */
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to view this site properly.
    </div>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <div id="js-enabled-message" class="js-message">
    JavaScript is enabled in your browser!
  </div>

  <script>
    // Select the message element and make it visible if JavaScript is enabled
    try {
      const jsEnabledMessage = document.getElementById('js-enabled-message');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block'; // Show the JavaScript-enabled message
      }
    } catch (error) {
      console.error('An error occurred while checking JavaScript:', error);
    }
  </script>
</body>
</html>
```
