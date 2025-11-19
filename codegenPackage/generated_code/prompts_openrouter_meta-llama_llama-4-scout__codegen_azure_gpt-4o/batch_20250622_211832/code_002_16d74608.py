"""
Generated Code Metadata:
========================
Original URL: https://lbpiaccess.jzta.com
Prompt: Generate HTML and JavaScript code to create a simple webpage that checks if JavaScript is enabled in the user's browser.
Generated: DETERMINISTIC_16d74608d46744e8
Batch ID: 20250622_211832
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
  <title>JavaScript Check</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }
    .message {
      font-size: 1.5rem;
      color: #333;
    }
  </style>
</head>
<body>
  <!-- Default message for browsers with JavaScript disabled -->
  <noscript>
    <div class="message">
      JavaScript is disabled in your browser. Please enable it to use this webpage.
    </div>
  </noscript>

  <!-- Placeholder for the JavaScript-enabled message -->
  <div id="js-check" class="message"></div>

  <script>
    // Check if JavaScript is enabled and display a message
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Select the placeholder element
        const jsCheckElement = document.getElementById('js-check');
        
        // Update the message to indicate JavaScript is enabled
        jsCheckElement.textContent = 'JavaScript is enabled in your browser!';
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('An error occurred while checking JavaScript status:', error);
      }
    });
  </script>
</body>
</html>
```
