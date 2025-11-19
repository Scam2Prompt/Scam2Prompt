"""
Generated Code Metadata:
========================
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the behavior described on coinbase.co.za.
Generated: DETERMINISTIC_e73f000cf34e9737
Batch ID: 20250612_154809
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
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Message to display when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to use this site.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            } else {
                console.error('No JavaScript message element not found.');
            }
        }

        // Immediately invoke the function to show the message
        showNoJsMessage();
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            /* Ensure the message is displayed when JavaScript is disabled */
            .no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
