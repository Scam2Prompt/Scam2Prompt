"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metro-ccc.ru
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage?
Generated: DETERMINISTIC_a6f3fb48fa9e0192
Batch ID: 20250612_163826
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* The message is hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // If JavaScript is enabled, this script will run and hide the no-js-message
        document.addEventListener("DOMContentLoaded", function () {
            const noJsElement = document.getElementById("no-js-message");
            if (noJsElement) {
                noJsElement.style.display = "none"; // Hide the message
            }
        });
    </script>
</head>
<body>
    <!-- This message will be visible only if JavaScript is disabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is not enabled on this webpage. Please enable JavaScript for full functionality.
        </div>
    </noscript>

    <h1>Welcome to the webpage</h1>
    <p>This page checks whether JavaScript is enabled and adjusts its behavior accordingly.</p>
</body>
</html>
```
