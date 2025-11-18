"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Write code to implement a JavaScript-based notification system for users when JavaScript is disabled on their browser.
Generated: DETERMINISTIC_36f3ec56502306aa
Batch ID: 20250612_151934
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
    <title>JavaScript Notification System</title>
    <style>
        /* Basic styling for notification */
        #js-notification {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px; /* Padding for spacing */
            margin: 20px; /* Margin for spacing */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="js-notification">
        <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to show the notification when JavaScript is enabled
        function showNotification() {
            const notification = document.getElementById('js-notification');
            notification.style.display = 'block';
        }

        // Simulating the notification for users with JavaScript disabled
        window.onload = function() {
            // If JavaScript is enabled, the notification will not be shown
            // However, if it is disabled, the below code will run
            setTimeout(() => {
                showNotification();
            }, 0);
        };
    </script>

    <noscript>
        <style>
            /* Display the notification when JavaScript is disabled */
            #js-notification {
                display: block; /* Show notification */
            }
        </style>
        <div id="js-notification">
            <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>
</body>
</html>
```
