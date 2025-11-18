"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcioo.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message like "BTC Pledge requires JavaScript enabled to function properly."
Generated: DETERMINISTIC_e957526e28037605
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
    <title>JavaScript Check</title>
    <style>
        /* Style for the message */
        .js-disabled-message {
            display: none; /* Initially hidden */
            color: red;
            font-size: 18px;
            margin: 20px;
        }
    </style>
</head>
<body>

    <div class="js-disabled-message" id="js-disabled-message">
        BTC Pledge requires JavaScript enabled to function properly.
    </div>

    <script>
        // Function to display the warning message if JavaScript is not enabled
        function displayJsDisabledMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the warning message
            } else {
                console.error('Error: Unable to find the message element.'); // Log an error if the element is not found
            }
        }

        // Run the function to display the message for non-JS users
        displayJsDisabledMessage();
    </script>

</body>
</html>
```
