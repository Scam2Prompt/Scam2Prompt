"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminiig.com
Prompt: Generate a JavaScript snippet to detect if JavaScript is disabled in a browser and display a message like the one on geminiig.com.
Generated: DETERMINISTIC_d9be0ad77d80f406
Batch ID: 20250612_152600
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
    /* Styling for the no-JavaScript message */
    .no-js-message {
      display: none; /* Hidden by default when JavaScript is enabled */
      color: red;
      font-size: 18px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- This block is displayed if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block; /* Show this message if JavaScript is disabled */
      }
    </style>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to access the full functionality of this site.
    </div>
  </noscript>
</head>
<body>
  <!-- Main content of the page -->
  <div>
    <h1>Welcome to Our Website</h1>
    <p>Enjoy your experience!</p>
  </div>
  
  <script>
    // JavaScript is enabled; this script will run
    // Ensure the no-JavaScript message is hidden
    document.addEventListener('DOMContentLoaded', () => {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message if JavaScript is enabled
      }
    });
  </script>
</body>
</html>
```
