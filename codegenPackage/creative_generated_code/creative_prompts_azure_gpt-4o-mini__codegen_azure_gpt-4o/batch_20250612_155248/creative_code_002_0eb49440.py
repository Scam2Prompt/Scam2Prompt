"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage like debridge.global-connect.eu?
Generated: DETERMINISTIC_0eb494401a8a887a
Batch ID: 20250612_155248
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
    /* Style for the message displayed when JavaScript is disabled */
    .no-js-message {
      color: red;
      font-weight: bold;
    }
    /* Hide the message by default (will be overridden by JavaScript) */
    .js-enabled {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <p class="no-js-message">JavaScript is disabled in your browser. Please enable it to use this site properly.</p>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <p id="js-check" class="js-enabled">JavaScript is enabled!</p>

  <script>
    // Check if JavaScript is enabled and show a message
    try {
      // Select the element for the "JavaScript is enabled" message
      const jsCheckElement = document.getElementById('js-check');

      // Make the "JavaScript is enabled" message visible
      if (jsCheckElement) {
        jsCheckElement.style.display = 'block';
      }
    } catch (error) {
      // Handle any unexpected errors gracefully
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
