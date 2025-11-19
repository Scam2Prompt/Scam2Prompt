"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: How do I create a fallback message for users without JavaScript when they visit a site like Sophon.eu?
Generated: DETERMINISTIC_96daee9c232dd2e4
Batch ID: 20250612_155442
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
    <title>Sophon.eu</title>
    <style>
        /* Style for the no-JavaScript fallback message */
        .no-js-message {
            color: red;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            border: 2px solid red;
            margin: 20px;
            background-color: #ffe6e6;
        }
    </style>
    <script>
        // Remove the fallback message from the DOM if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.remove();
            }
        });
    </script>
</head>
<body>
    <!-- Fallback message for users who don't have JavaScript enabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is required to view this site properly. Please enable it in your browser settings.
        </div>
    </noscript>

    <!-- Main content of the site -->
    <h1>Welcome to Sophon.eu</h1>
    <p>This website leverages JavaScript for interactive features.</p>
</body>
</html>
```
