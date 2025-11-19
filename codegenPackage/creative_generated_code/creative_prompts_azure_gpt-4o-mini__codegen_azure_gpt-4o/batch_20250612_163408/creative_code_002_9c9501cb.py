"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-32--compassionate-wing-d4bcd6.netlify.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like vue-diet?
Generated: DETERMINISTIC_9c9501cbd233bc04
Batch ID: 20250612_163408
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
    /* Hide the fallback message by default */
    .no-js {
      display: none;
      color: red;
      font-weight: bold;
    }
    /* If JavaScript is disabled, this will make the message visible */
    .js-enabled .no-js {
      display: none;
    }
  </style>
  <script>
    // Add a class to the HTML element to indicate JavaScript is enabled
    document.documentElement.classList.add('js-enabled');
  </script>
</head>
<body>
  <!-- Fallback message for users with JavaScript disabled -->
  <div class="no-js">
    JavaScript is disabled in your browser. Please enable it to use this application.
  </div>

  <div id="app">
    <!-- Vue.js or other JavaScript-based content goes here -->
    <h1>Welcome to Vue-Diet!</h1>
  </div>
</body>
</html>
```
