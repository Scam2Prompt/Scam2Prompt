"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdex-4ld.pages.dev
Prompt: Write code to check if JavaScript is enabled in a browser and display an error message if it is disabled, as seen on https://mdex-4ld.pages.dev.
Generated: DETERMINISTIC_ceea2f678726d8be
Batch ID: 20250612_151329
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
    <title>JavaScript Check</title>
    <style>
        /* Styling for the error message */
        .no-js-message {
            display: none;
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Default error message -->
    <div id="no-js-message" class="no-js-message">
        Error: JavaScript is disabled in your browser. Please enable JavaScript to proceed.
    </div>

    <!-- JavaScript block -->
    <script>
        // If JavaScript is enabled, hide the error message
        document.addEventListener('DOMContentLoaded', function () {
            try {
                const errorMessageElement = document.getElementById('no-js-message');
                if (errorMessageElement) {
                    errorMessageElement.style.display = 'none'; // Hide error message
                }
            } catch (error) {
                console.error('An error occurred while checking JavaScript availability:', error);
            }
        });
    </script>

    <!-- Fallback for browsers with JavaScript disabled -->
    <noscript>
        <style>
            .no-js-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>
</body>
</html>
```
