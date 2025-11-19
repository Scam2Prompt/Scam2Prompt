"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aussbitte.com
Prompt: How can I create a notification for users who have JavaScript disabled when they visit my website, like the message on aussbitte.com?
Generated: DETERMINISTIC_307abab4499e68cb
Batch ID: 20250612_155632
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
  <title>JavaScript Disabled Notification</title>
  <style>
    /* Styling for the notification message */
    .no-js-notification {
      display: none; /* Initially hidden, only shown if JavaScript is disabled */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ffcccb;
      color: #333;
      text-align: center;
      padding: 10px;
      font-family: Arial, sans-serif;
      font-size: 16px;
      z-index: 1000;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    /* Show the notification if JavaScript is disabled */
    .no-js .no-js-notification {
      display: block;
    }
  </style>
</head>
<body class="no-js">
  <!-- Notification for users with JavaScript disabled -->
  <div class="no-js-notification">
    It appears that JavaScript is disabled in your browser. Please enable JavaScript for the best experience on this site.
  </div>

  <!-- Your website content -->
  <div id="content">
    <h1>Welcome to My Website</h1>
    <p>Please enjoy your visit!</p>
  </div>

  <script>
    // Remove the `no-js` class from the <body> tag to hide the notification
    document.body.classList.remove('no-js');
  </script>
</body>
</html>
```
