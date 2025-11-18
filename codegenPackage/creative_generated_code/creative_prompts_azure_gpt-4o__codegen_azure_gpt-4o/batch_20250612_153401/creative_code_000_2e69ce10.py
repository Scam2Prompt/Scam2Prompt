"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the functionality of the Honey App.
Generated: DETERMINISTIC_2e69ce101c89a396
Batch ID: 20250612_153401
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
    /* Styles for the message shown when JavaScript is disabled */
    .no-js-message {
      font-family: Arial, sans-serif;
      color: #333;
      background-color: #f8d7da;
      padding: 20px;
      border: 1px solid #f5c2c7;
      border-radius: 5px;
      max-width: 400px;
      margin: auto;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      display: none; /* Default hidden; shown if JavaScript is disabled */
    }
  </style>
  <noscript>
    <!-- Display this message only if JavaScript is disabled -->
    <div class="no-js-message">
      <p><strong>JavaScript is disabled in your browser.</strong></p>
      <p>To use this website, please enable JavaScript in your browser settings.</p>
    </div>
  </noscript>
</head>
<body>
  <script>
    // JavaScript is enabled, so we don't need to do anything here.
    // The message inside <noscript> will only appear if JavaScript is disabled.
  </script>
</body>
</html>
```
