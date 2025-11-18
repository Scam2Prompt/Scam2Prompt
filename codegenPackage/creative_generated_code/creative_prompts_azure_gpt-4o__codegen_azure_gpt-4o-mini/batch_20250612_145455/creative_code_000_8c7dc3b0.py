"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message like "Please enable JavaScript to continue."
Generated: DETERMINISTIC_8c7dc3b09d79694d
Batch ID: 20250612_145455
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
        /* Styles for the message when JS is disabled */
        #js-disabled-message {
            display: none; /* Hide the message by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 18px;
            margin: 20px 0;
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        Please enable JavaScript to continue.
    </div>

    <script>
        // Function to display the message when JavaScript is enabled
        function hideJsDisabledMessage() {
            const messageElement = document.getElementById('js-disabled-message');
            messageElement.style.display = 'none';
        }

        // Call the function to hide the message
        hideJsDisabledMessage();
    </script>

    <noscript>
        <!-- This block is rendered if JavaScript is disabled -->
        <style>
            #js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

    <h1>Welcome to Our Website</h1>
    <p>Here is some content that requires JavaScript to function properly.</p>

</body>
</html>
```
