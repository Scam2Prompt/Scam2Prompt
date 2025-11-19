"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-base.pages.dev
Prompt: How can I enable JavaScript and cookies for the Photon Base website?
Generated: DETERMINISTIC_a4146b07c4a4aea9
Batch ID: 20250612_160156
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
    <script>
        // Check if JavaScript is enabled
        if (typeof window === 'undefined') {
            alert('JavaScript is not enabled in your browser. Please enable JavaScript to use the Photon Base website.');
        }

        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax; path=/";
            const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

            // Clean up the test cookie
            document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";

            return cookiesEnabled;
        }

        // Check for cookie support
        if (!areCookiesEnabled()) {
            alert('Cookies are not enabled in your browser. Please enable cookies to use the Photon Base website.');
        }
    </script>
</head>
<body>
    <h1>Welcome to the Photon Base Website</h1>
    <p>Please ensure that JavaScript and cookies are enabled in your browser for the best experience.</p>
</body>
</html>
```
