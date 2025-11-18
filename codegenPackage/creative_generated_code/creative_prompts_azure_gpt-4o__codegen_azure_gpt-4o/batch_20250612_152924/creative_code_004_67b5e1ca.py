"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.eu
Prompt: Provide a solution for ensuring a web app remains functional even when JavaScript is disabled, while still prompting users to enable JavaScript for full functionality.
Generated: DETERMINISTIC_67b5e1ca58e7f58b
Batch ID: 20250612_152924
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
  <title>JavaScript Disabled Fallback</title>
  <style>
    /* Styling for the "JavaScript Disabled" message */
    .no-js-warning {
      display: none; /* Hidden by default */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }

    /* If JavaScript is disabled, this CSS rule will be applied */
    html.no-js .no-js-warning {
      display: block;
    }
  </style>
  <script>
    // Remove "no-js" class if JavaScript is enabled
    document.documentElement.classList.remove('no-js');
  </script>
</head>

<body>
  <noscript>
    <!-- This block will only be rendered if JavaScript is disabled -->
    <div class="no-js-warning">
      JavaScript is disabled in your browser. Some features may not work as expected. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <div>
    <!-- Main content of the application -->
    <h1>Welcome to the Web App</h1>
    <p>This application works without JavaScript, but enabling it will unlock full functionality.</p>
  </div>

  <script>
    // Example script to demonstrate JavaScript functionality
    try {
      // Simulating JavaScript-dependent functionality
      const message = document.createElement('p');
      message.textContent = "You're using JavaScript!";
      message.style.color = "green";
      document.body.appendChild(message);
    } catch (error) {
      console.error("An error occurred while running JavaScript:", error);
    }
  </script>
</body>

</html>
```
