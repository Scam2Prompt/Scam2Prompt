"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drophunter.net
Prompt: Can you provide a code snippet that checks if JavaScript is enabled in a browser for an app similar to Drop Hunter?
Generated: DETERMINISTIC_ddec42b1b03e00f6
Batch ID: 20250612_135717
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
        /* This message will be displayed if JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the message
        document.addEventListener("DOMContentLoaded", function () {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div id="no-js-message" class="no-js-message">
            JavaScript is not enabled. Please enable JavaScript in your browser to use this application.
        </div>
    </noscript>

    <div id="app">
        <!-- Main content of your app -->
        <h1>Welcome to Drop Hunter</h1>
        <p>Your app's content will load here if JavaScript is enabled.</p>
    </div>
</body>
</html>
```
