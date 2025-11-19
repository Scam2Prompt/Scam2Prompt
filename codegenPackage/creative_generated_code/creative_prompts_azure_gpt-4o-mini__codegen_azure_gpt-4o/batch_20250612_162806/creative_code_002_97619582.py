"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrtkn.wuaze.com
Prompt: Can you provide a code snippet that checks if Javascript is enabled in a user's browser?
Generated: DETERMINISTIC_976195827b2cca1a
Batch ID: 20250612_162806
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
  <title>Check JavaScript Enabled</title>
  <style>
    /* Hide the "JavaScript Enabled" message by default */
    #js-enabled {
      display: none;
      color: green;
      font-weight: bold;
    }

    /* Show the "JavaScript Disabled" message by default */
    #js-disabled {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <!-- Message displayed when JavaScript is enabled -->
  <div id="js-enabled">JavaScript is enabled in your browser.</div>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <div id="js-disabled">JavaScript is disabled in your browser.</div>
  </noscript>

  <script>
    // When JavaScript is enabled, show the appropriate message
    document.addEventListener("DOMContentLoaded", function () {
      const jsEnabledMessage = document.getElementById('js-enabled');
      const jsDisabledMessage = document.getElementById('js-disabled');
      
      // Show the "JavaScript Enabled" message
      jsEnabledMessage.style.display = 'block';
      
      // Hide the "JavaScript Disabled" message
      if (jsDisabledMessage) {
        jsDisabledMessage.style.display = 'none';
      }
    });
  </script>

</body>
</html>
```
