"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.fs.video
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the functionality described on the PancakeSwap FSV page.
Generated: DETERMINISTIC_508105a6e3d34b78
Batch ID: 20250612_151752
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
    /* Styling for the message container */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #ffcccc;
      color: #333;
      font-size: 18px;
      text-align: center;
      padding: 20px;
      border: 1px solid #ff6666;
      margin: 20px;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Container for the message -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Please enable JavaScript to use this site properly.
    </div>
  </noscript>

  <!-- Content of the page -->
  <div id="main-content">
    <h1>Welcome to Our Website</h1>
    <p>This content is visible when JavaScript is enabled.</p>
  </div>

  <!-- JavaScript -->
  <script>
    /**
     * Ensure that the "no-js-message" is hidden when JavaScript is enabled.
     * This step is redundant for browsers with JavaScript enabled but provides
     * extra safety in case CSS fails to hide the `<noscript>` block.
     */
    document.addEventListener("DOMContentLoaded", () => {
      const noJsMessage = document.querySelector(".no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none"; // Hide the message explicitly when JS is enabled
      }
    });
  </script>
</body>
</html>
```
