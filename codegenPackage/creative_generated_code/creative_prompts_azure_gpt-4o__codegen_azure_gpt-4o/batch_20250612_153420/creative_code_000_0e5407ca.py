"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.org
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the functionality described on the Origin USD website.
Generated: DETERMINISTIC_0e5407ca871a0f35
Batch ID: 20250612_153420
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
    /* Style for the message displayed when JavaScript is disabled */
    .no-js-message {
      display: none; /* Initially hidden */
      color: red;
      font-size: 16px;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Default message for JavaScript-disabled browsers -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to improve your experience.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This is the main content of the page.</p>
  </div>

  <script>
    // Self-invoking function to detect JavaScript status
    (function () {
      try {
        // Select the message element
        const noJsMessage = document.querySelector('.no-js-message');
        
        // Ensure it's hidden when JavaScript is enabled
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        console.error('Error while detecting JavaScript status:', error);
      }
    })();
  </script>
</body>
</html>
```
