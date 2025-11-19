"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hdhdh00007.pages.dev
Prompt: How do I implement a feature that prompts users to enable JavaScript and cookies on my website?
Generated: DETERMINISTIC_2bc20eb2d0177e21
Batch ID: 20250612_155936
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
    .no-js, .no-cookies {
      display: none;
      background-color: #f8d7da;
      color: #721c24;
      padding: 15px;
      border: 1px solid #f5c6cb;
      border-radius: 5px;
      margin: 20px 0;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Warning message for JavaScript -->
  <noscript>
    <div class="no-js">
      JavaScript is disabled in your browser. Please enable JavaScript to use this website.
    </div>
  </noscript>

  <!-- Warning message for Cookies -->
  <div id="no-cookies" class="no-cookies">
    Cookies are disabled in your browser. Please enable cookies to use this website.
  </div>

  <!-- Content of the site -->
  <div id="site-content">
    <h1>Welcome to Our Website</h1>
    <p>Please ensure you have JavaScript and cookies enabled for the best experience.</p>
  </div>

  <script>
    /**
     * Function to check if cookies are enabled in the browser.
     * If cookies are disabled, show the warning message.
     */
    function checkCookiesEnabled() {
      try {
        // Attempt to set a test cookie and check if it is stored
        document.cookie = "test_cookie=1";
        const cookiesEnabled = document.cookie.indexOf("test_cookie=1") !== -1;

        // Delete the test cookie
        document.cookie = "test_cookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

        // Show warning if cookies are disabled
        if (!cookiesEnabled) {
          document.getElementById("no-cookies").style.display = "block";
        }
      } catch (error) {
        console.error("Error checking cookies:", error);
      }
    }

    // Check cookies when the script loads
    checkCookiesEnabled();
  </script>
</body>
</html>
```
