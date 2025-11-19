"""
Generated Code Metadata:
========================
Original URL: https://fjvybl.cc
Prompt: Write a script that checks if JavaScript is enabled in a user's browser and displays a message similar to CoinCarp's notification.
Generated: DETERMINISTIC_7a0ebfbebc1b8e3f
Batch ID: 20250612_154001
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
    <title>JavaScript Check</title>
    <style>
        /* Basic styling for the notification */
        #js-notification {
            display: none; /* Hidden by default */
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            padding: 15px;
            border-radius: 5px;
            z-index: 1000; /* Ensure it appears above other content */
        }
    </style>
</head>
<body>

    <div id="js-notification">
        JavaScript is enabled in your browser!
    </div>

    <noscript>
        <style>
            /* Style for the message when JavaScript is disabled */
            #js-notification {
                display: block; /* Show the message */
                background-color: #f44336; /* Red background */
            }
        </style>
        <div id="js-notification">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <script>
        // Function to display the notification when JavaScript is enabled
        function showJsEnabledNotification() {
            const notification = document.getElementById('js-notification');
            notification.style.display = 'block'; // Show the notification
        }

        // Check if the DOM is fully loaded before executing the function
        document.addEventListener('DOMContentLoaded', (event) => {
            try {
                showJsEnabledNotification(); // Call the function to show the notification
            } catch (error) {
                console.error('Error displaying JavaScript enabled notification:', error);
            }
        });
    </script>
</body>
</html>
```
