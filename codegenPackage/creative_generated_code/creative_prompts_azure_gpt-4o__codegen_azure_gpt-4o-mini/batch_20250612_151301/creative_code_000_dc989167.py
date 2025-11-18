"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionairerabbit.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, as required by the Billionaire Rabbit app.
Generated: DETERMINISTIC_dc9891671702982a
Batch ID: 20250612_151301
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
    <title>Billionaire Rabbit App</title>
    <style>
        /* Styles for the message */
        #js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Center the text */
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable JavaScript to use the Billionaire Rabbit app.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled.
        function showJsDisabledMessage() {
            const message = document.getElementById('js-disabled-message');
            message.style.display = 'block'; // Show the message
        }

        // This script will run if JavaScript is enabled
        window.onload = function() {
            // Hide the message if JavaScript is enabled
            const message = document.getElementById('js-disabled-message');
            message.style.display = 'none'; // Ensure the message is hidden
        };

        // Set a timeout to show the message after a short delay
        // This allows the page to load fully before checking
        setTimeout(showJsDisabledMessage, 1000); // Show message after 1 second if JS is not enabled
    </script>

</body>
</html>
```
