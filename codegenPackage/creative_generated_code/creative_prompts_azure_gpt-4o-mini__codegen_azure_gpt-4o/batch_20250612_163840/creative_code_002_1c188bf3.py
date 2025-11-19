"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbod.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
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
  <title>Check JavaScript Enabled</title>
  <noscript>
    <!-- Display a message if JavaScript is disabled -->
    <style>
      .no-js-warning {
        color: red;
        font-weight: bold;
        text-align: center;
        padding: 20px;
      }
    </style>
    <div class="no-js-warning">
      JavaScript is disabled in your browser. Please enable it to view this content.
    </div>
  </noscript>
</head>
<body>
  <!-- Main content for when JavaScript is enabled -->
  <div id="js-enabled-content" style="display: none;">
    <h1>JavaScript is enabled!</h1>
    <p>Your browser supports JavaScript and it is turned on.</p>
  </div>

  <script>
    // Ensure JavaScript is enabled by manipulating DOM elements
    document.addEventListener('DOMContentLoaded', () => {
      const jsEnabledContent = document.getElementById('js-enabled-content');
      if (jsEnabledContent) {
        jsEnabledContent.style.display = 'block'; // Show the content for JavaScript-enabled browsers
      }
    });
  </script>
</body>
</html>
```
