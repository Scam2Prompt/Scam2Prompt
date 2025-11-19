"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqed.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_155739
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
    <div class="no-js">JavaScript is disabled in your web browser. Please enable JavaScript for full functionality.</div>
  </noscript>
  <script>
    // Ensure this script runs only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      // Add a class to indicate JavaScript is enabled
      document.body.classList.add('js-enabled');
    });
  </script>
</head>
<body>
  <div class="js-enabled">
    <!-- Content visible only if JavaScript is enabled -->
    <h1>JavaScript is enabled!</h1>
  </div>
</body>
</html>
```
abledMessage = document.querySelector('.js-enabled');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>
</head>
<body>
  <div class="js-enabled" style="display: none; color: green; font-weight: bold;">
    JavaScript is enabled and working correctly!
  </div>
</body>
</html>
```
