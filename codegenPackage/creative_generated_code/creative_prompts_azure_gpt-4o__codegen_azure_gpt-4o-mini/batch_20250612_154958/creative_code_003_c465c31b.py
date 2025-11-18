"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Develop a script that redirects users to an error page if JavaScript is disabled, similar to the functionality required by "aubi.online."
Generated: DETERMINISTIC_c465c31b3327a77a
Batch ID: 20250612_154958
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
    <title>JavaScript Redirect Example</title>
    <style>
        /* Basic styles for error page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8d7da;
            color: #721c24;
            text-align: center;
            padding: 50px;
        }
        .error-message {
            font-size: 24px;
        }
    </style>
    <noscript>
        <!-- Redirect to error page if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0; url='error.html'" />
    </noscript>
</head>
<body>
    <div class="error-message">
        <h1>JavaScript Disabled</h1>
        <p>Please enable JavaScript to view this page correctly.</p>
    </div>

    <script>
        // This script runs when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            console.log("JavaScript is enabled.");
            // You can add additional functionality here as needed
        });
    </script>
</body>
</html>
```

```html
<!-- Save this as error.html for the redirection target -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error Page</title>
    <style>
        /* Styles for the error page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8d7da;
            color: #721c24;
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>Error: JavaScript is Required</h1>
    <p>It seems that JavaScript is disabled in your browser. Please enable it to use this website properly.</p>
</body>
</html>
```
