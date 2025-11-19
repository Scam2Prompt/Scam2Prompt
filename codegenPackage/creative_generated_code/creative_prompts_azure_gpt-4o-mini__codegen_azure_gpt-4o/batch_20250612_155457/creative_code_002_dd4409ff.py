"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwwq.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser for the ETH Pledge platform?
Generated: DETERMINISTIC_dd4409ffbda18c9d
Batch ID: 20250612_155457
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
  <title>ETH Pledge Platform</title>
  <style>
    /* Default style when JavaScript is disabled */
    .js-enabled-message {
      display: none;
    }

    .no-js-message {
      display: block;
      color: red;
    }
  </style>
  <script>
    // When JavaScript is enabled, hide the "no-js" message and show the "js-enabled" message
    document.addEventListener("DOMContentLoaded", function () {
      const noJsMessage = document.getElementById("no-js-message");
      const jsEnabledMessage = document.getElementById("js-enabled-message");

      // Error handling to ensure elements exist before manipulating DOM
      if (noJsMessage && jsEnabledMessage) {
        noJsMessage.style.display = "none"; // Hide the "JavaScript Disabled" message
        jsEnabledMessage.style.display = "block"; // Show the "JavaScript Enabled" message
      }
    });
  </script>
</head>

<body>
  <!-- Message displayed if JavaScript is disabled -->
  <div id="no-js-message" class="no-js-message">
    JavaScript is disabled in your browser. Please enable it to use the ETH Pledge platform.
  </div>

  <!-- Message displayed if JavaScript is enabled -->
  <div id="js-enabled-message" class="js-enabled-message">
    JavaScript is enabled! Welcome to the ETH Pledge platform.
  </div>
</body>

</html>
```
