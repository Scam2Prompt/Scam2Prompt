"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop-playboicarti.com
Prompt: Write a script that displays a maintenance notification on an online store, similar to the one on Playboi Carti's website.
Generated: DETERMINISTIC_618c4aa1387e9b15
Batch ID: 20250612_163912
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
    <title>Maintenance Notification</title>
    <style>
        /* Basic styling for the maintenance notification */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .notification {
            background-color: #ffcc00;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .notification h1 {
            margin: 0;
            font-size: 24px;
        }
        .notification p {
            margin: 10px 0 0;
        }
    </style>
</head>
<body>
    <div class="notification" id="maintenanceNotification">
        <h1>Site Under Maintenance</h1>
        <p>We are currently performing scheduled maintenance.</p>
        <p>Please check back later.</p>
    </div>

    <script>
        // Function to hide the maintenance notification after a specific duration
        function hideNotification(duration) {
            // Error handling for duration parameter
            if (typeof duration !== 'number' || duration < 0) {
                console.error('Invalid duration provided for hideNotification. Must be a non-negative number.');
                return;
            }
            // Set a timeout to hide the notification after the specified duration
            setTimeout(() => {
                const notification = document.getElementById('maintenanceNotification');
                if (notification) {
                    notification.style.display = 'none';
                } else {
                    console.error('Notification element not found.');
                }
            }, duration);
        }

        // Display the notification indefinitely
        // Optionally, you can call hideNotification with a specific duration in milliseconds
        // hideNotification(30000); // Example: hides the notification after 30 seconds
    </script>
</body>
</html>
```
