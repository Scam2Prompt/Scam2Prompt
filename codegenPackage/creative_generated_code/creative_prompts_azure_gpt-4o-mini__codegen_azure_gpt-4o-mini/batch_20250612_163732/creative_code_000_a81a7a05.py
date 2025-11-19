"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: How can I enable JavaScript and cookies in my browser for web applications?
Generated: DETERMINISTIC_a81a7a05e54fc61d
Batch ID: 20250612_163732
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
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Create a div to show JavaScript is enabled
            const jsEnabledDiv = document.createElement('div');
            jsEnabledDiv.innerHTML = "<p>JavaScript is enabled!</p>";
            document.body.appendChild(jsEnabledDiv);
        }

        // Function to check if cookies are enabled
        function checkCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=enabled; max-age=3600";
            const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

            if (cookiesEnabled) {
                // If the cookie is set, show a message
                const cookiesEnabledDiv = document.createElement('div');
                cookiesEnabledDiv.innerHTML = "<p>Cookies are enabled!</p>";
                document.body.appendChild(cookiesEnabledDiv);

                // Clean up the test cookie
                document.cookie = "testcookie=; max-age=0";
            } else {
                // Show message if cookies are not enabled
                const cookiesDisabledDiv = document.createElement('div');
                cookiesDisabledDiv.innerHTML = "<p>Cookies are disabled. Please enable cookies in your browser settings.</p>";
                document.body.appendChild(cookiesDisabledDiv);
            }
        }

        // Run checks once the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', function () {
            checkJavaScriptEnabled();
            checkCookiesEnabled();
        });
    </script>
</head>
<body>
    <h1>Browser Settings Check</h1>
    <p>This page will check if JavaScript and cookies are enabled in your browser.</p>
</body>
</html>
```
