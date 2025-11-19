"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcqoo.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a mobile browser for accessing BTC Pledge?
Generated: DETERMINISTIC_7d456bddacea7a1e
Batch ID: 20250612_155457
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
  <title>BTC Pledge - JavaScript Check</title>
  <style>
    /* Fallback message styling */
    .js-disabled {
      display: none;
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
    .js-enabled {
      display: none;
      color: green;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <script>
    // Inline script to detect JavaScript support
    document.addEventListener("DOMContentLoaded", () => {
      // Show JavaScript-enabled message and hide fallback message
      const jsEnabledMessage = document.querySelector('.js-enabled');
      const jsDisabledMessage = document.querySelector('.js-disabled');
      if (jsEnabledMessage && jsDisabledMessage) {
        jsEnabledMessage.style.display = 'block';
        jsDisabledMessage.style.display = 'none';
      }
    });
  </script>
</head>
<body>
  <!-- Fallback message for browsers with JavaScript disabled -->
  <noscript>
    <div class="js-disabled">
      JavaScript is disabled in your browser. Please enable it to access BTC Pledge.
    </div>
  </noscript>

  <!-- Message for browsers with JavaScript enabled -->
  <div class="js-enabled">
    JavaScript is enabled in your browser. You can access BTC Pledge.
  </div>
</body>
</html>
```
