"""
Generated Code Metadata:
========================
Original URL: https://fronkweb.web.app
Prompt: Generate code for a web app that displays a custom error message when JavaScript is disabled, as seen in the FRONK web app.
Generated: DETERMINISTIC_3b2a39641db83687
Batch ID: 20250612_152235
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
    <title>Custom Error Message</title>
    <style>
        /* Basic styling for the error message */
        .error-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 20px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
    <noscript>
        <style>
            /* Show the error message when JavaScript is disabled */
            .error-message {
                display: block; /* Display the error message */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="error-message">
        <h1>JavaScript Disabled</h1>
        <p>It seems that JavaScript is disabled in your browser. Please enable JavaScript to use the full functionality of this web app.</p>
    </div>

    <h1>Welcome to the FRONK Web App</h1>
    <p>This is a sample web application that requires JavaScript to function properly.</p>

    <script>
        // Check if JavaScript is enabled
        console.log("JavaScript is enabled."); // Log message for debugging
    </script>
</body>
</html>
```
