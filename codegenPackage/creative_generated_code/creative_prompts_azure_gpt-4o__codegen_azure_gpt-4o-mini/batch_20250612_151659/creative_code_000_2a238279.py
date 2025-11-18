"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flippingclub.xyz
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "flippingclub doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_2a2382791ed4b72a
Batch ID: 20250612_151659
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
        /* Basic styles for the message */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            padding: 20px;
            border: 1px solid #d8000c;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        flippingclub doesn't work properly without JavaScript enabled.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            // Get the message element
            const messageElement = document.getElementById('no-js-message');
            // Display the message
            messageElement.style.display = 'block';
        }

        // Ensure the message is shown if JavaScript is not executed
        window.onload = function() {
            // This code will run only if JavaScript is enabled
            // If JavaScript is disabled, the message will be displayed by default
            // In this case, we do not need to do anything, as the message is already hidden
        };
    </script>

</body>
</html>
```
