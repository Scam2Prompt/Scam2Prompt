"""
Generated Code Metadata:
========================
Original URL: https://bonkbox-claim.web.app
Prompt: Write code to dynamically display a message on a webpage if JavaScript is disabled, inspired by the BONKBOXES whitelist page functionality.
Generated: DETERMINISTIC_d03bb151bf5a0031
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Message</title>
    <style>
        /* Style the message container */
        #js-disabled-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #FFC080;
            color: #666;
            text-align: center;
            padding: 1em;
            display: none;
        }
    </style>
</head>
<body>
    <!-- Container for the message -->
    <div id="js-disabled-message">
        <strong>JavaScript is disabled.</strong> This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const jsDisabledMessage = document.getElementById('js-disabled-message');

            // If JavaScript is disabled, the message will be displayed
            // We use a noscript tag to handle this
            try {
                // Try to access the localStorage to detect if JavaScript is enabled
                window.localStorage.getItem('test');
            } catch (e) {
                // If an error occurs, it means JavaScript is disabled
                jsDisabledMessage.style.display = 'block';
            }

            // Alternatively, you can use the following approach
            // If the script runs, it means JavaScript is enabled
            // So we remove the noscript message
            const noscriptMessage = document.querySelector('noscript');
            if (noscriptMessage) {
                noscriptMessage.style.display = 'none';
            }
        });
    </script>
    <noscript>
        <div id="js-disabled-message">
            <strong>JavaScript is disabled.</strong> This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
        </div>
    </noscript>
</body>
</html>
```
