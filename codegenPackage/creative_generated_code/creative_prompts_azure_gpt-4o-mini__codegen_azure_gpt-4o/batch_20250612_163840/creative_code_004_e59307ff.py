"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkxn.com
Prompt: How do I create a fallback message for users who have JavaScript disabled on mobile sites?
Generated: DETERMINISTIC_e59307ffec1d648d
Batch ID: 20250612_163840
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
  <title>Fallback Message Example</title>
  <style>
    /* Style the fallback message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      text-align: center;
      border: 1px solid #f5c6cb;
      border-radius: 4px;
      font-family: Arial, sans-serif;
      margin: 10px;
    }

    /* If JavaScript is disabled, show the message */
    .no-js .no-js-message {
      display: block;
    }
  </style>
</head>
<body class="no-js">
  <!-- Fallback message for users with JavaScript disabled -->
  <div class="no-js-message">
    It seems like JavaScript is disabled on your device. Please enable JavaScript to fully experience this site.
  </div>

  <!-- Regular content -->
  <div id="main-content">
    <h1>Welcome to Our Mobile Site</h1>
    <p>Enjoy the full functionality of our site.</p>
  </div>

  <script>
    // Remove the 'no-js' class from the <body> tag if JavaScript is enabled
    document.body.classList.remove('no-js');
  </script>
</body>
</html>
```
