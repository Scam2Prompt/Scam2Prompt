"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.juta-soft.hu
Prompt: Write a script that checks if cookies are enabled in a browser before attempting to sign in to Outlook.
Generated: DETERMINISTIC_e2d58eda0e9bdfb2
Batch ID: 20250612_164139
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
    <title>Cookie Checker</title>
    <script>
        /**
         * Function to check if cookies are enabled in the user's browser.
         * If cookies are disabled, display an error message and prevent sign-in.
         */
        function checkCookiesBeforeSignIn() {
            try {
                // Attempt to set a test cookie
                document.cookie = "test_cookie=enabled; path=/";

                // Check if the cookie was successfully set
                const cookiesEnabled = document.cookie.indexOf("test_cookie=enabled") !== -1;

                if (!cookiesEnabled) {
                    // Cookies are disabled - show an alert and prevent sign-in
                    alert("Cookies are disabled in your browser. Please enable cookies to sign in.");
                    return false; // Prevent sign-in
                } else {
                    // Cookies are enabled - proceed with sign-in
                    alert("Cookies are enabled. You can proceed to sign in.");
                    return true; // Allow sign-in
                }
            } catch (error) {
                // Error handling in case of unexpected issues
                console.error("An error occurred while checking cookies:", error);
                alert("An unexpected error occurred. Please try again later.");
                return false; // Prevent sign-in in case of errors
            }
        }
    </script>
</head>
<body>
    <h1>Sign in to Outlook</h1>
    <form onsubmit="return checkCookiesBeforeSignIn()">
        <!-- Sign-in form fields -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Sign In</button>
    </form>
</body>
</html>
```
