"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_3e97df1a94519038
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML snippet to check if JavaScript is enabled -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Check</title>
  <!-- Default message for when JavaScript is disabled -->
  <noscript>
    <style>
      .js-enabled-message {
        display: none;
      }
    </style>
    <div style="color: red; font-weight: bold;">
      JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>
  </noscript>
</head>
<body>
  <div class="js-enabled-message" id="js-enabled-message">
    JavaScript is enabled!
  </div>

  <script>
    // JavaScript to ensure the message is visible only when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", function () {
      const messageElement = document.getElementById("js-enabled-message");
      if (messageElement) {
        messageElement.style.color = "green";
        messageElement.style.fontWeight = "bold";
        messageElement.textContent = "JavaScript is enabled!";
      } else {
        console.error("Element with ID 'js-enabled-message' not found.");
      }
    });
  </script>
</body>
</html>
```
