"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genixs.co
Prompt: Generate code to detect whether JavaScript is disabled in a browser and display a custom message instructing users to enable it.
Generated: DETERMINISTIC_8da31b174fa8948f
Batch ID: 20250612_154344
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
    /* Style for the message displayed if JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default; shown only if JavaScript is disabled */
      color: red;
      font-size: 1.2rem;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <p class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this site properly.
    </p>
  </noscript>

  <!-- Normal content for users with JavaScript enabled -->
  <div id="content">
    <h1>Welcome to our website!</h1>
    <p>This is the main content of the site.</p>
  </div>

  <script>
    // JavaScript-enabled users will automatically hide the noscript message
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
