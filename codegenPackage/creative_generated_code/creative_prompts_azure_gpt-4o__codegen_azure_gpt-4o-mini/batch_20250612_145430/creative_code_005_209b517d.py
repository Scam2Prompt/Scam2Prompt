"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-pals.vercel.app
Prompt: Write code to detect if JavaScript is disabled in a browser and display a message like "You need to enable JavaScript to run this app," as seen on Phantom Pals.
Generated: DETERMINISTIC_209b517d73e92e79
Batch ID: 20250612_145430
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles for the message when JS is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f44336; /* Red background */
            color: #ffffff; /* White text */
            padding: 20px; /* Spacing */
            text-align: center; /* Center text */
            font-family: Arial, sans-serif; /* Font style */
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="js-disabled-message">
        You need to enable JavaScript to run this app.
    </div>

    <noscript>
        <style>
            /* If JS is disabled, show the message */
            .no-js-message {
                display: block; /* Show message */
            }
        </style>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        (function() {
            // Get the message container
            const messageContainer = document.getElementById('js-disabled-message');

            // Function to hide the message if JS is enabled
            function hideJsDisabledMessage() {
                if (messageContainer) {
                    messageContainer.style.display = 'none';
                }
            }

            // Hide the message on page load
            document.addEventListener('DOMContentLoaded', hideJsDisabledMessage);
        })();
    </script>

</body>
</html>
```
