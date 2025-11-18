"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a warning message for BTC pledge-related functionality.
Generated: DETERMINISTIC_1c91980a82f73b1a
Batch ID: 20250612_145619
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
  <title>JavaScript Disabled Warning</title>
  <style>
    /* Style for the warning message */
    .js-warning {
      display: none; /* Hidden by default; will be shown if JS is disabled */
      background-color: #ffcccb;
      color: #000;
      padding: 15px;
      border: 1px solid #ff0000;
      border-radius: 5px;
      margin: 20px 0;
      text-align: center;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Warning message for JavaScript-disabled browsers -->
  <noscript>
    <!-- The noscript tag ensures this content is displayed only when JS is disabled -->
    <div class="js-warning">
      JavaScript is disabled in your browser. BTC pledge functionality requires JavaScript to be enabled.
      Please enable JavaScript to proceed.
    </div>
  </noscript>

  <script>
    // Self-contained script to ensure JS is working
    try {
      // If JavaScript is enabled, the warning message won't be shown
      const warningMessage = document.querySelector('.js-warning');
      if (warningMessage) {
        warningMessage.style.display = 'none';
      }
    } catch (error) {
      // Error handling (fallback for unexpected JS issues)
      console.error("An error occurred while checking JavaScript functionality:", error);
    }
  </script>
</body>
</html>
```
