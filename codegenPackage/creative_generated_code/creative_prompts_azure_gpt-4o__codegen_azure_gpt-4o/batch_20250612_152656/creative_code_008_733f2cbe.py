"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wen-drop.web.app
Prompt: Write a script to check if JavaScript is enabled on a user's browser and display a message prompting them to enable it, as required by Wen Exchange.
Generated: DETERMINISTIC_733f2cbe1297c184
Batch ID: 20250612_152656
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
    /* Style for the no-JS message */
    .no-js-message {
      display: none;
      font-family: Arial, sans-serif;
      color: red;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <script>
    // When JavaScript is enabled, remove the no-JS message
    document.addEventListener("DOMContentLoaded", function () {
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none";
      }
    });
  </script>
</head>
<body>
  <!-- Default message for users with JavaScript disabled -->
  <noscript>
    <div id="no-js-message" class="no-js-message">
      JavaScript is not enabled in your browser. Wen Exchange requires JavaScript to function properly. 
      Please enable JavaScript in your browser settings and refresh the page.
    </div>
  </noscript>

  <!-- Main content of the page -->
  <div>
    <h1>Welcome to Wen Exchange</h1>
    <p>If you're seeing this, JavaScript is enabled and the site will work as expected.</p>
  </div>
</body>
</html>
```
