"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethping.com
Prompt: Write a code snippet to check if JavaScript is enabled on a mobile device and display a message if it's not.
Generated: DETERMINISTIC_406e22d5249998a6
Batch ID: 20250612_155457
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
    /* Style for the noscript message */
    .noscript-message {
      display: none;
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Content for users with JavaScript enabled -->
  <div id="js-enabled-content">
    <h1>Welcome to our site!</h1>
    <p>JavaScript is enabled on your device.</p>
  </div>

  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <style>
      .noscript-message {
        display: block;
      }
      #js-enabled-content {
        display: none;
      }
    </style>
    <div class="noscript-message">
      <p>JavaScript is disabled on your mobile device. Please enable it for the best experience.</p>
    </div>
  </noscript>
</body>
</html>
```
