"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pin-ai.org
Prompt: What are the best practices for enabling JavaScript and cookies to enhance user experience on a website?
Generated: DETERMINISTIC_07656e7f15eb6529
Batch ID: 20250612_160711
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
    <title>User Experience Enhancements</title>
    <script>
        // Function to check if cookies are enabled in the browser
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1";
            const cookiesEnabled = document.cookie.includes("testcookie");
            // Clean up test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
            return cookiesEnabled;
        }

        // Function to set a cookie with an expiration date
        function setCookie(name, value, days) {
            let expires = "";
            if (days) {
                const date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + (value || "") + expires + "; path=/";
        }

        // Function to get a cookie by name
        function getCookie(name) {
            const nameEQ = name + "=";
            const ca = document.cookie.split(';');
            for (let i = 0; i < ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0) === ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
        }

        // Function to show a welcome message if user is returning
        function displayWelcomeMessage() {
            const username = getCookie("username");
            if (username) {
                alert(`Welcome back, ${username}!`);
            } else {
                const newUsername = prompt("What's your name?");
                if (newUsername) {
                    setCookie("username", newUsername, 7); // Set cookie for 7 days
                    alert(`Welcome, ${newUsername}!`);
                }
            }
        }

        // Initialize the script
        window.onload = function() {
            // Check for cookies support
            if (areCookiesEnabled()) {
                displayWelcomeMessage();
            } else {
                alert("Cookies are disabled. Please enable them for a better experience.");
            }
        };
    </script>
</head>
<body>
    <h1>User Experience Enhancement with JavaScript and Cookies</h1>
    <p>This example demonstrates how to use cookies to enhance user experience on a website.</p>
</body>
</html>
```
