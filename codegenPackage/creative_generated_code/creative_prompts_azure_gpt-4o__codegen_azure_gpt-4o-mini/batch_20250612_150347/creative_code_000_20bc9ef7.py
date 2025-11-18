"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message to the user.
Generated: DETERMINISTIC_20bc9ef70d9e8fab
Batch ID: 20250612_150347
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Initially hide the message */
            color: red; /* Color for the message */
            font-weight: bold; /* Bold text */
            margin: 20px; /* Margin for spacing */
        }
    </style>
</head>
<body>

    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript for the best experience on this website.
        </div>
    </noscript>

    <script>
        // This script runs only if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            console.log("JavaScript is enabled."); // Log for debugging purposes
        });
    </script>

</body>
</html>
```
