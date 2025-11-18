"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigbonus.eu
Prompt: Provide an example of a JavaScript-based app that requires JavaScript to function properly, including code for handling user notifications when JavaScript is disabled.
Generated: DETERMINISTIC_2945cee2350745f2
Batch ID: 20250612_145455
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
    <title>JavaScript Notification Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .notification {
            display: none;
            padding: 10px;
            margin: 20px;
            border: 1px solid #f00;
            background-color: #ffe6e6;
            color: #d8000c;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="notification">
            JavaScript is disabled in your browser. Please enable JavaScript to use the full functionality of this application.
        </div>
    </noscript>

    <div id="app">
        <h1>Welcome to the JavaScript App</h1>
        <button id="notifyButton">Send Notification</button>
        <div id="userNotification" class="notification"></div>
    </div>

    <script>
        // Check if the document is ready
        document.addEventListener('DOMContentLoaded', function () {
            const notifyButton = document.getElementById('notifyButton');
            const userNotification = document.getElementById('userNotification');

            // Function to show user notification
            function showNotification(message) {
                try {
                    // Set the message in the notification div
                    userNotification.textContent = message;
                    userNotification.style.display = 'block';

                    // Automatically hide notification after 3 seconds
                    setTimeout(() => {
                        userNotification.style.display = 'none';
                    }, 3000);
                } catch (error) {
                    console.error('Error displaying notification:', error);
                }
            }

            // Event listener for the notification button
            notifyButton.addEventListener('click', function () {
                // Calling the function to show notification
                showNotification('Your action was successful!');
            });
        });
    </script>
</body>
</html>
```
