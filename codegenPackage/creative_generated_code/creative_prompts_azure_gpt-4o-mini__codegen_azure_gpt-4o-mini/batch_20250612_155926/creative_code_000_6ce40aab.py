"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds.pages.dev
Prompt: How can I enable JavaScript and cookies in my browser for better web functionality?
Generated: DETERMINISTIC_6ce40aabc6e42eba
Batch ID: 20250612_155926
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
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
        }
        .message {
            color: red;
            display: none; /* Hide the message by default */
        }
    </style>
</head>
<body>
    <h1>Browser Settings</h1>
    <p>
        For better web functionality, please ensure that JavaScript and cookies are enabled in your browser settings.
    </p>
    <div class="message" id="errorMessage">
        <strong>Error:</strong> JavaScript is disabled or cookies are not allowed!
    </div>

    <script>
        // Function to check if cookies are enabled
        function areCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; SameSite=Lax";
            const cookiesEnabled = document.cookie.indexOf("testcookie=") !== -1;

            // Clean up the test cookie
            if (cookiesEnabled) {
                document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            }

            return cookiesEnabled;
        }

        // Check if JavaScript is enabled
        if (typeof window === 'undefined') {
            // If window is undefined, JavaScript is not enabled
            document.getElementById('errorMessage').style.display = 'block';
        } else if (!areCookiesEnabled()) {
            // If cookies are not enabled, show the error message
            document.getElementById('errorMessage').style.display = 'block';
        } else {
            // If everything is working, you could continue with your functionality
            console.log("JavaScript and cookies are enabled.");
        }
    </script>
</body>
</html>
```
