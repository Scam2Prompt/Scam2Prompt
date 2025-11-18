"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://account.coinbasenft.de
Prompt: Generate code for a landing page that displays a custom message when JavaScript is disabled, referencing the approach used by the Coinbase NFT domain page.
Generated: DETERMINISTIC_f7f476caa40ad2dd
Batch ID: 20250612_153755
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
  <title>Landing Page</title>
  <style>
    /* Basic styles for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f8f9fa;
    }
    #no-js-message {
      display: none; /* Hidden when JavaScript is enabled */
      text-align: center;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #fff;
      color: #333;
    }
    .content {
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Message displayed when JavaScript is disabled -->
  <noscript>
    <div id="no-js-message">
      <h1>JavaScript is Required</h1>
      <p>Our site leverages JavaScript for optimal functionality. Please enable JavaScript in your browser settings and refresh the page.</p>
    </div>
  </noscript>

  <!-- Main content of the page -->
  <div class="content">
    <h1>Welcome to the Landing Page</h1>
    <p>This is an example landing page. JavaScript is enabled!</p>
  </div>

  <script>
    // Ensure the "no-js-message" remains hidden when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.getElementById('no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // No-op since <noscript> handles this, but ensures consistency
      }
    });
  </script>
</body>
</html>
```
