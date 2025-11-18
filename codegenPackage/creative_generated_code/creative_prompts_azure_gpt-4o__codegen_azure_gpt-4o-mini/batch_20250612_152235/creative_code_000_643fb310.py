"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting users to enable it, similar to the functionality required for the FRONK web app.
Generated: DETERMINISTIC_643fb310228fdf60
Batch ID: 20250612_152235
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
        /* Style for the message when JavaScript is disabled */
        #js-disabled-message {
            display: none; /* Initially hidden */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 20px; /* Padding around the message */
            text-align: center; /* Center the text */
            font-family: Arial, sans-serif; /* Font style */
        }
    </style>
</head>
<body>
    <!-- Message to display when JavaScript is disabled -->
    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it to use the features of this website.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function displayJsDisabledMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is enabled by executing this script
        document.addEventListener('DOMContentLoaded', () => {
            // If this code runs, JavaScript is enabled
            // No action needed here, script will continue executing
        });

        // If JavaScript is disabled, the following <noscript> tag will execute
        // and show the message for users without JS support
    </script>

    <noscript>
        <style>
            /* Style to ensure the message is shown with no JavaScript */
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</body>
</html>
```
