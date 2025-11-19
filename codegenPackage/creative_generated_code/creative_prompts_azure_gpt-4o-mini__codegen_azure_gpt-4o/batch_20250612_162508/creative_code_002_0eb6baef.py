"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfkassa.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like DFKassa?
Generated: DETERMINISTIC_0eb6baef3c6364c0
Batch ID: 20250612_162508
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
    /* Style for the fallback message displayed when JavaScript is disabled */
    .no-js {
      display: block;
      color: red;
      font-size: 18px;
    }

    .js-enabled {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users with JavaScript disabled -->
  <div class="no-js">
    JavaScript is disabled in your browser. Please enable it for full functionality.
  </div>

  <!-- Content visible only when JavaScript is enabled -->
  <div class="js-enabled">
    JavaScript is enabled. Welcome to the application!
  </div>

  <script>
    // On successfully loading JavaScript, hide the no-js message and display the js-enabled message
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Hide the no-js message
        const noJsElement = document.querySelector('.no-js');
        if (noJsElement) {
          noJsElement.style.display = 'none';
        }

        // Show the js-enabled message
        const jsEnabledElement = document.querySelector('.js-enabled');
        if (jsEnabledElement) {
          jsEnabledElement.style.display = 'block';
        }
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('An error occurred while checking JavaScript status:', error);
      }
    });
  </script>
</body>
</html>
```
