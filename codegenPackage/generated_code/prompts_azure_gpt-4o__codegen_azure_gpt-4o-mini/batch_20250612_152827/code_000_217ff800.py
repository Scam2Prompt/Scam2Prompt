"""
Generated Code Metadata:
========================
Original URL: https://khuga-mint.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message to enable it, similar to the behavior on the "Mint" webpage.
Generated: DETERMINISTIC_217ff8005da37bf8
Batch ID: 20250612_152827
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

    <!-- Message to be displayed if JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to use this site.
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

    <!-- Main content of the page -->
    <h1>Welcome to Our Website</h1>
    <p>This is a sample webpage that requires JavaScript to function properly.</p>

</body>
</html>
```
