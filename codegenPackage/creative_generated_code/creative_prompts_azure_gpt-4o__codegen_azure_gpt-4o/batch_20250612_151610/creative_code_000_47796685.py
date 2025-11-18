"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on https://blur.si.
Generated: DETERMINISTIC_477966857459a23d
Batch ID: 20250612_151610
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
      display: none; /* Default to hidden; shown only if JS is disabled */
      color: red;
      font-size: 1.2em;
      text-align: center;
      margin-top: 20px;
    }

    /* Fallback for browsers with JavaScript disabled */
    noscript .no-js-message {
      display: block; /* Ensure the message is visible when JS is disabled */
    }
  </style>
</head>
<body>
  <!-- Message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      <strong>JavaScript is disabled in your browser. Please enable it for the best experience.</strong>
    </div>
  </noscript>

  <!-- Message for users with JavaScript enabled -->
  <div id="js-enabled-message" style="display: none; text-align: center; margin-top: 20px;">
    <strong>JavaScript is enabled in your browser. Thanks for visiting our site!</strong>
  </div>

  <script>
    // JavaScript to dynamically show the "JavaScript enabled" message
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Select the JS-enabled message element
        const jsEnabledMessage = document.getElementById('js-enabled-message');

        // Display the message if JS is enabled
        if (jsEnabledMessage) {
          jsEnabledMessage.style.display = 'block';
        }
      } catch (error) {
        // Error handling (unlikely for this simple logic)
        console.error('An error occurred while displaying the JavaScript-enabled message:', error);
      }
    });
  </script>
</body>
</html>
```
