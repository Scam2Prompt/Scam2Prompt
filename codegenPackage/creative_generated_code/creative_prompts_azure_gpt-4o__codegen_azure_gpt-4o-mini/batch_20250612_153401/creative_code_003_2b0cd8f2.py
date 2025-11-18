"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-drago.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
Batch ID: 20250612_153401
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
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffcc00; /* Warning color */
            color: #000;
            padding: 10px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to show the message when JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show the message
            }
        }

        // This script will run if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            // Hide the message if JavaScript is running
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'none'; // Hide the message
            }
        });

        // Call the function to show the message if the script is executed
        showNoJsMessage();
    </script>
</body>
</html>
```
