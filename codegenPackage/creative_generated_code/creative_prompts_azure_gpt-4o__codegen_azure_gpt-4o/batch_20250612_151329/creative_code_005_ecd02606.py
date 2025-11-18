"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdddd.pages.dev
Prompt: Provide code to enable JavaScript detection and display a message prompting users to enable JavaScript, similar to the functionality described on the chimpers-dojo website.
Generated: DETERMINISTIC_ecd02606cf3c16cf
Batch ID: 20250612_151329
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
  <title>Enable JavaScript Detection</title>
  <style>
    /* Style for the message to appear when JavaScript is disabled */
    .no-js-message {
      display: none; /* Hidden by default, shown if JavaScript is disabled */
      color: #ffffff;
      background-color: #ff0000;
      padding: 20px;
      text-align: center;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to view this site properly.
  </div>

  <noscript>
    <!-- Fallback message if JavaScript is disabled -->
    <style>
      .no-js-message {
        display: block; /* Show message if JavaScript is disabled */
      }
    </style>
  </noscript>

  <script>
    // Ensure the no-js-message is hidden when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", function () {
      const noJsMessage = document.querySelector(".no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none"; // Hide message as JavaScript is enabled
      }
    });
  </script>
</body>
</html>
```
