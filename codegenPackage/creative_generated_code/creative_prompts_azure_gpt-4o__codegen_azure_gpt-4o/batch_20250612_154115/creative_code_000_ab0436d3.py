"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message.
Generated: DETERMINISTIC_ab0436d31d9d639c
Batch ID: 20250612_154115
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
        /* Custom error message styling */
        #js-disabled-message {
            display: none; /* Hidden by default */
            color: red;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- This will only be displayed if JavaScript is disabled -->
        <div id="js-disabled-message">JavaScript is disabled in your browser. Please enable JavaScript to view this site properly.</div>
    </noscript>

    <script>
        // Check if JavaScript is enabled and handle accordingly
        document.addEventListener('DOMContentLoaded', function () {
            // Ensure that the message does not display when JavaScript is enabled
            const jsDisabledMessage = document.getElementById('js-disabled-message');
            if (jsDisabledMessage) {
                jsDisabledMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
