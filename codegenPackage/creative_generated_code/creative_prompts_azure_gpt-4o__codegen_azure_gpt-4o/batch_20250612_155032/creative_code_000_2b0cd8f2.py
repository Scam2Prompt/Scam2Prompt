"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.coinbasenft.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
Batch ID: 20250612_155032
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
  <title>JavaScript Disabled Detection</title>
  <style>
    /* Style for the message displayed when JavaScript is disabled */
    #no-js-message {
      display: none; /* Hidden by default */
      color: red;
      font-size: 18px;
      font-weight: bold;
      background-color: #ffe6e6;
      padding: 10px;
      border: 1px solid red;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Message displayed if JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Content of the page -->
  <h1>Welcome to My Website</h1>
  <p>This is a sample page to demonstrate JavaScript detection.</p>

  <script>
    // JavaScript block that ensures the message is not visible when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      // Locate the message element (should exist only within <noscript>)
      const noJsMessage = document.getElementById('no-js-message');
      // Ensure the message remains hidden if JavaScript is enabled
      if (noJsMessage) {
        noJsMessage.style.display = 'none';
      }
    });
  </script>
</body>
</html>
```
