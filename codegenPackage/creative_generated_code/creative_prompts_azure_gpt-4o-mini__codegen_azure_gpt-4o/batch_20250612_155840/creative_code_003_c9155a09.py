"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.eu
Prompt: How do I create a fallback message for users without JavaScript enabled on my website?
Generated: DETERMINISTIC_c9155a0964f37808
Batch ID: 20250612_155840
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
  <title>Fallback Message for No JavaScript</title>
  <style>
    /* Style for the no-JS fallback message */
    .no-js-message {
      font-family: Arial, sans-serif;
      color: #ffffff;
      background-color: #ff0000;
      padding: 10px;
      text-align: center;
      border: 1px solid #cc0000;
      border-radius: 5px;
      margin: 20px auto;
      max-width: 600px;
    }
    /* Hide the fallback message when JavaScript is enabled */
    .no-js-message {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Fallback message for users without JavaScript enabled -->
  <noscript>
    <div class="no-js-message">
      JavaScript is disabled in your browser. Some features of this website may not work properly. Please enable JavaScript for the best experience.
    </div>
  </noscript>

  <!-- Content for users with JavaScript enabled -->
  <div id="main-content">
    <!-- Main content of the website -->
    <h1>Welcome to Our Website!</h1>
    <p>If you're seeing this, JavaScript is enabled and everything is working as intended.</p>
  </div>

  <!-- Optional JavaScript code -->
  <script>
    // Error handling: Ensure the DOM is fully loaded before running JavaScript
    document.addEventListener("DOMContentLoaded", function () {
      try {
        // Example: JavaScript functionality can be added here
        console.log("JavaScript is enabled, and the page is fully loaded.");
      } catch (error) {
        console.error("An error occurred:", error);
      }
    });
  </script>
</body>
</html>
```
