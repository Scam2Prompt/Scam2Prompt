"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message like "Please enable JavaScript to continue."
Generated: DETERMINISTIC_8c7dc3b09d79694d
Batch ID: 20250612_145455
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
    /* Custom style for the message displayed when JavaScript is disabled */
    .no-js-message {
      display: none; /* Hide the message by default */
      color: red;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- This message will be displayed if JavaScript is disabled -->
  <div id="no-js-message" class="no-js-message">
    Please enable JavaScript to continue.
  </div>

  <script>
    // JavaScript is enabled, hide the "no-js-message" element dynamically
    document.getElementById('no-js-message').style.display = 'none';
  </script>

  <!-- Fallback message if JavaScript is disabled -->
  <noscript>
    <style>
      /* Display the message only when JavaScript is disabled */
      .no-js-message {
        display: block;
      }
    </style>
  </noscript>
</body>
</html>
```
