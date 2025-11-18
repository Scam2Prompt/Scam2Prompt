"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a message prompting users to enable it, as required by the ETH Pledge website.
Generated: DETERMINISTIC_b58e64b5883128e7
Batch ID: 20250612_145619
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
        /* Style for the message container */
        #js-disabled-message {
            display: none; /* Initially hide the message */
            background-color: #ffcc00; /* Warning background color */
            padding: 20px; /* Padding for the message */
            text-align: center; /* Center the text */
            font-size: 18px; /* Increase font size */
            color: #000; /* Text color */
        }
    </style>
</head>
<body>
    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it for the best experience on the ETH Pledge website.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showJsDisabledMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is running
        document.addEventListener("DOMContentLoaded", function() {
            // JavaScript is enabled; do nothing
        });

        // If JavaScript is disabled, this script will not run,
        // and the message will be displayed.
        window.onload = function() {
            // If the page has loaded, we assume JavaScript is enabled
            console.log("JavaScript is enabled."); // Logging for debugging
        };
    </script>

    <noscript>
        <!-- This block will be executed if JavaScript is disabled -->
        <style>
            /* Ensure the message is visible when JS is disabled */
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it for the best experience on the ETH Pledge website.
        </div>
    </noscript>
</body>
</html>
```
