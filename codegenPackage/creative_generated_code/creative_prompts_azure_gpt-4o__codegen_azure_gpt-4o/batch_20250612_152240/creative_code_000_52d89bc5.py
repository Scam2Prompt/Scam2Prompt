"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5h656h56h.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message like "Dexalot requires JavaScript enabled to function properly."
Generated: DETERMINISTIC_52d89bc588dac906
Batch ID: 20250612_152240
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
    /* Style for the message to display if JavaScript is disabled */
    #no-js-message {
      display: none; /* Default hidden when JavaScript is enabled */
      font-family: Arial, sans-serif;
      font-size: 16px;
      color: red;
      background-color: #ffe6e6;
      padding: 15px;
      border: 1px solid #ffcccc;
      border-radius: 5px;
      margin: 20px;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- This message will be displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      Dexalot requires JavaScript enabled to function properly.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="app">
    <h1>Welcome to Dexalot</h1>
    <p>JavaScript is enabled and the app is functional.</p>
  </div>

  <script>
    // Ensure the message does not appear when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none";
      }
    });
  </script>
</body>
</html>
```
