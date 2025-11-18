"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proxycare.proxurve.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it for accessing the N-central login page.
Generated: DETERMINISTIC_fa07b7181a135267
Batch ID: 20250612_155002
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
  <title>N-central Login</title>
  <style>
    /* Basic styling for the message */
    #no-js-message {
      display: none; /* Hidden by default */
      color: red;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Content for users with JavaScript -->
  <div id="content">
    <h1>Welcome to the N-central Login Page</h1>
    <p>Please proceed with your login.</p>
  </div>

  <!-- Message that will only appear if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      It appears that JavaScript is disabled in your browser. Please enable JavaScript to access the N-central login page.
    </div>
  </noscript>

  <script>
    // Ensure JavaScript-enabled users never see the no-js message
    // This script runs only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Ensures message is hidden even if noscript tag is used
      }
    });
  </script>
</body>
</html>
```
