"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb8.cc
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser?
Generated: DETERMINISTIC_b4782b4bf5dab78b
Batch ID: 20250612_160946
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
  <title>Check JavaScript Enabled</title>
  <style>
    /* This message will display if JavaScript is disabled */
    .no-js {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js">
      JavaScript is disabled in your browser. Please enable it for full functionality.
    </div>
  </noscript>

  <!-- Content for users with JavaScript enabled -->
  <div id="js-enabled">
    JavaScript is enabled in your browser.
  </div>

  <script>
    // JavaScript code runs only if JS is enabled
    try {
      // Ensure the no-js message doesn't appear when JavaScript is enabled
      document.querySelector('.no-js').style.display = 'none';
    } catch (error) {
      console.error("An error occurred while checking JavaScript status:", error);
    }
  </script>
</body>
</html>
```
