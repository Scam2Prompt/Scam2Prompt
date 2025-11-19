"""
Generated Code Metadata:
========================
Original URL: https://devoursol.com
Prompt: Generate code to enable JavaScript and cookies in a web application to improve user experience during security checks.
Generated: DETERMINISTIC_db2f881ad041449e
Batch ID: 20250612_163817
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
  <script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
      // If this script runs, JavaScript is enabled
      document.getElementById('js-status').textContent = 'JavaScript is enabled.';
    }

    // Function to check if cookies are enabled
    function checkCookiesEnabled() {
      try {
        // Attempt to set a test cookie
        document.cookie = "test_cookie=enabled; path=/";
        const cookiesEnabled = document.cookie.indexOf("test_cookie=enabled") !== -1;

        // Update the status based on cookie availability
        if (cookiesEnabled) {
          document.getElementById('cookie-status').textContent = 'Cookies are enabled.';
          // Clean up the test cookie
          document.cookie = "test_cookie=enabled; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC";
        } else {
          document.getElementById('cookie-status').textContent = 'Cookies are disabled.';
        }
      } catch (error) {
        // Handle any errors that occur during cookie testing
        console.error('Error checking cookies:', error);
        document.getElementById('cookie-status').textContent = 'Error checking cookies.';
      }
    }

    // Run checks when the page loads
    window.onload = function () {
      checkJavaScriptEnabled();
      checkCookiesEnabled();
    };
  </script>
</head>
<body>
  <h1>Security Check</h1>
  <p id="js-status">Checking JavaScript status...</p>
  <p id="cookie-status">Checking cookie status...</p>
</body>
</html>
```
