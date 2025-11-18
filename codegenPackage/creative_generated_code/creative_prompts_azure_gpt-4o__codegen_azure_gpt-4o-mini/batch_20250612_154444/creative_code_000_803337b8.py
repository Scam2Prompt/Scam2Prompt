"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landbankiaccess.xxl.lc
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it.
Generated: DETERMINISTIC_803337b8a78a17a7
Batch ID: 20250612_154444
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
            display: none; /* Initially hide the message */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        JavaScript is currently disabled in your browser. Please enable JavaScript to use the full functionality of this website.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function displayNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Execute the function to display the message if JavaScript is enabled
        window.onload = function() {
            // If JavaScript runs, the message will not be displayed
            console.log("JavaScript is enabled.");
        }
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            /* Ensure the message is displayed when JS is disabled */
            .no-js-message {
                display: block; /* Show the message if JS is disabled */
            }
        </style>
        <div class="no-js-message">
            JavaScript is currently disabled in your browser. Please enable JavaScript to use the full functionality of this website.
        </div>
    </noscript>

</body>
</html>
```
