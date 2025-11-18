"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript disabled and display a warning message similar to the one on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_196cb256f8c85020
Batch ID: 20250612_152441
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
    /* Styling for the no-JavaScript warning message */
    #js-warning {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 10px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px auto;
      width: 80%;
    }
  </style>
</head>
<body>
  <!-- No-JavaScript warning message -->
  <noscript>
    <div id="js-warning">
      Warning: JavaScript is disabled in your browser. Please enable JavaScript to use this site properly.
    </div>
  </noscript>

  <!-- Main content -->
  <div id="main-content">
    <h1>Welcome to the Website</h1>
    <p>This content is visible only if JavaScript is enabled.</p>
  </div>

  <script>
    // Ensure the page is fully functional when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Hide the warning message
        const warningMessage = document.getElementById('js-warning');
        if (warningMessage) {
          warningMessage.style.display = 'none';
        }

        // Show the main content
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
          mainContent.style.display = 'block';
        }
      } catch (error) {
        console.error('An error occurred while processing JavaScript detection:', error);
      }
    });
  </script>
</body>
</html>
```
