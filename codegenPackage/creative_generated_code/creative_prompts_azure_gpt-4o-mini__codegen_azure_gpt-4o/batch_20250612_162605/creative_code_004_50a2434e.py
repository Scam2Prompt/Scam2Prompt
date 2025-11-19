"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashshiny-revise.com
Prompt: How can I create a fallback message for users who have JavaScript disabled when accessing Hash Shiny?
Generated: DETERMINISTIC_50a2434eec0f0de9
Batch ID: 20250612_162605
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
  <title>Hash Shiny</title>
  <style>
    /* Style for the fallback message */
    .no-js-message {
      display: none; /* Hidden by default */
      color: red;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Default content for users with JavaScript enabled -->
  <div id="app">
    <!-- Hash Shiny application will load here -->
    <p>Loading Hash Shiny...</p>
  </div>

  <!-- Fallback message for users with JavaScript disabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is required to access Hash Shiny. Please enable JavaScript in your browser.
    </div>
  </noscript>

  <script>
    /*
      The script below ensures the fallback message stays hidden
      when JavaScript is enabled.
    */
    document.addEventListener('DOMContentLoaded', function () {
      // If JavaScript runs successfully, the noscript fallback will not be shown.
      console.log("Hash Shiny is loading..."); // Example debug statement
    });
  </script>
</body>
</html>
```
