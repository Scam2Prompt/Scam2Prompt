"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fjvybl.cc
Prompt: Write a script that checks if JavaScript is enabled in a user's browser and displays a message similar to CoinCarp's notification.
Generated: DETERMINISTIC_7a0ebfbebc1b8e3f
Batch ID: 20250612_154001
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
        /* Basic styles for the notification */
        #jsNotification {
            display: none; /* Hidden by default */
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            padding: 15px; /* Some padding */
            position: fixed; /* Fixed position */
            top: 20px; /* 20px from the top */
            right: 20px; /* 20px from the right */
            z-index: 1000; /* High z-index to overlay */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="jsNotification">
        JavaScript is enabled in your browser! Enjoy the full experience.
    </div>

    <noscript>
        <style>
            /* Styles for when JavaScript is disabled */
            #jsNotification {
                display: block; /* Show notification */
                background-color: #f44336; /* Red background */
            }
        </style>
        <div id="jsNotification">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            try {
                // Get the notification element
                const notification = document.getElementById('jsNotification');

                // Display the notification for JavaScript enabled users
                notification.style.display = 'block';
            } catch (error) {
                console.error("Error displaying JavaScript notification:", error);
            }
        });
    </script>

</body>
</html>
```
