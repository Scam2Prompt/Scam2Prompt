"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethxoo.com
Prompt: Create a script that checks if JavaScript is enabled in a user's browser and displays a warning message if it is disabled, tailored for a cryptocurrency pledge platform.
Generated: DETERMINISTIC_f0ef027a43a9c2ab
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML Document -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Crypto Pledge Platform</title>
  <style>
    /* Style for the warning message */
    .no-js-warning {
      display: none; /* Hidden by default, displayed only when JavaScript is disabled */
      background-color: #f44336; /* Red background for emphasis */
      color: #fff;
      padding: 15px;
      text-align: center;
      font-size: 1.2em;
      border: 1px solid #d32f2f;
      border-radius: 5px;
      margin: 20px auto;
      max-width: 600px;
    }
  </style>
</head>
<body>
  <!-- Warning message displayed only if JavaScript is disabled -->
  <div class="no-js-warning">
    JavaScript is disabled in your browser. This platform requires JavaScript to function properly. Please enable JavaScript to continue.
  </div>

  <script>
    /**
     * JavaScript code to hide the warning message if JavaScript is enabled.
     * If the script runs, it means JavaScript is enabled, and the warning is not needed.
     */
    document.addEventListener('DOMContentLoaded', function () {
      try {
        // Select the warning message element
        const warningMessage = document.querySelector('.no-js-warning');
        
        if (warningMessage) {
          // Hide the warning message since JavaScript is enabled
          warningMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any errors that occur (should be rare)
        console.error('An error occurred while checking JavaScript status:', error);
      }
    });
  </script>
</body>
</html>
```
