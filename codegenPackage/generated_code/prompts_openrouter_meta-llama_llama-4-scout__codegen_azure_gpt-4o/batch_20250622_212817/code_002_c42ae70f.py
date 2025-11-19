"""
Generated Code Metadata:
========================
Original URL: https://celestiacelestia.com
Prompt: Generate a simple webpage that displays a customizable message when JavaScript is disabled, similar to the one found at https://celestiacelestia.com.
Generated: DETERMINISTIC_c42ae70f88316843
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Disabled Message</title>
  <style>
    /* Basic styling for the message */
    .no-js-message {
      display: none; /* Hidden by default */
      background-color: #f8d7da;
      color: #721c24;
      padding: 20px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      text-align: center;
      font-family: Arial, sans-serif;
      margin: 20px;
    }
  </style>
</head>
<body>
  <!-- Message to display when JavaScript is disabled -->
  <div class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to view this webpage properly.
  </div>

  <script>
    // JavaScript to hide the message when JavaScript is enabled
    document.addEventListener('DOMContentLoaded', function () {
      const noJsMessage = document.querySelector('.no-js-message');
      if (noJsMessage) {
        noJsMessage.style.display = 'none'; // Hide the message
      }
    });
  </script>

  <noscript>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <style>
      .no-js-message {
        display: block; /* Show the message if JavaScript is disabled */
      }
    </style>
  </noscript>
</body>
</html>
```
