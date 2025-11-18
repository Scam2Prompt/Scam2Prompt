"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fjvybl.cc
Prompt: Write a script that checks if JavaScript is enabled in a user's browser and displays a message similar to CoinCarp's notification.
Generated: DETERMINISTIC_7a0ebfbebc1b8e3f
Batch ID: 20250612_154001
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
    /* Default styling for the no-JavaScript message */
    .no-js-message {
      display: block;
      padding: 20px;
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      font-size: 16px;
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px auto;
      max-width: 500px;
    }

    /* Hide the message when JavaScript is enabled */
    .js-enabled .no-js-message {
      display: none;
    }
  </style>
  <noscript>
    <!-- Message to display if JavaScript is disabled -->
    <div class="no-js-message">
      JavaScript is disabled in your browser. For the best experience, please enable JavaScript.
    </div>
  </noscript>
</head>
<body>
  <!-- Main content container -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This content will be enhanced when JavaScript is enabled.</p>
  </div>

  <script>
    // Check if JavaScript is enabled
    // Add a class to the <body> to indicate JavaScript is enabled
    try {
      document.body.classList.add('js-enabled');
    } catch (error) {
      console.error('An error occurred while checking JavaScript status:', error);
    }
  </script>
</body>
</html>
```
