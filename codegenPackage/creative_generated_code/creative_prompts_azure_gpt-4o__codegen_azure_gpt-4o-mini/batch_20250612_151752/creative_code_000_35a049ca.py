"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getcoins.eu
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the functionality described on https://getcoins.eu.
Generated: DETERMINISTIC_35a049cad717ba64
Batch ID: 20250612_151752
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            padding: 10px;
            border: 1px solid red;
            background-color: #f8d7da;
        }
    </style>
</head>
<body>

    <!-- Message to be displayed when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to display the message when JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            }
        }

        // Execute the function to ensure the message is hidden if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'none'; // Hide the message
            }
        });

        // Error handling to catch any potential issues
        try {
            // Placeholder for any future JavaScript code
            console.log("JavaScript is enabled."); // Log to console for confirmation
        } catch (error) {
            console.error('An error occurred:', error); // Log any errors to the console
        }
    </script>
</body>
</html>
```
