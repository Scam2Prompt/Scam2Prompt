"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser?
Generated: DETERMINISTIC_1c188bf3c8768c38
Batch ID: 20250612_163647
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* This message will be shown if JavaScript is disabled */
        #no-js-message {
            display: block;
            color: red;
            font-weight: bold;
        }
        /* Hide the message by default if JavaScript is enabled */
        .js-enabled #no-js-message {
            display: none;
        }
    </style>
    <script>
        // Add a class to the <html> element to indicate JavaScript is enabled
        document.documentElement.classList.add('js-enabled');
    </script>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for full functionality.
    </div>
</body>
</html>
```
