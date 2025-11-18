"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: Create a basic HTML and JavaScript template for a web app that displays a warning message if JavaScript is disabled.
Generated: DETERMINISTIC_77163bbbc491e4ad
Batch ID: 20250612_150347
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
  <title>JavaScript Warning Example</title>
  <style>
    /* Styles for the warning message */
    #js-warning {
      display: none; /* Hidden by default, will be displayed if JavaScript is disabled */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Warning message for JavaScript being disabled -->
  <noscript>
    <div id="js-warning">
      Warning: JavaScript is disabled! Please enable JavaScript for the best experience.
    </div>
  </noscript>
  
  <!-- Content of the web app -->
  <div id="app">
    <h1>Welcome to My Web App</h1>
    <p>This is a simple web app template.</p>
  </div>

  <script>
    // JavaScript code for the web app (if any) will go here

    // Example: Ensuring the app is ready
    document.addEventListener('DOMContentLoaded', () => {
      console.log('Web app is initialized.');
    });
  </script>
</body>
</html>
```
