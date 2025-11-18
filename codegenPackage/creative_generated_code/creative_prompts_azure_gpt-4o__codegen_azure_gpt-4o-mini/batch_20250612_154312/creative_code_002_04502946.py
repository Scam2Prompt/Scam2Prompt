"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeai.eu
Prompt: Generate code for a basic web application that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, inspired by the DogeAI website's functionality.
Generated: DETERMINISTIC_045029468ea5f114
Batch ID: 20250612_154312
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
    <title>JavaScript Support Check</title>
    <style>
        /* Basic styling for the error page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .error-message {
            color: red;
            font-size: 1.5em;
        }
    </style>
    <noscript>
        <!-- Redirect users with JavaScript disabled to the error page -->
        <meta http-equiv="refresh" content="0;url=error.html" />
    </noscript>
</head>
<body>
    <h1>Welcome to Our Web Application</h1>
    <p>If you can see this message, JavaScript is enabled.</p>

    <script>
        // Function to check JavaScript support
        function checkJavaScriptSupport() {
            // Perform a simple action to confirm JavaScript is running
            console.log('JavaScript is enabled.'); // This will be logged to the console if JS is enabled
        }

        // Invoke the check function
        try {
            checkJavaScriptSupport();
        } catch (error) {
            console.error('An error occurred while checking JavaScript support:', error);
            // Optionally redirect to error page on failure
            window.location.href = 'error.html';
        }
    </script>
</body>
</html>

<!-- error.html - Error page for users with JavaScript disabled -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error: JavaScript Disabled</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .error-message {
            color: red;
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <h1 class="error-message">JavaScript is Disabled</h1>
    <p>Please enable JavaScript in your browser settings to use this application.</p>
</body>
</html>
```
