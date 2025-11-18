"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Write code for a JavaScript snippet that displays a custom error message when JavaScript is disabled, similar to the behavior described on the DogeAI website.
Generated: DETERMINISTIC_3eae712e5a38d7ae
Batch ID: 20250612_154312
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
  <title>JavaScript Disabled Message</title>
  <style>
    /* Style for the warning message */
    .no-js-warning {
      display: none; /* Hidden by default, will display when JavaScript is disabled */
      color: #fff;
      background-color: #ff0000; /* Red warning background */
      padding: 16px;
      text-align: center;
      font-size: 16px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <!-- This message will be displayed if JavaScript is disabled -->
  <div class="no-js-warning" id="no-js-warning">
    Warning: This site requires JavaScript to function properly. Please enable JavaScript in your browser settings.
  </div>

  <script>
    // JavaScript is enabled, so hide the warning message
    document.addEventListener('DOMContentLoaded', () => {
      const warningElement = document.getElementById('no-js-warning');
      if (warningElement) {
        warningElement.style.display = 'none'; // Ensure message is hidden
      }
    });
  </script>

  <!-- Noscript fallback message for browsers with JavaScript disabled -->
  <noscript>
    <style>
      /* Override the hidden style for the message when JavaScript is disabled */
      .no-js-warning {
        display: block; /* Show warning if JavaScript is disabled */
      }
    </style>
  </noscript>
</body>
</html>
```
