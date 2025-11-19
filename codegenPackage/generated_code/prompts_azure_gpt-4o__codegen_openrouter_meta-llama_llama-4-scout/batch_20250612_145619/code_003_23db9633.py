"""
Generated Code Metadata:
========================
Original URL: https://imftokoen.com
Prompt: Write code to display a fallback message for users accessing a webpage without JavaScript enabled, specifically targeting mobile browsers.
Generated: DETERMINISTIC_23db963321805bfe
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Fallback Message</title>
    <style>
        /* Add some basic styling to make the fallback message more readable */
        .fallback-message {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20vh;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Display a fallback message for users without JavaScript enabled -->
        <div class="fallback-message">
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript in your browser settings to view this page properly.</p>
            <p>For mobile users:</p>
            <ul>
                <li>For Android: Go to Settings > Apps > Chrome > Permissions > JavaScript</li>
                <li>For iOS: Go to Settings > Safari > Advanced > JavaScript</li>
            </ul>
        </div>
    </noscript>

    <!-- Include a script to detect and handle mobile browsers -->
    <script>
        // Check if the user is on a mobile device
        function isMobile() {
            try {
                return /Android|iOS|iPad|iPhone|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            } catch (error) {
                console.error('Error detecting mobile device:', error);
                return false;
            }
        }

        // Display a mobile-specific message if JavaScript is enabled
        if (isMobile()) {
            document.addEventListener('DOMContentLoaded', function() {
                const mobileMessage = document.createElement('div');
                mobileMessage.classList.add('fallback-message');
                mobileMessage.innerHTML = `
                    <h1>JavaScript is Enabled</h1>
                    <p>You are on a mobile device with JavaScript enabled. Enjoy your browsing experience!</p>
                `;
                document.body.appendChild(mobileMessage);
            });
        } else {
            // Handle non-mobile devices
            document.addEventListener('DOMContentLoaded', function() {
                // You can add additional scripts or functionality here
            });
        }
    </script>
</body>
</html>
```
