"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cow-swap-dao.org
Prompt: Generate a code example that demonstrates how to enable JavaScript and cookies in a web application to improve user experience, inspired by Cow Swap DAO.
Generated: DETERMINISTIC_8a51f6f95d7861da
Batch ID: 20250612_162734
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
        /* Styling for fallback messages */
        .no-js-message, .no-cookies-message {
            display: none;
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Fallback message if JavaScript is disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to enjoy full functionality of the application.
        </div>
    </noscript>

    <div id="app-content">
        <!-- Content will only be visible if JavaScript and cookies are enabled -->
        <h1>Welcome to Cow Swap DAO</h1>
        <p>JavaScript and cookies are enabled. You can fully interact with this web application!</p>
    </div>

    <script>
        // Check if cookies are enabled
        function areCookiesEnabled() {
            try {
                // Attempt to set and read a cookie to verify functionality
                document.cookie = "test_cookie=1; SameSite=Strict";
                return document.cookie.indexOf("test_cookie=1") !== -1;
            } catch (error) {
                return false;
            }
        }

        // Display appropriate messaging based on JavaScript and cookie settings
        (function initializeApp() {
            const appContent = document.getElementById("app-content");
            const body = document.body;

            if (areCookiesEnabled()) {
                // Cookies are enabled, show the main application content
                appContent.style.display = "block";
            } else {
                // Cookies are disabled, show a fallback message
                const cookiesMessage = document.createElement("div");
                cookiesMessage.className = "no-cookies-message";
                cookiesMessage.textContent = "Cookies are disabled in your browser. Please enable them for full functionality.";
                body.appendChild(cookiesMessage);
                appContent.style.display = "none";
            }
        })();
    </script>
</body>
</html>
```
