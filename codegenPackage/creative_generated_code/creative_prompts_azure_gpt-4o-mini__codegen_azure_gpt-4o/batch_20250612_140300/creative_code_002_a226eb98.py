"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aimining6.cc
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_140300
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
</head>
<body>
  <!-- Message displayed if JavaScript is enabled -->
  <div id="js-enabled" style="display: none;">
    JavaScript is enabled in your browser.
  </div>

  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div id="js-disabled">
      JavaScript is disabled in your browser. Please enable it to continue.
    </div>
  </noscript>

  <script>
    /**
     * Check if JavaScript is enabled.
     * If JavaScript is enabled, this script will execute and
     * display the relevant message.
     */
    document.addEventListener("DOMContentLoaded", () => {
      try {
        // Show the JavaScript-enabled message
        const jsEnabledDiv = document.getElementById("js-enabled");
        if (jsEnabledDiv) {
          jsEnabledDiv.style.display = "block";
        }
      } catch (error) {
        console.error("An error occurred while checking JavaScript status:", error);
      }
    });
  </script>
</body>
</html>
```
