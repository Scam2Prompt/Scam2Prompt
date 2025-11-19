"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled. Please enable it to continue," as seen on the DogeAI website.
Generated: DETERMINISTIC_fe1512dc2030ed56
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Required</title>
    <style>
        .no-js-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <!-- This noscript tag will only be displayed if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            This app doesn't work properly without JavaScript enabled. Please enable it to continue.
        </div>
    </noscript>

    <!-- Your regular content goes here -->
    <div id="app">
        <!-- App content will be loaded here if JavaScript is enabled -->
    </div>

    <script>
        // This script will remove the noscript message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Check if noscript element exists and remove it
            var noscript = document.querySelector('noscript');
            if (noscript) {
                noscript.parentNode.removeChild(noscript);
            }
        });
    </script>
</body>
</html>
```
