"""
Generated Code Metadata:
========================
Original URL: https://swapfinderbq.github.io
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "avedex-m doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_d0538c98a7b701f2
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="no-js-message" id="no-js-message">
        avedex-m doesn't work properly without JavaScript enabled.
    </div>

    <script>
        // Function to display a message if JavaScript is disabled
        function checkJavaScriptEnabled() {
            // Get the message element
            const messageElement = document.getElementById('no-js-message');

            // Check if the message element exists
            if (messageElement) {
                // Show the message if JavaScript is enabled
                messageElement.style.display = 'none';
            } else {
                console.error('Message element not found.');
            }
        }

        // Call the function to check JavaScript status
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message when JavaScript is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
