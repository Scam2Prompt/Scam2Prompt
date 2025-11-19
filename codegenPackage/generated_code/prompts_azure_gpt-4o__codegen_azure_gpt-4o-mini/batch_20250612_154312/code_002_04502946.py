"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Generate code for a basic web application that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, inspired by the DogeAI website's functionality.
Generated: DETERMINISTIC_045029468ea5f114
Batch ID: 20250612_154312
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
            font-size: 24px;
        }
    </style>
    <noscript>
        <!-- Redirect to error page if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0; url=error.html">
    </noscript>
</head>
<body>
    <h1>Welcome to the Web Application</h1>
    <p>This application requires JavaScript to function properly.</p>
    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // If JavaScript is enabled, we can proceed with the application logic
            console.log("JavaScript is enabled.");
            // Additional application logic can go here
        });
    </script>
</body>
</html>

<!-- error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - JavaScript Disabled</title>
    <style>
        /* Basic styling for the error page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .error-message {
            color: red;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1 class="error-message">Error: JavaScript is Disabled</h1>
    <p>Please enable JavaScript in your browser settings to use this application.</p>
</body>
</html>
```
