"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raiden.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the Raiden Online domain details page.
Generated: DETERMINISTIC_4ca7b2495ee4ca9e
Batch ID: 20250612_151912
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #ffcccc;
            color: #e60000;
            padding: 20px;
            border: 1px solid #e60000;
            margin: 20px;
            font-family: Arial, sans-serif;
            text-align: center;
        }
    </style>
    <script>
        // This function runs when the document is fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            // If JavaScript is enabled, hide the no-js message
            document.getElementById('no-js-message').style.display = 'none';
        });
    </script>
</head>
<body>
    <div id="no-js-message">
        <h1>JavaScript is Disabled</h1>
        <p>It seems that JavaScript is disabled in your browser. Please enable JavaScript to use this website properly.</p>
    </div>

    <noscript>
        <!-- This section will only display if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

    <h2>Welcome to Our Website!</h2>
    <p>This content is only accessible if JavaScript is enabled.</p>
</body>
</html>
```
