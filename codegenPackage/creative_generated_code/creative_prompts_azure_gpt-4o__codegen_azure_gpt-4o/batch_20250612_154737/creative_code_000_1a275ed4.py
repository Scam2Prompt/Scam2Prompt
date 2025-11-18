"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc106.d952.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the behavior of the "mining-h5" platform.
Generated: DETERMINISTIC_1a275ed4cb105c5d
Batch ID: 20250612_154737
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
  <title>JavaScript Disabled Detector</title>
  <style>
    /* Style for the message displayed when JavaScript is disabled */
    .no-js-message {
      display: none;
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <script>
    // JavaScript code to remove the "no-js-message" if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message since JS is enabled
      }
    });
  </script>
</head>
<body>
  <!-- This message will only be visible if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message" class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to continue using this platform.
    </div>
  </noscript>

  <!-- Content of your website -->
  <div id="app">
    <h1>Welcome to the Platform!</h1>
    <p>This platform requires JavaScript to function properly.</p>
  </div>
</body>
</html>
```
