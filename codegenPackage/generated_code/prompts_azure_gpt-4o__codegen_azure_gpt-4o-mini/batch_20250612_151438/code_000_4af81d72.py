"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it, similar to the behavior on the Hinge Health EU website.
Generated: DETERMINISTIC_4af81d72263b992e
Batch ID: 20250612_151438
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Message to display when JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript to use this website properly.</p>
    </div>

    <script>
        // Function to hide the no-JS message if JavaScript is enabled
        function hideNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Call the function to hide the message
        hideNoJsMessage();
    </script>

    <!-- Main content of the website -->
    <h1>Welcome to Our Website</h1>
    <p>This is a sample content that requires JavaScript to function properly.</p>

</body>
</html>
```
