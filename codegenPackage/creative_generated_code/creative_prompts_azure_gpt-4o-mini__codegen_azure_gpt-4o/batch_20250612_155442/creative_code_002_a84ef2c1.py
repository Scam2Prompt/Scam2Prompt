"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for cPanel compatibility?
Generated: DETERMINISTIC_a84ef2c195a19f86
Batch ID: 20250612_155442
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
    /* Default message displayed if JavaScript is disabled */
    .js-disabled {
      display: block;
      color: red;
      font-weight: bold;
    }
    .js-enabled {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <p class="js-disabled">JavaScript is disabled in your browser. Please enable JavaScript for full compatibility with cPanel.</p>
  </noscript>

  <!-- Message displayed if JavaScript is enabled -->
  <p id="js-enabled" class="js-enabled">JavaScript is enabled in your browser. You are good to go!</p>

  <script>
    // Use JavaScript to dynamically show the "enabled" message
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Select the enabled message element
        const enabledMessage = document.getElementById('js-enabled');
        if (enabledMessage) {
          enabledMessage.style.display = 'block'; // Show the message
        }

        // Optionally hide the disabled message if desired
        const disabledMessage = document.querySelector('.js-disabled');
        if (disabledMessage) {
          disabledMessage.style.display = 'none'; // Hide the message
        }
      } catch (error) {
        console.error('An error occurred while checking JavaScript status:', error);
      }
    });
  </script>
</body>
</html>
```
