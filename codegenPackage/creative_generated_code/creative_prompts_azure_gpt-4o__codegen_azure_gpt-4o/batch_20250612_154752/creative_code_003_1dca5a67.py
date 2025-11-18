"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://combo.magiceden.nl
Prompt: Generate JavaScript code to display a warning message and block access to a webpage if JavaScript is not enabled, mimicking the behavior described on the Magic Eden NL site.
Generated: DETERMINISTIC_1dca5a6746abb2c6
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Enabled Check</title>

  <style>
    /* Styling for the warning message */
    #no-js-warning {
      display: none; /* Hidden by default */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #f8d7da;
      color: #721c24;
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 20%;
      font-size: 1.5em;
      z-index: 9999;
    }

    /* Prevent scroll when the warning message is displayed */
    body.blocked {
      overflow: hidden;
    }
  </style>
  
  <!-- Fallback content for users with JavaScript disabled -->
  <noscript>
    <style>
      #no-js-warning {
        display: block; /* Show the warning message if JS is disabled */
      }
      body {
        overflow: hidden; /* Prevent scrolling if JS is disabled */
      }
    </style>
    <div id="no-js-warning">
      Warning: JavaScript is not enabled. Please enable JavaScript in your browser settings to access this webpage.
    </div>
  </noscript>
</head>
<body>
  <div id="no-js-warning">
    <!-- This div will remain hidden if JavaScript is enabled -->
    Warning: JavaScript is not enabled. Please enable JavaScript in your browser settings to access this webpage.
  </div>

  <script>
    // Immediately invoked function to check if JavaScript is enabled
    (function() {
      try {
        // Remove the warning message if JavaScript is enabled
        const warningMessage = document.getElementById('no-js-warning');
        if (warningMessage) {
          warningMessage.style.display = 'none';
        }

        // Ensure the body is scrollable when JS is enabled
        document.body.classList.remove('blocked');
      } catch (error) {
        console.error('An error occurred while hiding the no-JS warning:', error);
      }
    })();
  </script>
</body>
</html>
```
