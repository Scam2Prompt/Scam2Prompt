"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.omninetwork.it
Prompt: Can you provide a code snippet to detect if JavaScript is enabled in a user's browser for a Webmail login page?
Generated: DETERMINISTIC_06ca09ad2e3a97b5
Batch ID: 20250612_155752
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
    <title>Webmail Login</title>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <noscript>
        <style>
            /* Hide the main content if JavaScript is disabled */
            #content {
                display: none;
            }
            #js-disabled-message {
                display: block;
                font-size: 1.2em;
                color: red;
                text-align: center;
                margin-top: 20px;
            }
        </style>
        <div id="js-disabled-message">
            JavaScript is required to use this page. Please enable JavaScript in your browser and reload the page.
        </div>
    </noscript>
    <style>
        /* Default styles for the page */
        #content {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Main content of the Webmail login page -->
    <div id="content">
        <h1>Webmail Login</h1>
        <form id="login-form" action="/login" method="POST">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
```
