"""
Generated Code Metadata:
========================
Original URL: https://ethvni.com
Prompt: Provide a solution for detecting and notifying users when JavaScript is disabled on a Bitcoin pledge platform, inspired by the ethvni.com website.
Generated: DETERMINISTIC_f1925dd81184315d
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
    <title>Bitcoin Pledge Platform</title>
    <style>
        /* Styles for the notification message */
        #js-disabled-notification {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding */
            position: fixed; /* Fixed position */
            top: 0; /* At the top */
            left: 0; /* Align to the left */
            right: 0; /* Stretch to the right */
            text-align: center; /* Centered text */
            z-index: 1000; /* On top of other elements */
        }
    </style>
</head>
<body>

    <div id="js-disabled-notification">
        JavaScript is disabled in your browser. Please enable it to use the Bitcoin pledge platform.
    </div>

    <script>
        // Function to show the notification if JavaScript is disabled
        function showJsDisabledNotification() {
            const notification = document.getElementById('js-disabled-notification');
            if (notification) {
                notification.style.display = 'block'; // Show the notification
            } else {
                console.error('Notification element not found.'); // Log error if element is not found
            }
        }

        // Function to hide the notification (if needed)
        function hideJsDisabledNotification() {
            const notification = document.getElementById('js-disabled-notification');
            if (notification) {
                notification.style.display = 'none'; // Hide the notification
            } else {
                console.error('Notification element not found.'); // Log error if element is not found
            }
        }

        // Immediately show the notification if JavaScript is disabled
        document.addEventListener('DOMContentLoaded', function() {
            // This function will only run if JavaScript is enabled
            hideJsDisabledNotification();
        });

        // Fallback for when JavaScript is disabled
        window.onload = function() {
            // If the page is loaded without JavaScript, show the notification
            showJsDisabledNotification();
        };
    </script>

</body>
</html>
```
