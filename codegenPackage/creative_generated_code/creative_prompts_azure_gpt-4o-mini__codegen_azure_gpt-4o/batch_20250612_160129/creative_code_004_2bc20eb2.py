"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-soitinyastro.pages.dev
Prompt: How do I implement a feature that prompts users to enable JavaScript and cookies on my website?
Generated: DETERMINISTIC_2bc20eb2d0177e21
Batch ID: 20250612_160129
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
    /* Style for the warning messages */
    .warning {
      display: none;
      padding: 10px;
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      margin: 10px 0;
      font-size: 16px;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Warning for JavaScript disabled -->
  <noscript>
    <div class="warning">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Warning for Cookies disabled -->
  <div id="cookie-warning" class="warning">
    Cookies are disabled in your browser. Please enable cookies to use this website.
  </div>

  <!-- Content of the page -->
  <div id="content">
    <h1>Welcome to Our Website</h1>
    <p>This is a demo page that requires JavaScript and cookies enabled.</p>
  </div>

  <script>
    // Function to check if cookies are enabled
    function areCookiesEnabled() {
      try {
        // Check if cookies can be set and read
        document.cookie = "testcookie=1";
        return document.cookie.indexOf("testcookie=1") !== -1;
      } catch (err) {
        console.error("Error while checking cookies:", err);
        return false;
      }
    }

    // Display cookie warning if cookies are disabled
    window.addEventListener("DOMContentLoaded", () => {
      const cookieWarning = document.getElementById("cookie-warning");

      // Check if cookies are enabled
      if (!areCookiesEnabled()) {
        cookieWarning.style.display = "block";
      } else {
        // Remove test cookie if it was successfully set
        document.cookie = "testcookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      }
    });
  </script>
</body>
</html>
```
