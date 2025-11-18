"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etbkwf.com
Prompt: Generate code to detect if JavaScript is disabled and display a warning message for users accessing a dApp, similar to the behavior on https://etbkwf.com.
Generated: DETERMINISTIC_c216e05affd1a9d3
Batch ID: 20250612_154635
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
    #js-warning {
      display: none; /* Hidden by default */
      background-color: #ffcccc;
      color: #800000;
      padding: 10px;
      margin: 20px 0;
      border: 1px solid #800000;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      text-align: center;
    }

    /* Show message if JavaScript is disabled */
    .no-js #js-warning {
      display: block;
    }
  </style>
  <noscript>
    <!-- noscript tag is used to show content if JavaScript is disabled -->
    <style>
      #js-warning {
        display: block; /* Force display of the warning message */
      }
    </style>
  </noscript>
</head>
<body class="no-js">
  <!-- Warning message displayed if JavaScript is disabled -->
  <div id="js-warning">
    JavaScript is disabled in your browser. Please enable JavaScript to access this application.
  </div>

  <script>
    // Remove the 'no-js' class from <body> if JavaScript is enabled
    document.body.classList.remove('no-js');
  </script>
</body>
</html>
```
