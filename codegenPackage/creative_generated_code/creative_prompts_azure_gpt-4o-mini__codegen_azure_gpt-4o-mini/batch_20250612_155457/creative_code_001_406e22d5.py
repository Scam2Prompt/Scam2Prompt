"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethping.com
Prompt: Write a code snippet to check if JavaScript is enabled on a mobile device and display a message if it's not.
Generated: DETERMINISTIC_406e22d5249998a6
Batch ID: 20250612_155457
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styling for the message */
        .js-disabled-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <div class="js-disabled-message" id="js-disabled-message">
        JavaScript is disabled on your device. Please enable it for the best experience.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showJsDisabledMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            } else {
                console.error('Message element not found'); // Log error if element is not found
            }
        }

        // Check if the device is mobile
        const isMobileDevice = () => {
            return /Mobi|Android/i.test(navigator.userAgent);
        };

        // Check if JavaScript is enabled
        if (!isMobileDevice()) {
            // If it's not a mobile device, do not show the message
            console.log('This is not a mobile device.');
        } else {
            // For mobile devices, show message if JavaScript is disabled
            showJsDisabledMessage();
        }
    </script>

    <!-- Adding a noscript tag to show a message when JavaScript is disabled -->
    <noscript>
        <style>
            /* Ensure the message is visible when JavaScript is disabled */
            .js-disabled-message {
                display: block; /* Show message */
            }
        </style>
        <div class="js-disabled-message">
            JavaScript is disabled on your device. Please enable it for the best experience.
        </div>
    </noscript>
</body>
</html>
```
