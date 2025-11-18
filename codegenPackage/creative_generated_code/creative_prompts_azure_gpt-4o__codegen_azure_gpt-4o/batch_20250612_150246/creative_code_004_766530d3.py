"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rainbnb.live
Prompt: Write a script to detect whether JavaScript is enabled in a user's browser and display a warning message if it is disabled, as seen on RainBNB.
Generated: DETERMINISTIC_766530d379239736
Batch ID: 20250612_150246
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
    /* Warning message styling */
    .no-js-warning {
      display: block; /* Ensures the warning shows by default */
      background-color: #ffcccc; /* Light red background */
      color: #000; /* Black text for good contrast */
      text-align: center;
      padding: 15px;
      font-size: 1rem;
      border: 1px solid #ff0000; /* Red border */
      margin: 10px;
    }
  </style>
</head>
<body>
  <!-- Warning message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-warning">
      Warning: JavaScript is disabled in your browser. Please enable JavaScript to use all features of this site.
    </div>
  </noscript>

  <!-- Main content -->
  <h1>Welcome to RainBNB</h1>
  <p>Enjoy browsing our site!</p>

  <script>
    // JavaScript is enabled, so we can dynamically remove the warning or provide further enhancements if needed.
    // In this case, the <noscript> warning already handles the display logic by default.
    console.log('JavaScript is enabled.');
  </script>
</body>
</html>
```
