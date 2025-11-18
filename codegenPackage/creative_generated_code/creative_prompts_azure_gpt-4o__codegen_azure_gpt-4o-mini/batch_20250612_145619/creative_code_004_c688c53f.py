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
        /* Style for the warning message */
        .warning {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <!-- Display warning message if JavaScript is disabled -->
        <style>
            .warning {
                display: block; /* Show warning message */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="warning" id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Some features of this page may not work correctly.
    </div>

    <h1>cPanel Login</h1>
    <!-- Login form goes here -->
    <form action="/login" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>

    <script>
        // If JavaScript is enabled, hide the warning message
        document.getElementById('js-warning').style.display = 'none';
    </script>
</body>
</html>
```
