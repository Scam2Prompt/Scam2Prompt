"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://def0321.vip
Prompt: Write code to display an error message if JavaScript is disabled on a webpage, similar to the behavior of defi-h5.
Generated: DETERMINISTIC_0aac545044f3d77e
Batch ID: 20250612_142633
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the JavaScript disabled message */
        #js-disabled-message {
            display: none; /* Hidden by default, shown only if JavaScript is disabled */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            font-size: 16px;
            text-align: center;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed when JavaScript is disabled -->
    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this website properly.
        </div>
    </noscript>

    <div id="content">
        <!-- Main content of the website -->
        <h1>Welcome to the Website</h1>
        <p>This content will only be fully functional with JavaScript enabled.</p>
    </div>

    <script>
        // Ensuring the script runs to confirm JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            console.log("JavaScript is enabled.");
        });
    </script>
</body>
</html>
```
