"""
Generated Code Metadata:
========================
Original URL: https://login.futurx.live
Prompt: Develop a script to redirect users to an error page if JavaScript is disabled, similar to the functionality observed on the FuturX login page.
Generated: DETERMINISTIC_6ea5613148f20dcc
Batch ID: 20250612_145626
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
    <title>JavaScript Redirect Example</title>
    <style>
        /* Basic styles for the error page */
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
        <meta http-equiv="refresh" content="0;url=error.html">
    </noscript>
</head>
<body>
    <h1>Welcome to Our Application</h1>
    <p>If you see this message, JavaScript is enabled.</p>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Redirect to error page if JavaScript is disabled
            window.location.href = "error.html";
        }

        // Call the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```

```html
<!-- error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - JavaScript Disabled</title>
    <style>
        /* Basic styles for the error page */
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
    <h1 class="error-message">Error: JavaScript is Disabled</h1>
    <p>Please enable JavaScript in your browser settings to use this application.</p>
</body>
</html>
```
