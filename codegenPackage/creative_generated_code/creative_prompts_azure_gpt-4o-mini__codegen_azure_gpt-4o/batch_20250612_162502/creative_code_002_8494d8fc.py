"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collab-land.de
Prompt: Can you provide code examples for detecting if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_8494d8fc428334b8
Batch ID: 20250612_162502
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
  <title>JavaScript Detection Example</title>
  <style>
    /* This message is shown only if JavaScript is disabled */
    .no-js {
      display: block;
      color: red;
      font-weight: bold;
    }

    /* This message is hidden by JavaScript */
    .js-enabled {
      display: none;
    }
  </style>
</head>
<body>

  <!-- Message shown if JavaScript is disabled -->
  <p class="no-js">JavaScript is disabled in your browser.</p>

  <!-- Message to be shown if JavaScript is enabled -->
  <p class="js-enabled">JavaScript is enabled in your browser.</p>

  <script>
    // JavaScript code to hide the "no-js" message and show the "js-enabled" message
    document.addEventListener("DOMContentLoaded", () => {
      // Select the elements by their class names
      const noJsMessage = document.querySelector(".no-js");
      const jsEnabledMessage = document.querySelector(".js-enabled");

      // Hide the "no-js" message and show the "js-enabled" message
      if (noJsMessage) noJsMessage.style.display = "none";
      if (jsEnabledMessage) jsEnabledMessage.style.display = "block";
    });
  </script>

</body>
</html>
```
