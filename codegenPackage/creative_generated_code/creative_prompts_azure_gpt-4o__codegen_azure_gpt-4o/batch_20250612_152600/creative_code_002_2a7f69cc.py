"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethplo.com
Prompt: Generate code to enable JavaScript detection and display a custom message if JavaScript is disabled on a cryptocurrency pledging website.
Generated: DETERMINISTIC_2a7f69cc2d2e9244
Batch ID: 20250612_152600
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
  <title>Cryptocurrency Pledging Website</title>
  <style>
    /* CSS to style the JavaScript-disabled message */
    #no-js-message {
      display: none; /* Hidden by default; will show only if JavaScript is disabled */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <style>
      #no-js-message {
        display: block; /* Show message if JavaScript is disabled */
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Main content of the website -->
  <h1>Welcome to the Cryptocurrency Pledging Website</h1>
  <p>Make secure pledges for your favorite cryptocurrency projects.</p>

  <!-- Custom message for JavaScript disabled -->
  <div id="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to use all features of this website.
  </div>

  <script>
    // JavaScript to ensure the #no-js-message remains hidden if JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none"; // Hide message as JavaScript is enabled
      }
    });
  </script>
</body>
</html>
```
