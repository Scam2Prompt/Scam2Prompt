"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genixs.co
Prompt: Generate code to detect whether JavaScript is disabled in a browser and display a custom message instructing users to enable it.
Generated: DETERMINISTIC_8da31b174fa8948f
Batch ID: 20250612_154344
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
            display: none; /* Initially hidden */
            color: red;
            font-size: 1.2em;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Message to instruct users to enable JavaScript -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this website.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function displayNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message
            }
        }

        // If this code runs, it means JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        });

        // Handle any potential errors during execution
        try {
            // Check if the document is loaded and ready
            if (document.readyState === 'complete') {
                // Code to run when the document is fully loaded
            }
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
        }
    </script>
</body>
</html>
```
