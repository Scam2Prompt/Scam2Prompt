"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.consesys.io
Prompt: Can you provide a code snippet to detect if JavaScript is enabled in a user's browser for a web application?
Generated: DETERMINISTIC_5d4f64f799f26345
Batch ID: 20250612_155122
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
  <title>JavaScript Detection</title>
</head>
<body>
  <!-- This message will be displayed if JavaScript is disabled -->
  <noscript>
    <div style="color: red; font-weight: bold;">
      JavaScript is disabled in your browser. Please enable it to use this application.
    </div>
  </noscript>

  <!-- This message will be displayed if JavaScript is enabled -->
  <div id="js-enabled-message" style="display: none;">
    JavaScript is enabled in your browser.
  </div>

  <script>
    // Check if JavaScript is enabled by showing the message in the <div>
    try {
      const jsEnabledMessage = document.getElementById("js-enabled-message");
      if (jsEnabledMessage) {
        jsEnabledMessage.style.display = "block"; // Display the message if JavaScript is enabled
      }
    } catch (error) {
      console.error("An error occurred while detecting JavaScript:", error);
    }
  </script>
</body>
</html>
```
