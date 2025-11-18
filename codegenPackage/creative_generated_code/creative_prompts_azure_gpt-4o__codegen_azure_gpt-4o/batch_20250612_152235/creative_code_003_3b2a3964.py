"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Generate code for a web app that displays a custom error message when JavaScript is disabled, as seen in the FRONK web app.
Generated: DETERMINISTIC_3b2a39641db83687
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
  <title>JavaScript Disabled Warning</title>
  <style>
    /* Styles for the JavaScript-disabled message */
    .no-js-warning {
      display: none; /* Initially hidden */
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 20px;
      margin: 20px 0;
      text-align: center;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <!-- Warning message -->
  <div class="no-js-warning" id="noJsWarning">
    ⚠️ JavaScript is disabled in your browser. This application requires JavaScript to function properly. Please enable JavaScript and refresh the page.
  </div>

  <!-- Content of the web app -->
  <div id="appContent">
    <h1>Welcome to the FRONK Web App</h1>
    <p>This is a sample web application.</p>
  </div>

  <!-- Fallback for browsers with JavaScript disabled -->
  <noscript>
    <style>
      /* Override styles to display the message when JavaScript is disabled */
      #noJsWarning {
        display: block;
      }
      #appContent {
        display: none; /* Hide the app content */
      }
    </style>
  </noscript>

  <script>
    // Ensure proper functionality and hide the warning message if JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      try {
        const noJsWarning = document.getElementById("noJsWarning");
        if (noJsWarning) {
          noJsWarning.style.display = "none"; // Hide the warning as JavaScript is enabled
        }
      } catch (error) {
        console.error("An error occurred while initializing the application:", error);
        alert("An unexpected error occurred. Please try refreshing the page.");
      }
    });
  </script>
</body>
</html>
```
