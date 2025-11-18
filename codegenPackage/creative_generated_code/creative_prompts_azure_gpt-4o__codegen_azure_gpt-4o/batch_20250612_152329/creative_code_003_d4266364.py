"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbsc.com
Prompt: Provide an example of JavaScript code that checks for JavaScript being enabled in a browser and displays a warning if it is disabled.
Generated: DETERMINISTIC_d42663643150a3c5
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Enabled Check</title>
  <style>
    /* Style for the warning message */
    .no-js-warning {
      display: none;
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Warning message displayed if JavaScript is disabled -->
  <noscript>
    <div class="no-js-warning">
      Warning: JavaScript is disabled. Please enable JavaScript for the best experience.
    </div>
  </noscript>
  <h1>Welcome to Our Website</h1>
  <p>Your experience will be enhanced with JavaScript enabled!</p>
  
  <!-- JavaScript to ensure the page works correctly -->
  <script>
    // Ensure any additional dynamic checks for JavaScript can be handled here
    document.addEventListener("DOMContentLoaded", function () {
      // JavaScript is enabled, so no further action needed
      console.log("JavaScript is enabled.");
    });
  </script>
</body>
</html>
```
