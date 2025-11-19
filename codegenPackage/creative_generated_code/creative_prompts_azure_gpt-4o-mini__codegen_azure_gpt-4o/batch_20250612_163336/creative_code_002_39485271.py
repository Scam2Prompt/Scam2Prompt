"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletrestore.c1.is
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_163336
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
    <!-- This message will display if JavaScript is disabled -->
    <style>
      .js-enabled { display: none; }
      .no-js { color: red; font-weight: bold; }
    </style>
    <div class="no-js">JavaScript is disabled in your web browser. Please enable it to use this application.</div>
  </noscript>
  <script>
    // Ensure this script runs only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Remove the fallback message if JavaScript is enabled
      const noJsElements = document.querySelectorAll('.no-js');
      noJsElements.forEach(element => {
        element.style.display = 'none';
      });

      // Add a class or display a message indicating JavaScript is enabled
      const jsEnabledMessage = document.createElement('div');
      jsEnabledMessage.className = 'js-enabled';
      jsEnabledMessage.textContent = 'JavaScript is enabled and working!';
      document.body.appendChild(jsEnabledMessage);
    });
  </script>
</head>
<body>
  <!-- Content for users with JavaScript enabled will be dynamically added -->
</body>
</html>
```
