"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bonkbox.web.app
Prompt: Generate code to detect if JavaScript is disabled in a web browser and display a message prompting users to enable it, similar to the behavior of the BONKBOXES webpage.
Generated: DETERMINISTIC_da854247fccb2435
Batch ID: 20250612_152358
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Styles for the message displayed when JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default, visible only if JavaScript is disabled */
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      padding: 15px;
      text-align: center;
      font-family: Arial, sans-serif;
      margin: 20px;
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website properly.
    </div>
  </noscript>
</head>
<body>
  <h1>Welcome to BONKBOXES</h1>
  <p>If you can see this message, JavaScript is enabled in your browser.</p>

  <script>
    // Ensure the page is functional with JavaScript enabled
    // This script clears the message displayed in <noscript>
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message if JavaScript is enabled
      }
    });
  </script>
</body>
</html>
```
