"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoz999.pages.dev
Prompt: Provide a code snippet that prompts users to enable JavaScript and cookies if they are disabled.
Generated: DETERMINISTIC_95f1c559d8b4e3c7
Batch ID: 20250612_155905
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
  <title>Enable JavaScript and Cookies</title>
  <style>
    /* Styling for the error messages */
    .message {
      font-family: Arial, sans-serif;
      color: red;
      font-size: 1.2em;
      margin: 20px;
      border: 1px solid red;
      padding: 10px;
      background-color: #ffe6e6;
    }
  </style>
  <noscript>
    <!-- Message displayed if JavaScript is disabled -->
    <div class="message">
      JavaScript is disabled in your browser. Please enable JavaScript to continue using this website.
    </div>
  </noscript>
</head>
<body>
  <div id="cookieMessage" class="message" style="display: none;">
    <!-- Message displayed if cookies are disabled -->
    Cookies are disabled or blocked in your browser. Please enable cookies to continue using this website.
  </div>

  <script>
    // Check if cookies are enabled
    function areCookiesEnabled() {
      try {
        // Attempt to set and read a test cookie
        document.cookie = "testcookie=1";
        return document.cookie.indexOf("testcookie=1") !== -1;
      } catch (error) {
        console.error("Error checking cookie support:", error);
        return false;
      }
    }

    // Display cookie message if cookies are disabled
    if (!areCookiesEnabled()) {
      const cookieMessage = document.getElementById("cookieMessage");
      cookieMessage.style.display = "block";
    }
  </script>
</body>
</html>
```
