"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-octofi.pages.dev
Prompt: Write code to display a custom message when JavaScript is disabled in a web app interface.
Generated: DETERMINISTIC_689a80ec9818407d
Batch ID: 20250612_152235
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
  <title>JavaScript Disabled Message</title>
  <style>
    /* Style for the no-script message */
    .no-js-message {
      display: none; /* Hide by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 10px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 14px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Content of the web application -->
  <div id="app">
    <h1>Welcome to the Web App</h1>
    <p>This application requires JavaScript to function properly.</p>
  </div>

  <!-- No-script message -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use the full functionality of this application.
    </div>
  </noscript>

  <!-- Optional JavaScript initialization -->
  <script>
    // This script ensures that the page functions correctly when JavaScript is enabled.
    document.addEventListener('DOMContentLoaded', () => {
      console.log("JavaScript is enabled. The application is running.");
    });
  </script>
</body>
</html>
```
