"""
Generated Code Metadata:
========================
Original URL: https://ethbvt.com
Prompt: Generate a simple webpage code snippet that requires JavaScript to be enabled, similar to the ethbvt.com website.
Generated: DETERMINISTIC_4adcdcc75439310d
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Required</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    #no-js-message {
      display: block;
      color: #ff0000;
      font-size: 1.5em;
      margin-top: 20%;
    }

    #content {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is required to view this webpage. Please enable JavaScript in your browser settings.
    </div>
  </noscript>

  <!-- Content that will be shown if JavaScript is enabled -->
  <div id="content">
    <h1>Welcome to the Website</h1>
    <p>JavaScript is enabled. Enjoy your experience!</p>
  </div>

  <script>
    // Ensure the page content is displayed only if JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Hide the no-JS message
        const noJsMessage = document.getElementById('no-js-message');
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }

        // Show the main content
        const content = document.getElementById('content');
        if (content) {
          content.style.display = 'block';
        }
      } catch (error) {
        console.error('An error occurred while initializing the page:', error);
      }
    });
  </script>
</body>
</html>
```
