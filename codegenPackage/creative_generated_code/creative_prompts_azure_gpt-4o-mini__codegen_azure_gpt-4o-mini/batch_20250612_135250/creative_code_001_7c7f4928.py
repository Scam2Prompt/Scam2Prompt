"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and prompts the user to enable it for the Arbitrum site.
Generated: DETERMINISTIC_7c7f49286d1c45bb
Batch ID: 20250612_135250
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
        /* Styling for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around the message */
            text-align: center; /* Centered text */
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript for the Arbitrum site to function properly.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Attempt to display the message if JavaScript is disabled
            var noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'block'; // Show the message
        }

        // If JavaScript is running, we can hide the message
        window.onload = function() {
            // Hide the message since JavaScript is enabled
            var noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none'; // Hide the message
        };

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
