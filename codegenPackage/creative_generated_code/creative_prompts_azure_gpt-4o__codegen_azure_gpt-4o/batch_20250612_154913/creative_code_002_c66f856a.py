"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase33.com
Prompt: Generate a script to detect if JavaScript is disabled in a browser and display a custom error message, referencing the iview-admin requirements mentioned on the Coinbase33 website.
Generated: DETERMINISTIC_c66f856a668c7909
Batch ID: 20250612_154913
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
  
  <!-- Include essential styles -->
  <style>
    .no-js-error {
      display: none; /* Hidden by default */
      font-family: Arial, sans-serif;
      color: #fff;
      background-color: #ff4d4f;
      padding: 20px;
      text-align: center;
      border-radius: 5px;
      margin: 20px;
    }
  </style>
</head>
<body>
  
  <!-- Message to display if JavaScript is disabled -->
  <div id="no-js-message" class="no-js-error">
    JavaScript is disabled in your browser. Please enable JavaScript to use this application.
  </div>
  
  <noscript>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <style>
      #no-js-message {
        display: block; /* Show the message if JavaScript is disabled */
      }
    </style>
  </noscript>
  
  <!-- JavaScript to hide the message if JavaScript is enabled -->
  <script>
    (function () {
      try {
        // Find the "no-js-message" div and hide it if JavaScript is enabled
        const noJsMessage = document.getElementById('no-js-message');
        if (noJsMessage) {
          noJsMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any unexpected errors to the console
        console.error('Error while detecting JavaScript status:', error);
      }
    })();
  </script>

</body>
</html>
```
