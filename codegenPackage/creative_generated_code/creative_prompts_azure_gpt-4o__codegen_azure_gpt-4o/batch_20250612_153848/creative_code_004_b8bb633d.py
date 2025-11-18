"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-wiederherstellung.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in the browser and display a warning message, as seen on the Coinbase login page.
Generated: DETERMINISTIC_b8bb633d14e26dcd
Batch ID: 20250612_153848
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
    /* Style for the warning message */
    #js-disabled-warning {
      display: none; /* Hidden by default, shown only if JS is disabled */
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
      margin: 20px auto;
      max-width: 600px;
    }
  </style>
  <noscript>
    <!-- Warning message displayed when JavaScript is disabled -->
    <div id="js-disabled-warning">
      JavaScript is disabled in your browser. Please enable JavaScript to continue using this site.
    </div>
  </noscript>
</head>
<body>
  <h1>Welcome</h1>
  <p>Please log in to continue.</p>

  <script>
    // Ensure the warning message does not appear when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      // Check for the presence of the warning element
      const warningElement = document.getElementById("js-disabled-warning");
      
      // Hide the warning element if JavaScript is enabled
      if (warningElement) {
        warningElement.style.display = "none";
      }
    });
  </script>
</body>
</html>
```
