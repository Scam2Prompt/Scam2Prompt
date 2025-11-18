"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.world
Prompt: Write code to detect whether JavaScript is enabled in a browser and display a message prompting users to enable it for accessing the "Polkadot Go - POAP Hunt" app.
Generated: DETERMINISTIC_dfdfbe42827d9921
Batch ID: 20250612_142620
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
  <title>Polkadot Go - POAP Hunt</title>
  <style>
    /* Simple styling for the no-JavaScript message */
    #no-js-message {
      display: none; /* Hidden by default */
      font-family: Arial, sans-serif;
      font-size: 16px;
      color: red;
      text-align: center;
      margin-top: 20px;
    }
  </style>
  <noscript>
    <!-- Fallback message shown when JavaScript is disabled -->
    <style>
      #no-js-message {
        display: block; /* Display the message if JavaScript is disabled */
      }
    </style>
  </noscript>
</head>
<body>
  <!-- Content of the app -->
  <div id="app">
    <h1>Welcome to Polkadot Go - POAP Hunt</h1>
    <p>Enjoy the hunt for POAP tokens!</p>
  </div>

  <!-- Message displayed if JavaScript is disabled -->
  <div id="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to fully access the Polkadot Go - POAP Hunt app.
  </div>

  <script>
    // JavaScript code to ensure the message is hidden when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      try {
        const noJsMessage = document.getElementById("no-js-message");
        if (noJsMessage) {
          // Hide the no-JavaScript message explicitly when JavaScript is detected
          noJsMessage.style.display = "none";
        }
      } catch (error) {
        console.error("An error occurred while checking JavaScript state:", error);
      }
    });
  </script>
</body>
</html>
```
