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
    <title>Cow Swap DAO - Enable JavaScript and Cookies</title>
    <script>
        // Function to check if cookies are enabled
        function checkCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax";

            // Check if the cookie was successfully set
            const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

            // Clean up the test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

            return cookiesEnabled;
        }

        // Function to show a message based on cookie status
        function displayCookieMessage() {
            if (checkCookiesEnabled()) {
                // Cookies are enabled, proceed with app functionality
                console.log("Cookies are enabled. You can enjoy the full features of the application.");
            } else {
                // Cookies are disabled, alert the user
                alert("Cookies are disabled in your browser. Please enable cookies for an enhanced experience.");
            }
        }

        // Function to initialize the application
        function initApp() {
            displayCookieMessage();
            // Additional initialization code can go here
        }

        // Run the initialization function when the DOM is fully loaded
        document.addEventListener("DOMContentLoaded", initApp);
    </script>
</head>
<body>
    <h1>Welcome to Cow Swap DAO</h1>
    <p>Please enable JavaScript and cookies for the best user experience.</p>
</body>
</html>
```
