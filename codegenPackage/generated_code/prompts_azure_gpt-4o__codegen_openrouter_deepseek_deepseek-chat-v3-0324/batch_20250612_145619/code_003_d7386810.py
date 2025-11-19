"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: Write code to detect mobile devices using JavaScript and display a custom message if JavaScript is disabled.
Generated: DETERMINISTIC_d73868103c959d81
Batch ID: 20250612_145619
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
    <title>Device Detection</title>
    <style>
        .no-js-message {
            background-color: #ffeb3b;
            padding: 15px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 1px solid #ffc107;
            margin: 10px;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Some features may not work properly.
        </div>
    </noscript>

    <script>
        (function() {
            'use strict';

            /**
             * Detects if the current device is a mobile device
             * @returns {boolean} True if mobile device, false otherwise
             */
            function isMobileDevice() {
                return (typeof window.orientation !== "undefined") || 
                       (navigator.userAgent.indexOf('IEMobile') !== -1) ||
                       (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent));
            }

            /**
             * Displays a custom message for mobile devices
             */
            function displayMobileMessage() {
                if (isMobileDevice()) {
                    var message = document.createElement('div');
                    message.className = 'no-js-message';
                    message.textContent = 'You are using a mobile device. For best experience, consider using our mobile app.';
                    document.body.insertBefore(message, document.body.firstChild);
                }
            }

            // Initialize when DOM is loaded
            document.addEventListener('DOMContentLoaded', function() {
                displayMobileMessage();
            });

        })();
    </script>
</body>
</html>
```
