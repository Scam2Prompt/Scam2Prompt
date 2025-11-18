"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkhamintelligence.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the behavior on the Arkham Intelligence website.
Generated: DETERMINISTIC_e456ed609fbd2ab4
Batch ID: 20250612_145238
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
        /* Style for the JavaScript disabled message */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 20px; /* Padding around the message */
            text-align: center; /* Centered text */
            position: absolute; /* Positioned absolutely */
            top: 0; /* At the top of the page */
            left: 0; /* Left aligned */
            width: 100%; /* Full width */
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to display message if JavaScript is disabled
        function showJsDisabledMessage() {
            // Get the message element
            const messageElement = document.getElementById('no-js-message');
            // Show the message element
            messageElement.style.display = 'block';
        }

        // Set a timeout to show the message if the script isn't executed
        setTimeout(showJsDisabledMessage, 100);

        // Main application code goes here
        // Assuming the application needs JavaScript to work properly
        // For example:
        document.addEventListener('DOMContentLoaded', function() {
            // Your application initialization code here
            console.log('JavaScript is enabled. Application initialized.');
        });
    </script>
</body>
</html>
```
