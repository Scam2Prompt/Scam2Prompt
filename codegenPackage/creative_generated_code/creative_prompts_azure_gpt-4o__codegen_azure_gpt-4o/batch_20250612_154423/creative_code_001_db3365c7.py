"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-web-utils-prod.app.greate.eu
Prompt: Create a script that mimics the functionality of the Metamask Web Utils domain details page by detecting JavaScript support and prompting users to enable it for proper app functionality.
Generated: DETERMINISTIC_db3365c7d8bda81a
Batch ID: 20250612_154423
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
  <style>
    /* Basic styling */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    .js-disabled {
      display: none;
      color: red;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <style>
      .js-disabled {
        display: block;
      }
    </style>
    <p class="js-disabled">JavaScript is disabled. Please enable JavaScript to use this application.</p>
  </noscript>
</head>
<body>
  <h1>Welcome to Our Application</h1>
  <p>If you can see this, JavaScript is enabled!</p>

  <script>
    // Detect JavaScript functionality
    try {
      // Simulating JavaScript functionality detection
      const jsStatus = document.createElement('p');
      jsStatus.textContent = 'JavaScript is enabled and working correctly.';
      jsStatus.style.color = 'green';
      document.body.appendChild(jsStatus);
    } catch (error) {
      // Handle unexpected errors gracefully
      console.error('An error occurred while detecting JavaScript functionality:', error);
      const errorMsg = document.createElement('p');
      errorMsg.textContent = 'An error occurred. Please refresh your browser or check your JavaScript settings.';
      errorMsg.style.color = 'red';
      document.body.appendChild(errorMsg);
    }
  </script>
</body>
</html>
```
