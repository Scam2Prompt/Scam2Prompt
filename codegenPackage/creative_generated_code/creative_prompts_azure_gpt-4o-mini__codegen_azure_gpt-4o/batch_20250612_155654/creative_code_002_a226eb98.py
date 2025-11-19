"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eleganthotel-su.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_155654
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
    /* Style to show a message if JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default since JavaScript will enable dynamic content */
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <!-- Message shown only if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is not enabled in your browser. Please enable it to continue.
    </div>
  </noscript>

  <!-- Content to show if JavaScript is enabled -->
  <div id="js-enabled-message" style="display: none;">
    JavaScript is enabled in your browser! You can proceed.
  </div>

  <script>
    // On page load, show the JavaScript-enabled message
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Locate the element to display the message
        const jsEnabledMessage = document.getElementById('js-enabled-message');
        
        // Ensure the element exists before manipulation
        if (jsEnabledMessage) {
          jsEnabledMessage.style.display = 'block'; // Show the message
        } else {
          console.error('JavaScript-enabled message element not found.');
        }
      } catch (error) {
        // Log errors for debugging purposes
        console.error('An error occurred while checking for JavaScript:', error);
      }
    });
  </script>

</body>
</html>
```
