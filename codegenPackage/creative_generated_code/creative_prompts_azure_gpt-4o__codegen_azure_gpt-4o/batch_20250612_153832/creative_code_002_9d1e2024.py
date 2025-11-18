"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defia.cc
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a custom message for "mining-h5."
Generated: DETERMINISTIC_9d1e20247c002709
Batch ID: 20250612_153832
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Style for the fallback message when JavaScript is disabled */
    .no-js-message {
      display: none; /* Initially hidden, will be shown if JavaScript is disabled */
      padding: 20px;
      background-color: #ffcccb;
      color: #333;
      text-align: center;
      font-size: 1.2em;
      border: 1px solid #f5c2c7;
      margin: 20px auto;
      width: 90%;
      max-width: 600px;
    }
  </style>
</head>
<body>
  <!-- Fallback message when JavaScript is disabled -->
  <div class="no-js-message">JavaScript is disabled in your browser. "mining-h5" requires JavaScript to function properly.</div>

  <!-- Content that requires JavaScript -->
  <div id="app">
    <p>Welcome to Mining-H5!</p>
    <!-- More app content here -->
  </div>

  <script>
    // Ensure the fallback message is hidden when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message as JavaScript is enabled
      }
    });
  </script>

  <!-- NoScript fallback for browsers with JavaScript disabled -->
  <noscript>
    <style>
      /* Show the fallback message if JavaScript is disabled */
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>
</body>
</html>
```
