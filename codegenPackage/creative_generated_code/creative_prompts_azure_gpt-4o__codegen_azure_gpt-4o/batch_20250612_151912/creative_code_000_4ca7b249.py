"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raiden.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the Raiden Online domain details page.
Generated: DETERMINISTIC_4ca7b2495ee4ca9e
Batch ID: 20250612_151912
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
  <title>Enable JavaScript</title>
  <style>
    /* Simple styling for the message */
    .no-js-message {
      font-family: Arial, sans-serif;
      font-size: 16px;
      color: red;
      text-align: center;
      margin-top: 50px;
    }
  </style>
</head>
<body>
  <!-- Default message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to view this website correctly.
    </div>
  </noscript>

  <script>
    // This script runs only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Clear any warnings or messages since JavaScript is enabled
      const noJsElements = document.querySelectorAll('.no-js-message');
      if (noJsElements.length > 0) {
        noJsElements.forEach(element => element.remove());
      }

      // Additional functionality can be added here, if needed
      console.log('JavaScript is enabled.');
    });
  </script>
</body>
</html>
```
