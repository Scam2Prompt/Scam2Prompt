"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Provide a code snippet to display a message prompting users to enable JavaScript when visiting imseoa.com on mobile.
Generated: DETERMINISTIC_444eb1ac0c204144
Batch ID: 20250612_163840
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
    /* Basic styles for the message */
    .no-js-message {
      display: none; /* Hidden by default, only displayed if JS is disabled */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 10px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 14px;
      z-index: 9999;
    }
  </style>
</head>
<body>
  <!-- Message shown only if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      Please enable JavaScript to fully experience imseoa.com on your mobile device.
    </div>
  </noscript>

  <!-- Main content of the website -->
  <div id="content">
    <h1>Welcome to imseoa.com</h1>
    <p>Enjoy exploring our features!</p>
  </div>

  <script>
    // Mobile detection logic
    (function () {
      // Check if the user is on a mobile device
      const isMobile = /Mobi|Android/i.test(navigator.userAgent);

      if (isMobile) {
        // Display a mobile-specific message if needed (JavaScript enabled scenario)
        console.log("JavaScript is enabled. Enjoy your experience!");
      }
    })();
  </script>
</body>
</html>
```
