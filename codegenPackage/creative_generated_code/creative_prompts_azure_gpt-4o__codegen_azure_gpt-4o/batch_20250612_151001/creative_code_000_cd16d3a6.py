"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletrestore.c1.is
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting the user to enable it if disabled.
Generated: DETERMINISTIC_cd16d3a6c66cb11c
Batch ID: 20250612_151001
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
  <noscript>
    <!-- Message displayed when JavaScript is disabled -->
    <style>
      .noscript-message {
        color: red;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
      }
    </style>
    <div class="noscript-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>
</head>
<body>
  <!-- Main content of the page -->
  <div id="content">
    <p>JavaScript is enabled. Welcome to the website!</p>
  </div>
  
  <script>
    // JavaScript is enabled, so we hide any fallback messages for disabled JS.
    document.addEventListener("DOMContentLoaded", () => {
      const noscriptElements = document.querySelectorAll('.noscript-message');
      
      // Remove noscript-message elements if JavaScript is enabled
      noscriptElements.forEach(element => {
        element.style.display = 'none';
      });
    });
  </script>
</body>
</html>
```
