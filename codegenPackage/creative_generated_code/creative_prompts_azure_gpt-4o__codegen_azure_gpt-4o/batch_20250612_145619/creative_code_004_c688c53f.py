"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Write code to display a warning message if JavaScript is disabled in a user's browser when accessing the cPanel login page.
Generated: DETERMINISTIC_c688c53f216c01aa
Batch ID: 20250612_145619
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
    <title>cPanel Login</title>
    <style>
        /* Style for the JavaScript disabled warning message */
        .no-js-warning {
            display: none; /* Initially hide the warning message */
            background-color: #ffcc00;
            color: #000;
            padding: 10px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 1px solid #ff9900;
            margin-bottom: 20px;
        }
    </style>
    <noscript>
        <!-- noscript tag to display a warning if JavaScript is disabled -->
        <style>
            /* Override display: none for browsers without JavaScript */
            .no-js-warning {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Warning message to display if JavaScript is disabled -->
    <div class="no-js-warning">
        Warning: This page requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>

    <!-- Main content of the cPanel login page -->
    <div id="main-content">
        <h1>cPanel Login</h1>
        <form action="/login" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br><br>
            <button type="submit">Login</button>
        </form>
    </div>

    <script>
        // JavaScript to check if the page loaded successfully with JavaScript enabled
        document.addEventListener("DOMContentLoaded", function() {
            console.log("JavaScript is enabled and running.");
        });
    </script>
</body>
</html>
```
