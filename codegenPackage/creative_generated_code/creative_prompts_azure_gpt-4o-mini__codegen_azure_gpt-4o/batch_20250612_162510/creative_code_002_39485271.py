"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link.sv
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_162510
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
  <noscript>
    <!-- This message will display if JavaScript is disabled -->
    <style>
      .js-enabled-message {
        display: none;
      }
    </style>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>
  </noscript>
  <style>
    /* Default styles for when JavaScript is enabled */
    .js-enabled-message {
      display: block;
      color: green;
      font-size: 1.2em;
    }

    /* Fallback styles handled in <noscript> for when JavaScript is disabled */
    .no-js-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Message for users when JavaScript is enabled -->
  <div class="js-enabled-message">
    JavaScript is enabled in your browser. You can fully use this application.
  </div>

  <script>
    // Ensure that the <noscript> fallback message is hidden correctly
    // Browser will automatically handle showing/hiding these sections
    window.addEventListener("DOMContentLoaded", () => {
      console.log("JavaScript is enabled and working correctly.");
    });
  </script>
</body>
</html>
```
