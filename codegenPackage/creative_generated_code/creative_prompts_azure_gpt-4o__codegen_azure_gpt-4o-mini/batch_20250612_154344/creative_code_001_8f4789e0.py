"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrny.world
Prompt: Create a script to detect if JavaScript is disabled in a browser and display a message prompting users to enable JavaScript for the "JRNY" app.
Generated: DETERMINISTIC_8f4789e0fd6d5ba4
Batch ID: 20250612_154344
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
        /* Styles for the JavaScript disabled message */
        .js-disabled-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <style>
            /* Show the message if JavaScript is disabled */
            .js-disabled-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="js-disabled-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript to use the "JRNY" app for a better experience.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            console.log("JavaScript is enabled.");
            // Additional logic for the JRNY app can be added here
        });
    </script>
</body>
</html>
```
