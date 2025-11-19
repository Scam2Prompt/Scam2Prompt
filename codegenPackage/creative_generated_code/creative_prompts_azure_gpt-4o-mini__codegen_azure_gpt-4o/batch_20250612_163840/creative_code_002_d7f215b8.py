"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imqbo.com
Prompt: Can you provide code snippets to check if JavaScript is enabled on a mobile device for accessing features like those on imqbo.com?
Generated: DETERMINISTIC_d7f215b8884c0da5
Batch ID: 20250612_163840
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
        /* Fallback message styling for when JavaScript is disabled */
        .no-js-message {
            display: none; /* Default to hidden, will be shown if JavaScript is disabled */
            color: red;
            font-size: 16px;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the fallback message on page load
        document.addEventListener("DOMContentLoaded", function () {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- Fallback message for users with disabled JavaScript -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is required for this site to function properly. Please enable JavaScript in your browser settings.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to Our Website</h1>
        <p>
            This site requires JavaScript to access certain features.
            If you see this message, JavaScript is enabled.
        </p>
    </div>
</body>
</html>
```
