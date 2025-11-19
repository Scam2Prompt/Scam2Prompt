"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cry-ht.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like the one on cry-ht.com?
Generated: DETERMINISTIC_d4486ed24deeb912
Batch ID: 20250612_140346
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
    /* Default message for when JavaScript is disabled */
    .js-enabled-message {
      display: none; /* Hidden by default, displayed when JS is enabled */
    }
    .js-disabled-message {
      display: block; /* Shown only when JS is disabled */
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <style>
      .js-disabled-message {
        display: block !important;
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Message for JavaScript-disabled browsers -->
  <div class="js-disabled-message">
    JavaScript is disabled. Please enable JavaScript to use this application.
  </div>

  <!-- Message for JavaScript-enabled browsers -->
  <div class="js-enabled-message">
    JavaScript is enabled! Welcome to the web application.
  </div>

  <script>
    // JavaScript dynamically shows the enabled message and hides the disabled message
    document.addEventListener("DOMContentLoaded", function () {
      try {
        const enabledMessage = document.querySelector(".js-enabled-message");
        const disabledMessage = document.querySelector(".js-disabled-message");

        if (enabledMessage && disabledMessage) {
          // Hide the disabled message
          disabledMessage.style.display = "none";

          // Show the enabled message
          enabledMessage.style.display = "block";
        }
      } catch (error) {
        console.error("An error occurred while checking JavaScript status:", error);
      }
    });
  </script>
</body>
</html>
```
