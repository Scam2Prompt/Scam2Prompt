"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser when accessing the Celestia domain details page?
Generated: DETERMINISTIC_1def18fc2353f76a
Batch ID: 20250612_155639
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
  <title>Celestia Domain Details</title>
  <style>
    /* Hide the fallback message initially */
    #js-disabled-message {
      display: none;
      color: red;
    }

    /* Show the fallback message if JavaScript is disabled */
    .no-js #js-disabled-message {
      display: block;
    }
  </style>
  <script>
    // Dynamically set a class on the HTML element if JavaScript is enabled
    document.documentElement.classList.remove('no-js');
    document.documentElement.classList.add('js');
  </script>
</head>
<body>
  <!-- Fallback message for when JavaScript is disabled -->
  <noscript>
    <p id="js-disabled-message">
      It seems like JavaScript is disabled in your browser. Please enable JavaScript to access the Celestia Domain Details page correctly.
    </p>
  </noscript>

  <!-- Main content for users with JavaScript enabled -->
  <div id="main-content">
    <h1>Welcome to Celestia Domain Details</h1>
    <p>This page requires JavaScript to function properly.</p>
  </div>
</body>
</html>
```
