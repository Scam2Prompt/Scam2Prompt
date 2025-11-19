"""
Generated Code Metadata:
========================
Original URL: https://equinix.online
Prompt: Create a script that redirects users to a custom error page if JavaScript is disabled on their browser.
Generated: DETERMINISTIC_76bfee027ac9eca1
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// no JavaScript redirect file, serves as a fallback
// when JavaScript is disabled

// noscript.html 
// This file will be rendered when JavaScript is disabled

// index.html (main entry point)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Redirect</title>
</head>
<body>
    <noscript>
        <meta http-equiv="refresh" content="0;url=noscript.html">
    </noscript>
    <script>
        // redirect to main application if JavaScript is enabled
        window.location.replace('app.html');
    </script>
</body>
</html>

// noscript.html (custom error page)
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
        }
    </style>
</head>
<body>
    <h1>Error: JavaScript Disabled</h1>
    <p>Please enable JavaScript in your browser to access our application.</p>
</body>
</html>

// app.html (main application page)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main Application</title>
</head>
<body>
    <!-- main application content -->
    <h1>Welcome to our application!</h1>
</body>
</html>
```
