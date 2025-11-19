"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web browser for the Decipherer app?
Generated: DETERMINISTIC_d681689e660b7cea
Batch ID: 20250612_162508
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
  <title>Check JavaScript Enabled - Decipherer App</title>
  <style>
    /* Default message for browsers without JavaScript enabled */
    .no-js {
      display: block;
      color: red;
      font-size: 18px;
      font-weight: bold;
    }

    /* Hide message if JavaScript is enabled */
    .js-enabled .no-js {
      display: none;
    }
  </style>
  <script>
    /* Add a class to the HTML element when JavaScript is enabled */
    document.documentElement.classList.add('js-enabled');
  </script>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <div class="no-js">
    JavaScript is disabled in your browser. Please enable it to use the Decipherer app.
  </div>

  <!-- Content displayed only when JavaScript is enabled -->
  <div id="app" style="display: none;">
    <h1>Welcome to the Decipherer App!</h1>
    <p>Enjoy using the app with JavaScript enabled.</p>
  </div>

  <script>
    // Show the app content if JavaScript is enabled
    window.addEventListener('DOMContentLoaded', () => {
      const app = document.getElementById('app');
      if (app) {
        app.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
