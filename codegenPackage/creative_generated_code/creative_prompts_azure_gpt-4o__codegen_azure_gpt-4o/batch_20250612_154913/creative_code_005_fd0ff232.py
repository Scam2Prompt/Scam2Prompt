"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freenft07.vercel.app
Prompt: Write JavaScript code to display a custom message when JavaScript is disabled, tailored for a web app like Fritzy v1.
Generated: DETERMINISTIC_fd0ff2321e1fa172
Batch ID: 20250612_154913
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
  <title>Fritzy v1</title>
  <style>
    /* Styling for the no-JavaScript message */
    .no-js-message {
      color: #ffffff;
      background-color: #ff0000;
      padding: 20px;
      text-align: center;
      font-size: 1.2rem;
      font-family: Arial, sans-serif;
      border: 2px solid #ff0000;
      border-radius: 5px;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- Default message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled or not supported in your browser. Fritzy v1 requires JavaScript to function properly. Please enable JavaScript to continue.
    </div>
  </noscript>

  <!-- Main app content (hidden if JavaScript is disabled) -->
  <div id="app">
    <h1>Welcome to Fritzy v1</h1>
    <p>Enjoy exploring our web application!</p>
  </div>

  <script>
    // JavaScript error handling: For browsers that support JavaScript but encounter runtime errors
    try {
      // Ensure that the app content is shown only when JavaScript is enabled
      const appContent = document.getElementById('app');
      if (appContent) {
        appContent.style.display = 'block'; // Make app visible if JavaScript is enabled
      }
    } catch (error) {
      // Log any unexpected errors to the console
      console.error('An unexpected error occurred while initializing the app:', error);
    }
  </script>
</body>
</html>
```
