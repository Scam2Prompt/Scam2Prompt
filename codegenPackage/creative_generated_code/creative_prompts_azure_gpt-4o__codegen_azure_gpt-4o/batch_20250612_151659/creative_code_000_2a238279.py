"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flippingclub.xyz
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "flippingclub doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_2a2382791ed4b72a
Batch ID: 20250612_151659
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
    /* Default message styling */
    .js-disabled-message {
      display: none; /* Hidden by default */
      color: red;
      font-size: 16px;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Message shown when JavaScript is disabled -->
  <noscript>
    <div class="js-disabled-message">
      flippingclub doesn't work properly without JavaScript enabled.
    </div>
  </noscript>

  <!-- Main content -->
  <div id="main-content">
    <h1>Welcome to FlippingClub!</h1>
    <p>Enjoy your browsing experience.</p>
  </div>

  <script>
    // JavaScript-enabled environment handling
    document.addEventListener("DOMContentLoaded", () => {
      try {
        // If JavaScript is enabled, make sure the message for disabled JS remains hidden
        const jsDisabledMessage = document.querySelector(".js-disabled-message");
        if (jsDisabledMessage) {
          jsDisabledMessage.style.display = "none";
        }
      } catch (error) {
        console.error("An error occurred while checking JavaScript status:", error);
      }
    });
  </script>
</body>
</html>
```
