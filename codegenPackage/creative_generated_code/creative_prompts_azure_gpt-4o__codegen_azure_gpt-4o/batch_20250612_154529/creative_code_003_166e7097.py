"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixdrop.eu
Prompt: Write a script to display a warning message when JavaScript is disabled, ensuring it works on both desktop and mobile browsers.
Generated: DETERMINISTIC_166e7097975457a2
Batch ID: 20250612_154529
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
    /* Warning message styling */
    .no-js-warning {
      display: none; /* Initially hide the warning, JavaScript will remove this */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      background-color: #ffcccb; /* Light red background for warning */
      color: #000; /* Black text for visibility */
      text-align: center;
      padding: 10px 0;
      font-size: 16px;
      font-family: Arial, sans-serif;
      z-index: 1000; /* Ensure it appears above other content */
    }
  </style>
  <noscript>
    <!-- This block will display if JavaScript is disabled -->
    <style>
      .no-js-warning {
        display: block; /* Show the warning when JavaScript is disabled */
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Warning message container -->
  <div class="no-js-warning">
    Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
  </div>

  <!-- Your main content -->
  <div>
    <h1>Welcome to the Website</h1>
    <p>This is the main content of the site.</p>
  </div>

  <script>
    // JavaScript for removing the warning when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Locate the warning element
        const warningElement = document.querySelector('.no-js-warning');

        // Ensure the element exists before attempting to hide it
        if (warningElement) {
          warningElement.style.display = 'none'; // Hide the warning
        }
      } catch (error) {
        // Log any unexpected errors
        console.error('Error handling JavaScript warning:', error);
      }
    });
  </script>
</body>
</html>
```
