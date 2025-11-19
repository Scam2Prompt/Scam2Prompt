"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iucnba.com
Prompt: How do I create a fallback for users who have JavaScript disabled when visiting iucnba.com?
Generated: DETERMINISTIC_72b4da99b8ebd36d
Batch ID: 20250612_155739
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
  <title>iucnba.com Fallback</title>
  <style>
    /* Basic styling for the fallback message */
    .no-js {
      display: none; /* Hidden by default */
      font-family: Arial, sans-serif;
      font-size: 1.2em;
      color: #333;
      padding: 20px;
      text-align: center;
      background-color: #f8d7da;
      border: 1px solid #f5c2c7;
      border-radius: 5px;
      margin: 20px;
    }

    .js-enabled .no-js {
      display: none; /* Keep it hidden if JavaScript is enabled */
    }
  </style>
</head>
<body>
  <!-- Fallback message for users without JavaScript -->
  <div class="no-js">
    It seems like JavaScript is disabled in your browser. To fully experience our website, please enable JavaScript or visit our <a href="/no-javascript.html">alternative page</a>.
  </div>

  <!-- Main content (hidden if JavaScript is disabled) -->
  <div class="js-content">
    <h1>Welcome to iucnba.com!</h1>
    <p>Enjoy our modern and interactive website experience.</p>
  </div>

  <!-- JavaScript to handle fallback -->
  <script>
    // If JavaScript is enabled, add a class to the document body
    document.body.classList.add('js-enabled');
  </script>
</body>
</html>
```
