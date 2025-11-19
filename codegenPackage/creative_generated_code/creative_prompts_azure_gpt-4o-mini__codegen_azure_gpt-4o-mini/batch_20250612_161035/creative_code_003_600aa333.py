"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogsontondrop.pages.dev
Prompt: Create a function that displays a message to users if JavaScript is disabled in their browser.
Generated: DETERMINISTIC_600aa333aa4c9351
Batch ID: 20250612_161035
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
    <title>JavaScript Disabled Check</title>
    <style>
        /* Style for the warning message */
        .js-disabled-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Warning message for users with JavaScript disabled -->
    <div id="jsDisabledMessage" class="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to display a message if JavaScript is disabled
        function checkJavaScriptEnabled() {
            // Get the message element
            const messageElement = document.getElementById('jsDisabledMessage');

            // If JavaScript is enabled, we hide the message
            messageElement.style.display = 'none';
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();

        // Display the warning message if JavaScript is disabled
        // This is done by using the <noscript> tag
    </script>

    <noscript>
        <style>
            /* Ensure the message is displayed when JavaScript is disabled */
            #jsDisabledMessage {
                display: block;
            }
        </style>
    </noscript>

</body>
</html>
```
