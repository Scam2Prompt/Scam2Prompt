"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the functionality described on the "debridge.global-connect.eu" domain details page.
Generated: DETERMINISTIC_2329373b831d3884
Batch ID: 20250612_151853
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
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it to use this website.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function displayJsDisabledMessage() {
            const messageDiv = document.getElementById('js-disabled-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Ensure the message is displayed if JavaScript is disabled
        window.onload = function() {
            // This message will only be executed if JavaScript is enabled
            console.log('JavaScript is enabled.');

            // Optionally, you can remove the message if JavaScript is enabled
            const messageDiv = document.getElementById('js-disabled-message');
            if (messageDiv) {
                messageDiv.style.display = 'none'; // Hide the message
            }
        };

        // Create a simple try-catch to handle any unexpected errors during execution
        try {
            // Main logic can be placed here if needed
        } catch (error) {
            console.error('An error occurred: ', error);
        }
    </script>

    <noscript>
        <!-- This provides a message when JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show the message when JS is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
