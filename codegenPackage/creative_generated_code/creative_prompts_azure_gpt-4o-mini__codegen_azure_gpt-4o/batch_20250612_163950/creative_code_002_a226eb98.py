"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crystal.free.nf
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_163950
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
  <title>JavaScript Check</title>
  <style>
    /* Style to hide the message shown when JavaScript is enabled */
    #js-enabled {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <noscript>
    <h1 style="color: red;">JavaScript is disabled in your browser.</h1>
    <p>Please enable JavaScript to use this website properly.</p>
  </noscript>
  
  <!-- Message shown if JavaScript is enabled -->
  <div id="js-enabled">
    <h1 style="color: green;">JavaScript is enabled in your browser.</h1>
    <p>Everything is working as expected!</p>
  </div>

  <script>
    // Check if JavaScript is enabled by displaying a hidden message
    document.getElementById('js-enabled').style.display = 'block';
  </script>
</body>
</html>
```
