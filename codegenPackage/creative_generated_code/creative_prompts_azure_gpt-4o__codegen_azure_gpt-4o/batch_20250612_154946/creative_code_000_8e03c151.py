"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwallet.42web.io
Prompt: Write JavaScript code to detect if a user's browser has JavaScript disabled and display a custom message prompting them to enable it.
Generated: DETERMINISTIC_8e03c1514fe93862
Batch ID: 20250612_154946
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
    /* Styling for the no-JavaScript message */
    .no-js-msg {
      display: none; /* Hidden by default */
      color: red;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-msg">
      JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>
  </noscript>

  <!-- Main content -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This content will be enhanced with JavaScript if it's enabled.</p>
  </div>

  <script>
    // JavaScript code executes only when JavaScript is enabled
    (function() {
      try {
        // Select the no-JavaScript message
        const noJsMessage = document.querySelector('.no-js-msg');
        
        // Hide the message to confirm JavaScript is enabled
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        console.error('An error occurred while detecting JavaScript status:', error);
      }
    })();
  </script>
</body>
</html>
```
