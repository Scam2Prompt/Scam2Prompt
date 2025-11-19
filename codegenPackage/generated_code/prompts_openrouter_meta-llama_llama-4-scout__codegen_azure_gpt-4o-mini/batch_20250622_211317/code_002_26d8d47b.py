"""
Generated Code Metadata:
========================
Original URL: https://onc185.vip
Prompt: Generate HTML and JavaScript code to create a simple webpage that shows a message and detects if JavaScript is enabled, inspired by the structure of https://onc185.vip.
Generated: DETERMINISTIC_26d8d47b8352c388
Batch ID: 20250622_211317
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
    <title>JavaScript Detection Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .message {
            padding: 20px;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .js-enabled {
            color: green;
        }
        .js-disabled {
            color: red;
        }
    </style>
</head>
<body>
    <div class="message" id="message">
        <!-- Message will be updated by JavaScript -->
        <p id="status">Checking if JavaScript is enabled...</p>
    </div>

    <noscript>
        <style>
            .message {
                display: none; /* Hide message if JavaScript is disabled */
            }
        </style>
        <div class="message js-disabled">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
        </div>
    </noscript>

    <script>
        // Function to update the message based on JavaScript availability
        function updateMessage() {
            const statusElement = document.getElementById('status');
            statusElement.textContent = 'JavaScript is enabled! Enjoy your experience.';
            statusElement.classList.add('js-enabled');
        }

        // Error handling for unexpected issues
        try {
            // Call the function to update the message
            updateMessage();
        } catch (error) {
            console.error('An error occurred while updating the message:', error);
            const statusElement = document.getElementById('status');
            statusElement.textContent = 'An error occurred. Please try again later.';
        }
    </script>
</body>
</html>
```
