"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-pals.vercel.app
Prompt: Write code to detect if JavaScript is disabled in a browser and display a message like "You need to enable JavaScript to run this app," as seen on Phantom Pals.
Generated: DETERMINISTIC_209b517d73e92e79
Batch ID: 20250612_145430
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
    /* Default message style: visible when JavaScript is disabled */
    #no-js-message {
      display: block;
      text-align: center;
      margin-top: 20px;
      padding: 10px;
      color: white;
      background-color: red;
      font-size: 18px;
    }

    /* Hide the message when JavaScript is enabled */
    .js-enabled #no-js-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message to be displayed when JavaScript is disabled -->
  <div id="no-js-message">You need to enable JavaScript to run this app.</div>

  <script>
    // Add a class to the HTML element indicating that JavaScript is enabled
    document.documentElement.classList.add('js-enabled');
  </script>
</body>
</html>
```
