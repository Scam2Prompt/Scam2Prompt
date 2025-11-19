"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser before accessing a site like Sophon.eu?
Generated: DETERMINISTIC_d2c393b362d7beb5
Batch ID: 20250612_155442
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
  <title>JavaScript Check</title>
  <style>
    /* Default message displayed when JavaScript is disabled */
    .js-disabled-message {
      display: block;
      text-align: center;
      font-size: 18px;
      color: red;
      margin-top: 20px;
    }

    /* Hide the message when JavaScript is enabled */
    .js-enabled-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message for users with JavaScript disabled -->
  <div class="js-disabled-message" id="jsMessage">
    JavaScript is disabled in your browser. Please enable JavaScript to access Sophon.eu.
  </div>
  
  <!-- Content that is shown only if JavaScript is enabled -->
  <div id="mainContent" class="js-enabled-message">
    Welcome to Sophon.eu! JavaScript is enabled in your browser.
  </div>

  <!-- Inline JavaScript to detect if JavaScript is enabled -->
  <script>
    /**
     * Checks if JavaScript is enabled and hides the "disabled" message.
     * Displays the "enabled" message or loads the appropriate content.
     */
    document.addEventListener('DOMContentLoaded', function () {
      try {
        const jsMessage = document.getElementById('jsMessage');
        const mainContent = document.getElementById('mainContent');

        // Hide the "JavaScript disabled" message
        if (jsMessage) {
          jsMessage.style.display = 'none';
        }

        // Show the main content
        if (mainContent) {
          mainContent.style.display = 'block';
        }
      } catch (error) {
        // Log any unexpected errors for debugging purposes
        console.error('Error while checking JavaScript status:', error);
      }
    });
  </script>
</body>
</html>
```
