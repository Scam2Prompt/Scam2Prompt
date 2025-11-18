"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminiig.com
Prompt: Generate a JavaScript snippet to detect if JavaScript is disabled in a browser and display a message like the one on geminiig.com.
Generated: DETERMINISTIC_d9be0ad77d80f406
Batch ID: 20250612_152600
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            background-color: #ffcc00;
            color: #000;
            padding: 20px;
            text-align: center;
            font-size: 18px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Message to display when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        It seems that JavaScript is disabled in your browser. Please enable it to view this website properly.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            messageElement.style.display = 'block'; // Show the message
        }

        // Execute the function to show the message
        showNoJsMessage();
    </script>

    <noscript>
        <!-- Fallback for users with JavaScript disabled -->
        <style>
            #no-js-message {
                display: block; /* Show message if JS is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
