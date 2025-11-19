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
    <title>Security Check</title>
    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax; path=/";
            const cookiesEnabled = document.cookie.indexOf("testcookie") !== -1;

            // Clean up the test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";

            return cookiesEnabled;
        }

        // Function to display a message based on cookie status
        function checkCookieStatus() {
            const messageElement = document.getElementById("cookie-status");

            if (areCookiesEnabled()) {
                messageElement.textContent = "Cookies are enabled. You can proceed with the security check.";
                messageElement.style.color = "green";
            } else {
                messageElement.textContent = "Cookies are disabled. Please enable cookies for a better experience.";
                messageElement.style.color = "red";
            }
        }

        // Function to enable JavaScript and cookies
        function enableFeatures() {
            // Check if JavaScript is enabled
            if (typeof document !== 'undefined') {
                checkCookieStatus();
            } else {
                console.error("JavaScript is not enabled in this browser.");
            }
        }

        // Run the enableFeatures function when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", enableFeatures);
    </script>
</head>
<body>
    <h1>Welcome to the Security Check</h1>
    <p id="cookie-status"></p>
</body>
</html>
```
