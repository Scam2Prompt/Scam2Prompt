"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aussbitte.com
Prompt: How can I create a notification for users who have JavaScript disabled when they visit my website, like the message on aussbitte.com?
Generated: DETERMINISTIC_307abab4499e68cb
Batch ID: 20250612_155632
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
        /* Styles for the notification banner */
        .no-js-notification {
            display: none; /* Hidden by default */
            background-color: #ffcc00; /* Warning color */
            color: #333; /* Text color */
            padding: 15px;
            text-align: center;
            position: fixed; /* Fixed position */
            top: 0;
            left: 0;
            width: 100%; /* Full width */
            z-index: 1000; /* On top */
        }
    </style>
</head>
<body>

    <!-- Notification banner for users with JavaScript disabled -->
    <div class="no-js-notification" id="no-js-notification">
        <strong>JavaScript is disabled in your browser.</strong>
        Please enable JavaScript to use all features of this website.
    </div>

    <noscript>
        <style>
            /* Show the notification if JavaScript is disabled */
            #no-js-notification {
                display: block; /* Display the banner */
            }
        </style>
    </noscript>

    <script>
        // JavaScript can be used for additional functionality
        document.addEventListener('DOMContentLoaded', function () {
            // Example: Hide notification bar if JavaScript is enabled
            const notification = document.getElementById('no-js-notification');
            if (notification) {
                notification.style.display = 'none'; // Hide the notification banner
            }
        });
    </script>

</body>
</html>
```
