"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imotokaen.com
Prompt: Can you provide code snippets to detect if JavaScript is enabled on a mobile device and display a message if it is not?
Generated: DETERMINISTIC_4c4a3bce0e0a3c02
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
  <title>JavaScript Detection</title>
  <style>
    /* Styling for the message displayed if JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default */
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message to display if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled on your device. Please enable it for the best experience.
    </div>
  </noscript>

  <script>
    // JavaScript runs automatically if enabled, so no extra handling is needed.
    // We use <noscript> to handle cases where JavaScript is disabled.
  </script>
</body>
</html>
```
