"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imptp.com
Prompt: How do I create a fallback for users who have JavaScript disabled on their mobile devices?
Generated: DETERMINISTIC_ef3764e1354d3871
Batch ID: 20250612_163840
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
  <title>JavaScript Fallback Example</title>
  <style>
    /* Styles for the fallback message */
    .no-js-message {
      display: none; /* Default to hidden when JavaScript is enabled */
      color: #ff0000; /* Red text to draw attention */
      font-size: 1.2em;
      margin: 20px;
    }
  </style>
  <noscript>
    <!-- Fallback message for users with JavaScript disabled -->
    <style>
      .no-js-message {
        display: block; /* Show fallback message if JavaScript is disabled */
      }
    </style>
  </noscript>
</head>
<body>
  <div id="app">
    <!-- Main content that requires JavaScript -->
    <h1>Welcome to Our Website</h1>
    <p>This content is enhanced with JavaScript.</p>
  </div>

  <!-- Fallback message for users without JavaScript -->
  <div class="no-js-message">
    <p>It appears that JavaScript is disabled on your device. Please enable JavaScript or use a browser that supports it for the best experience.</p>
  </div>

  <script>
    // JavaScript is enabled, ensure fallback is hidden
    document.addEventListener("DOMContentLoaded", () => {
      const fallbackMessage = document.querySelector(".no-js-message");
      if (fallbackMessage) {
        fallbackMessage.style.display = "none"; // Hide fallback message explicitly
      }
    });
  </script>
</body>
</html>
```
