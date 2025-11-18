"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earndrop.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message prompting the user to enable it.
Generated: DETERMINISTIC_b5af9e14f0d94381
Batch ID: 20250612_153648
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
    /* Custom styles for the message */
    #js-disabled-message {
      display: none; /* Hidden by default, shown if JS is disabled */
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div id="js-disabled-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Content for users with JavaScript enabled -->
  <div id="js-enabled-content">
    <h1>Welcome to our website!</h1>
    <p>Thank you for enabling JavaScript.</p>
  </div>

  <script>
    // JavaScript code to ensure the noscript message remains hidden
    // For users with JavaScript enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noScriptMessage = document.getElementById('js-disabled-message');
      if (noScriptMessage) {
        noScriptMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
