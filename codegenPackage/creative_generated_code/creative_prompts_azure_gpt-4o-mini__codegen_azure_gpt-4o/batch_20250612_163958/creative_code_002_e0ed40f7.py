"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lp.btcc.limited
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like BTCC?
Generated: DETERMINISTIC_e0ed40f75a53a5da
Batch ID: 20250612_163958
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
  <style>
    /* Default message displayed if JavaScript is disabled */
    .no-js-message {
      display: block;
      color: red;
      font-weight: bold;
    }

    /* Hide the message if JavaScript is enabled */
    .js-enabled .no-js-message {
      display: none;
    }
  </style>
  <script>
    // Add a class to the <html> element to indicate JS is enabled
    document.documentElement.classList.add('js-enabled');
  </script>
</head>
<body>
  <!-- Message shown to users if JavaScript is disabled -->
  <noscript>
    <p class="no-js-message">JavaScript is disabled in your browser. Please enable JavaScript to use this application.</p>
  </noscript>

  <!-- Content for users with JavaScript enabled -->
  <div>
    <p>JavaScript is enabled. Welcome to the application!</p>
  </div>
</body>
</html>
```
