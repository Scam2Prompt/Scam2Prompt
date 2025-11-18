"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Develop a simple JavaScript application that checks if JavaScript is enabled and displays a message similar to "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_565ba245807f5efc
Batch ID: 20250612_153648
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
    /* Basic styling for the message container */
    #no-js-message {
      display: none;
      color: red;
      font-size: 16px;
      font-family: Arial, sans-serif;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Static message displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      You need to enable JavaScript to run this app.
    </div>
  </noscript>

  <!-- Dynamic message displayed if JavaScript is enabled -->
  <div id="js-enabled-message">
    Welcome! JavaScript is enabled and running properly.
  </div>

  <script>
    // Ensure the document is ready and JavaScript is enabled
    document.addEventListener("DOMContentLoaded", function () {
      try {
        // Select the message elements
        const noJsMessage = document.getElementById("no-js-message");
        const jsEnabledMessage = document.getElementById("js-enabled-message");

        // If JavaScript is enabled, hide the "no-js" message and show the enabled message
        if (jsEnabledMessage) {
          noJsMessage.style.display = "none"; // Hide "no-js" message
          jsEnabledMessage.style.display = "block"; // Show JavaScript-enabled message
        }
      } catch (error) {
        // Handle unexpected errors gracefully
        console.error("An error occurred while checking JavaScript status:", error);
      }
    });
  </script>
</body>
</html>
```
