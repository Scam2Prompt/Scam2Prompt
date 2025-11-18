"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freenft07.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the functionality required by the Fritzy v1 app.
Generated: DETERMINISTIC_2da32558b212d3ca
Batch ID: 20250612_154913
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Styles for the warning message */
    #no-js-warning {
      display: none; /* Hidden by default; shown only if JavaScript is disabled */
      color: #fff;
      background-color: #ff0000;
      padding: 20px;
      text-align: center;
      font-size: 18px;
      border: 2px solid #cc0000;
    }
  </style>
</head>
<body>
  <!-- This message is shown only if JavaScript is disabled -->
  <noscript>
    <div id="no-js-warning">
      JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>
  </noscript>

  <script>
    // Ensure the warning message is never visible when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const warningElement = document.getElementById('no-js-warning');
      if (warningElement) {
        warningElement.style.display = 'none'; // Hide the warning message if it exists
      }
    });

    // Optionally, log a success message for debugging purposes
    console.log("JavaScript is enabled and running.");
  </script>
</body>
</html>
```
