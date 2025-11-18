"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gombke.pages.dev
Prompt: Generate a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "You need to enable JavaScript to run this app," similar to the GOMBLE Wallet Checker website.
Generated: DETERMINISTIC_de3d77e5b226f71e
Batch ID: 20250612_150435
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
        /* Basic styling for the message */
        #js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #ffcccb; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 20px;
            margin: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 18px;
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        You need to enable JavaScript to run this app.
    </div>

    <script>
        /**
         * Function to check if JavaScript is enabled.
         * If JavaScript is disabled, it displays a message to the user.
         */
        function checkJavaScriptEnabled() {
            // Show the message indicating JavaScript is required
            const messageElement = document.getElementById('js-disabled-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Display the message
            } else {
                console.error('Message element not found in the DOM.'); // Log error if element is not found
            }
        }

        // Run the check when the page loads
        window.onload = function() {
            // JavaScript is enabled, so we do nothing. 
            // If this function doesn't run, the message will be displayed after the DOM loads.
        };

        // In case JavaScript isn't enabled, we use a noscript tag to handle it
        document.addEventListener('DOMContentLoaded', function() {
            // This part will run only if JavaScript is enabled
            // You can put additional initialization code here
        });
    </script>

    <noscript>
        <style>
            /* Ensure the message is displayed when JavaScript is disabled */
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
