"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Provide a code example that detects JavaScript support in browsers and displays a message if it's disabled.
Generated: DETERMINISTIC_774d632d75b6a6d4
Batch ID: 20250612_160158
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
  <style>
    /* Default message for browsers where JavaScript is disabled */
    #no-js-message {
      display: none; /* Hidden by default */
      color: red;
      font-size: 18px;
      font-weight: bold;
    }
  </style>
  <noscript>
    <!-- This block is rendered only if JavaScript is disabled -->
    <style>
      #no-js-message {
        display: block;
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Message shown if JavaScript is disabled -->
  <div id="no-js-message">
    JavaScript is disabled in your browser. Please enable it for the best experience.
  </div>

  <!-- JavaScript initialization -->
  <script>
    // JavaScript will automatically hide the "no-js-message" if it runs successfully.
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none"; // Hide the message if JavaScript is enabled
      }
    });
  </script>
</body>
</html>
```
