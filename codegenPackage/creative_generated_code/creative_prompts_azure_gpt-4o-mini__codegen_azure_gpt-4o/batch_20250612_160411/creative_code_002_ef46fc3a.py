"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbgemcredentialorg.web.app
Prompt: Can you provide a code snippet for checking if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_ef46fc3a399dca52
Batch ID: 20250612_160411
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
    /* Initially hide the content that depends on JavaScript */
    .js-enabled {
      display: none;
    }
  </style>
</head>
<body>
  <noscript>
    <!-- Content to display when JavaScript is disabled -->
    <div style="color: red; font-weight: bold;">
      JavaScript is disabled in your browser. Please enable it to use this application.
    </div>
  </noscript>

  <!-- Content that requires JavaScript -->
  <div class="js-enabled">
    <p>JavaScript is enabled! Welcome to the application.</p>
  </div>

  <script>
    // When JavaScript is enabled, show elements that depend on it
    document.addEventListener('DOMContentLoaded', () => {
      const jsEnabledContent = document.querySelector('.js-enabled');
      if (jsEnabledContent) {
        // Display the content only if JavaScript is enabled
        jsEnabledContent.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
