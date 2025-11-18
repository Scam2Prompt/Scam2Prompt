"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdzv.com
Prompt: Generate code to detect if JavaScript is disabled on a user's browser and display a message instructing them to enable it for accessing a Bitcoin pledge platform.
Generated: DETERMINISTIC_7d724129d23288ad
Batch ID: 20250612_152600
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
  <title>Bitcoin Pledge Platform</title>
  <style>
    /* Style for the "JavaScript Disabled" message */
    #js-disabled-message {
      display: none; /* Hidden by default, will only show if JS is disabled */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
    #content {
      display: none; /* Content is hidden if JS is disabled */
    }
  </style>
</head>
<body>
  <!-- Message to display if JavaScript is disabled -->
  <noscript>
    <div id="js-disabled-message">
      JavaScript is disabled in your browser. Please enable it to access the Bitcoin pledge platform.
    </div>
  </noscript>

  <!-- Main content of the application -->
  <div id="content">
    <h1>Welcome to the Bitcoin Pledge Platform</h1>
    <p>This platform requires JavaScript to function properly. Thank you for enabling it!</p>
  </div>

  <script>
    // Ensure the content is visible only when JavaScript is enabled
    document.addEventListener("DOMContentLoaded", () => {
      const contentElement = document.getElementById("content");
      if (contentElement) {
        contentElement.style.display = "block"; // Show content since JS is enabled
      }
    });
  </script>
</body>
</html>
```
