"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Generate code to enable JavaScript-based functionality for a web application that displays a warning message when JavaScript is disabled, inspired by the mtec.cyou webpage.
Generated: DETERMINISTIC_bdd0c163f6c2a56f
Batch ID: 20250612_150446
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
  <title>JavaScript Warning</title>
  <style>
    /* Styles for the warning message */
    .no-js-warning {
      display: none; /* Hidden by default, unless JavaScript is disabled */
      background-color: #ffcc00;
      color: #333;
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 15px;
      border: 1px solid #e6a700;
      border-radius: 5px;
      margin: 15px;
    }
  </style>
  <noscript>
    <!-- Message displayed when JavaScript is disabled -->
    <style>
      .no-js-warning { 
        display: block; /* Override to display the warning message */
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Warning message -->
  <div class="no-js-warning">
    Warning: JavaScript is disabled in your browser. This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
  </div>

  <script>
    // Self-contained JavaScript to ensure the warning message is hidden when JavaScript is enabled
    (function() {
      try {
        // Locate the warning message element
        const warningMessage = document.querySelector('.no-js-warning');
        
        // Ensure the element exists before trying to manipulate it
        if (warningMessage) {
          // Hide the warning message as JavaScript is enabled
          warningMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any unexpected errors
        console.error('An error occurred while hiding the warning message:', error);
      }
    })();
  </script>
</body>
</html>
```
