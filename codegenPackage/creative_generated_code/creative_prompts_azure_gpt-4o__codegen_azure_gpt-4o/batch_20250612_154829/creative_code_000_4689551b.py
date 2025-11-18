"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it.
Generated: DETERMINISTIC_4689551b0f3bb70f
Batch ID: 20250612_154829
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
        /* Style for the no-JavaScript message */
        #no-js-message {
            display: none; /* Initially hidden; shown only if JavaScript is disabled */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <noscript>
        <div id="no-js-message">
            <strong>JavaScript is disabled in your browser. Please enable it to use this site properly.</strong>
        </div>
    </noscript>

    <!-- Content for when JavaScript is enabled -->
    <div id="content">
        <h1>Welcome to Our Website!</h1>
        <p>JavaScript is enabled, so you can enjoy all features.</p>
    </div>

    <!-- If JavaScript is enabled, hide the no-JavaScript message -->
    <script>
        // Ensure the "no-js-message" is completely hidden if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
