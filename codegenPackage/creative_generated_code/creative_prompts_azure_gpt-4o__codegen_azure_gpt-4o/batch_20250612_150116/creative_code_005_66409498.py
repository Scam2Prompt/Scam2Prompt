"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a user's browser and display a warning message.
Generated: DETERMINISTIC_664094980dca82b5
Batch ID: 20250612_150116
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
    /* Styling for the warning message */
    #js-warning {
      display: none; /* Hidden by default; shown when JS is disabled */
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Warning message placeholder -->
  <noscript>
    <!-- This block will only be rendered if JavaScript is disabled -->
    <div id="js-warning">
      Warning: JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <script>
    // JavaScript code runs here if enabled
    document.addEventListener('DOMContentLoaded', () => {
      // If JavaScript is enabled, ensure no warning is shown
      const warningElement = document.getElementById('js-warning');
      if (warningElement) {
        warningElement.style.display = 'none'; // Hide the warning if it's present
      }
    });
  </script>
</body>
</html>
```
