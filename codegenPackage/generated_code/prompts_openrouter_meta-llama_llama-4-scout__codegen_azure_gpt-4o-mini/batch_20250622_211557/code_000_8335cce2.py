"""
Generated Code Metadata:
========================
Original URL: https://duoiudf-dsdds.pages.dev
Prompt: How to enable JavaScript and cookies for a static site hosted on Pages.dev?
Generated: DETERMINISTIC_8335cce23d318550
Batch ID: 20250622_211557
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
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Display a message if JavaScript is enabled
            const jsEnabledMessage = document.getElementById("js-enabled");
            jsEnabledMessage.style.display = "block";
        });

        // Function to set a cookie
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }

        // Function to get a cookie
        function getCookie(name) {
            return document.cookie.split('; ').reduce((r, v) => {
                const parts = v.split('=');
                return parts[0] === name ? decodeURIComponent(parts[1]) : r;
            }, '');
        }

        // Function to check if cookies are enabled
        function checkCookiesEnabled() {
            setCookie('testCookie', 'test', 1);
            const cookiesEnabled = getCookie('testCookie') === 'test';
            if (cookiesEnabled) {
                // Remove the test cookie
                setCookie('testCookie', '', -1);
                const cookiesEnabledMessage = document.getElementById("cookies-enabled");
                cookiesEnabledMessage.style.display = "block";
            } else {
                console.error("Cookies are not enabled in this browser.");
            }
        }

        // Run the cookie check on page load
        window.onload = function() {
            checkCookiesEnabled();
        };
    </script>
    <style>
        /* Basic styling for messages */
        .message {
            display: none;
            margin: 20px;
            padding: 10px;
            border: 1px solid #4CAF50;
            background-color: #f9f9f9;
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <h1>Enable JavaScript and Cookies</h1>
    <div id="js-enabled" class="message">JavaScript is enabled!</div>
    <div id="cookies-enabled" class="message">Cookies are enabled!</div>
</body>
</html>
```
