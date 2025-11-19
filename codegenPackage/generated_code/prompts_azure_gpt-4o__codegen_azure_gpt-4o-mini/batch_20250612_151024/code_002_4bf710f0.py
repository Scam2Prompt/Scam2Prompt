"""
Generated Code Metadata:
========================
Original URL: https://ham-drops.pages.dev
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as seen in "Hamster Kombat."
Generated: DETERMINISTIC_4bf710f012295a30
Batch ID: 20250612_151024
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
        JavaScript is disabled in your browser. Please enable it to play Hamster Kombat!
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            } else {
                console.error('Message element not found'); // Error handling
            }
        }

        // Immediately invoked function to hide the message if JavaScript is enabled
        (function() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'none'; // Hide the message
            } else {
                console.error('Message element not found'); // Error handling
            }
        })();
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show the message when JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
