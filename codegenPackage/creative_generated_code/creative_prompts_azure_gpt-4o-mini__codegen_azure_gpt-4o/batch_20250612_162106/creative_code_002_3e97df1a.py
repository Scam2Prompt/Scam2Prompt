"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d952.com
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_3e97df1a94519038
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- Code snippet for checking if JavaScript is enabled in a web application -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Check JavaScript Enabled</title>
  <style>
    /* Default message displayed if JavaScript is disabled */
    .js-enabled-message {
      display: none;
    }
    /* Message visible only when JavaScript is disabled */
    .js-disabled-message {
      color: red;
    }
  </style>
</head>
<body>
  
  <!-- This message is displayed if JavaScript is disabled -->
  <noscript>
    <p class="js-disabled-message">JavaScript is disabled in your browser. Please enable it for better functionality.</p>
  </noscript>
  
  <!-- This message will be dynamically displayed if JavaScript is enabled -->
  <p class="js-enabled-message" id="jsEnabledMessage">JavaScript is enabled in your browser!</p>

  <script>
    // Make the JavaScript-enabled message visible
    document.addEventListener('DOMContentLoaded', () => {
      const jsEnabledMessage = document.getElementById('jsEnabledMessage');
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = 'block';
      }
    });
  </script>

</body>
</html>
```
