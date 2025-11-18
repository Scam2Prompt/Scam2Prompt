"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled. Please enable it to continue," as seen on the DogeAI website.
Generated: DETERMINISTIC_fe1512dc2030ed56
Batch ID: 20250612_154312
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
    /* Styling for the message displayed when JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default; shown only if JS is disabled */
      color: red;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <div class="no-js-message">
      This app doesn't work properly without JavaScript enabled. Please enable it to continue.
    </div>
  </noscript>

  <!-- Main content or application -->
  <div id="app">
    <!-- JavaScript-enabled users will see this content -->
    <h1>Welcome to the App</h1>
    <p>Your browser supports JavaScript!</p>
  </div>

  <script>
    // JavaScript is enabled; this script will run
    document.addEventListener("DOMContentLoaded", () => {
      // Ensure the page content behaves normally for users with JavaScript enabled
      console.log("JavaScript is enabled.");
    });

    // Optional: Additional error handling or diagnostic logic for complex apps
  </script>
</body>
</html>
```
