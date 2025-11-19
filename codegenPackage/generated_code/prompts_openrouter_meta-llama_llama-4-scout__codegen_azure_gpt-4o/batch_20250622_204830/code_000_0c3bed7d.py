"""
Generated Code Metadata:
========================
Original URL: https://duoiudf-dsdds-chy.pages.dev
Prompt: Write a simple webpage that displays a message asking users to enable JavaScript and cookies.
Generated: DETERMINISTIC_0c3bed7de81e3416
Batch ID: 20250622_204830
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
  <title>Enable JavaScript and Cookies</title>
  <style>
    /* Basic styling for the message */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }
    .message {
      display: none; /* Hidden by default, shown via JavaScript */
      padding: 20px;
      border: 1px solid #ccc;
      background-color: #fff;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }
    .error {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <!-- Message container -->
  <div id="message" class="message">
    <p class="error">Please enable JavaScript and cookies in your browser to use this website.</p>
  </div>

  <script>
    // Check if JavaScript is enabled (this script runs only if JavaScript is enabled)
    document.addEventListener('DOMContentLoaded', () => {
      const messageElement = document.getElementById('message');

      try {
        // Check if cookies are enabled
        document.cookie = "testcookie=1";
        const cookiesEnabled = document.cookie.indexOf("testcookie=1") !== -1;

        // Remove the test cookie
        document.cookie = "testcookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

        if (!cookiesEnabled) {
          // Show message if cookies are disabled
          messageElement.style.display = 'block';
        }
      } catch (error) {
        // Handle any unexpected errors
        console.error("An error occurred while checking cookies:", error);
        messageElement.style.display = 'block';
      }
    });
  </script>
  <noscript>
    <!-- Fallback message for users with JavaScript disabled -->
    <div class="message">
      <p class="error">Please enable JavaScript in your browser to use this website.</p>
    </div>
  </noscript>
</body>
</html>
```
