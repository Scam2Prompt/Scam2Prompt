"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Generate code for a web app that displays a custom error message when JavaScript is disabled, as seen in the FRONK web app.
Generated: DETERMINISTIC_3b2a39641db83687
Batch ID: 20250612_152235
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
    <title>JavaScript Disabled</title>
    <style>
        /* Basic styling for the error message */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text color */
            margin: 0;
            text-align: center;
        }
        
        .error-container {
            padding: 20px;
            border: 1px solid #f5c6cb; /* Border color matching background */
            border-radius: 5px;
            background-color: #ffffff; /* White background for the error message */
        }
    </style>
</head>
<body>
    <noscript>
        <div class="error-container">
            <h1>JavaScript is Disabled</h1>
            <p>This web app requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
        </div>
    </noscript>

    <script>
        // This code will run if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Main functionality of the web app goes here
            console.log("JavaScript is enabled. Continue loading the app...");
        });
    </script>
</body>
</html>
```
