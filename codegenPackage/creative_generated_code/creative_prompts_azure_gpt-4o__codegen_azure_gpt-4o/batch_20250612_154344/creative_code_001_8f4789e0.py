"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrny.world
Prompt: Create a script to detect if JavaScript is disabled in a browser and display a message prompting users to enable JavaScript for the "JRNY" app.
Generated: DETERMINISTIC_8f4789e0fd6d5ba4
Batch ID: 20250612_154344
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
  <title>JRNY App</title>

  <!-- Styles for the no-JavaScript message -->
  <style>
    #no-js-message {
      display: none; /* Hidden by default, shown only if JavaScript is disabled */
      color: #ffffff;
      background-color: #ff5722;
      text-align: center;
      padding: 15px;
      font-size: 18px;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 9999;
    }
  </style>
</head>
<body>
  <!-- No-JavaScript message -->
  <div id="no-js-message">
    JavaScript is disabled in your browser. Please enable it to use the JRNY app.
  </div>

  <!-- Content of the app -->
  <div id="app">
    <h1>Welcome to the JRNY App</h1>
    <p>Enjoy your journey with us!</p>
  </div>

  <!-- JavaScript to hide the no-JavaScript message -->
  <script>
    // Ensure the "no-js-message" does not appear when JavaScript is enabled
    (function() {
      try {
        // Select the no-JavaScript message element
        const noJsMessage = document.getElementById('no-js-message');
        
        // Hide the message if JavaScript is enabled
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('An error occurred while hiding the no-JavaScript message:', error);
      }
    })();
  </script>
  
  <!-- Fallback message for users with JavaScript disabled -->
  <noscript>
    <style>
      #no-js-message {
        display: block; /* Force display when JavaScript is disabled */
      }
    </style>
  </noscript>
</body>
</html>
```
