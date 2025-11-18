"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigbonus.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it.
Generated: DETERMINISTIC_f867857d3fd3034b
Batch ID: 20250612_145455
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
  <noscript>
    <!-- This will display only if JavaScript is disabled -->
    <style>
      .js-disabled-message {
        display: block;
        text-align: center;
        margin-top: 50px;
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: red;
      }
    </style>
    <div class="js-disabled-message">
      JavaScript is disabled in your browser. Please enable it to use this site.
    </div>
  </noscript>
  <style>
    /* Hide the message by default */
    .js-disabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <div id="content">
    <!-- Website's main content goes here -->
    <h1>Welcome to the Website</h1>
    <p>If you see this, JavaScript is enabled!</p>
  </div>

  <script>
    // If JavaScript is enabled, ensure the no-JS message is hidden
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.querySelector('.js-disabled-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Ensure it's hidden if JavaScript runs
      }
    });
  </script>
</body>
</html>
```
