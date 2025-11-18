"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the behavior on the "aubi.online" domain details page.
Generated: DETERMINISTIC_f37adcfbec78c53f
Batch ID: 20250612_154958
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* Style for the No-JavaScript message */
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
  <!-- Default message shown if JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable it to use this site.
    </div>
  </noscript>

  <script>
    // JavaScript is enabled if this script runs
    document.addEventListener("DOMContentLoaded", () => {
      // Example: JavaScript-related setup or message
      console.log("JavaScript is enabled.");
    });

    // Optional: You can dynamically remove the above <noscript> message if needed
  </script>
</body>
</html>
```
