"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1046049845.pages.dev
Prompt: Can you provide code snippets to check if JavaScript is enabled in a browser?
Generated: DETERMINISTIC_4dc0daab1549b7bd
Batch ID: 20250612_160940
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
  <title>JavaScript Enabled Check</title>
  <style>
    /* This message will be shown if JavaScript is disabled */
    .no-js-message {
      display: none;
      color: red;
      font-weight: bold;
    }
  </style>
  <script>
    // If JavaScript is enabled, hide the no-js message
    document.addEventListener('DOMContentLoaded', () => {
      const message = document.getElementById('no-js-message');
      if (message) {
        message.style.display = 'none'; // Hide the no-js message
      }
    });
  </script>
</head>
<body>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <div id="no-js-message" class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript for full functionality.
    </div>
  </noscript>

  <!-- Content visible if JavaScript is enabled -->
  <div>
    <h1>Welcome!</h1>
    <p>If you're seeing this, JavaScript is enabled in your browser.</p>
  </div>
</body>
</html>
```
