"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-pay.starpay.top
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior on the Starpay payment platform.
Generated: DETERMINISTIC_ffe81572003caf37
Batch ID: 20250612_155037
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
      display: none; /* Hidden by default, shown if JavaScript is disabled */
      color: red;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- The fallback message will be displayed only if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to continue using this platform.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="app">
    <h1>Welcome to Starpay</h1>
    <p>Your payment gateway.</p>
  </div>

  <script>
    // Ensure the message is hidden when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Find and hide the no-JavaScript message in case it was shown due to noscript fallback
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });

    // Additional JavaScript actions can be added here
    console.log('JavaScript is enabled.');
  </script>
</body>
</html>
```
