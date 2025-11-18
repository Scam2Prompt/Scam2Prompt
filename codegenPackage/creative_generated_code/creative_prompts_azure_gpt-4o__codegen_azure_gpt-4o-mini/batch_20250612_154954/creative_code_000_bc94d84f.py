"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elbdataplanescope.zhy.coinbasenft.de
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting the user to enable it, as seen on the domain details page at elbdataplanescope.zhy.coinbasenft.de.
Generated: DETERMINISTIC_bc94d84ffbf8e898
Batch ID: 20250612_154954
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
        /* Styles for the message if JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red; /* Color for the message */
            font-size: 20px; /* Font size */
            text-align: center; /* Center the text */
            margin-top: 20px; /* Margin from the top */
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function displayNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show the message
            }
        }

        // This function will run if JavaScript is enabled
        function init() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'none'; // Hide the message
            }
        }

        // Execute the init function to hide the message
        init();
    </script>
    
    <noscript>
        <!-- Fallback for when JavaScript is not enabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message when JavaScript is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
