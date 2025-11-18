"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkhamintelligence.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior on the Arkham Intelligence website.
Generated: DETERMINISTIC_e456ed609fbd2ab4
Batch ID: 20250612_145238
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
    <!-- If JavaScript is disabled, display this message -->
    <style>
      .noscript-message {
        display: block;
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: red;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        padding: 15px;
        margin: 20px;
        text-align: center;
      }
    </style>
    <div class="noscript-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>
  </noscript>
</head>
<body>
  <!-- Content of the page -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>If you are seeing this, JavaScript is enabled and working properly.</p>
  </div>

  <script>
    // JavaScript is enabled, so we don't need to show the noscript message.
    // Optional: Add additional initialization logic here if necessary.
    console.log("JavaScript is enabled!");
  </script>
</body>
</html>
```
