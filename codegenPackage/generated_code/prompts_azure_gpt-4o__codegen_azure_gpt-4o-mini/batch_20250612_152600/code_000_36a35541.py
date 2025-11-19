"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message like "Please enable JavaScript to continue," as seen on ETH Pledge's website.
Generated: DETERMINISTIC_36a355411b896819
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        Please enable JavaScript to continue.
    </div>

    <script>
        // Function to hide the no-JS message if JavaScript is enabled
        function hideNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'none'; // Hide the message
            }
        }

        // Call the function to hide the message
        hideNoJsMessage();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            /* Ensure the message is visible when JavaScript is disabled */
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
