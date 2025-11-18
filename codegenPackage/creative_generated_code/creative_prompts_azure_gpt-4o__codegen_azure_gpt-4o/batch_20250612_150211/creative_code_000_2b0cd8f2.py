"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cardex.space
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
Batch ID: 20250612_150211
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
    /* The message will only be visible if JavaScript is disabled */
    #no-js-message {
      display: none; /* This will be overridden if JavaScript is off */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Default message shown if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is disabled in your browser. Please enable it to use this website.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="content">
    <h1>Welcome to Our Website</h1>
    <p>Your browser supports JavaScript!</p>
  </div>

  <script>
    // JavaScript to hide the 'no-js-message' if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Ensure the message doesn't appear when JS is enabled
      }
    });
  </script>
</body>
</html>
```
