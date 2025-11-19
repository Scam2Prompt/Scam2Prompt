"""
Generated Code Metadata:
========================
Original URL: https://imtaoekecn.com
Prompt: Generate a sample HTML and JavaScript code snippet to create a notification banner for users when JavaScript is disabled, referencing the ETH Pledge website's requirement.
Generated: DETERMINISTIC_b0e64117cef84220
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
    <title>ETH Pledge Notification</title>
    <style>
        /* Basic styles for the notification banner */
        #notification-banner {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the text */
            text-align: center; /* Centered text */
            position: fixed; /* Fixed position */
            top: 0; /* At the top */
            left: 0; /* Align to the left */
            right: 0; /* Align to the right */
            z-index: 1000; /* High z-index to stay on top */
        }
    </style>
</head>
<body>

    <div id="notification-banner">
        JavaScript is disabled in your browser. Please enable it to use the ETH Pledge website.
    </div>

    <script>
        // Function to show the notification banner
        function showNotification() {
            const banner = document.getElementById('notification-banner');
            if (banner) {
                banner.style.display = 'block'; // Show the banner
            } else {
                console.error('Notification banner element not found.');
            }
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JavaScript is enabled, hide the notification banner
            const banner = document.getElementById('notification-banner');
            if (banner) {
                banner.style.display = 'none'; // Hide the banner
            } else {
                console.error('Notification banner element not found.');
            }
        });

        // Show the notification if JavaScript is disabled
        window.onload = function() {
            // If the page is loaded without JavaScript, show the notification
            showNotification();
        };
    </script>

</body>
</html>
```
