"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etf-key.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message prompting the user to enable it.
Generated: DETERMINISTIC_b5af9e14f0d94381
Batch ID: 20250612_150234
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
    /* Custom styles for the message when JavaScript is disabled */
    .no-js-message {
      color: red;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for when JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable it to use this website properly.
    </div>
  </noscript>

  <script>
    // The script tag itself serves as the primary mechanism to detect enabled JavaScript.
    // If JavaScript is disabled, the <noscript> content will be displayed instead.
    console.log("JavaScript is enabled. No further action needed.");
  </script>
</body>
</html>
```
