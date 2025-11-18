"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.pages.dev
Prompt: Create a script to detect if JavaScript is disabled and display a message prompting users to enable it for the "PulseX" app.
Generated: DETERMINISTIC_2c907abfd7f07f47
Batch ID: 20250612_154413
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
    <title>PulseX App</title>
    <style>
        /* Styles for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide message by default */
            background-color: #ffdddd;
            color: #d8000c;
            border: 1px solid #d8000c;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use the PulseX app.
    </div>

    <script>
        // Function to show the no-JS message
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is running
        document.addEventListener('DOMContentLoaded', () => {
            // JavaScript is enabled, so we hide the message
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none'; // Hide the message
        });
    </script>

    <noscript>
        <!-- Display message to users with JavaScript disabled -->
        <style>
            /* Ensure the message is visible without JavaScript */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>
</body>
</html>
```
