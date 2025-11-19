"""
Generated Code Metadata:
========================
Original URL: https://jrny.world
Prompt: Create a script to detect if JavaScript is disabled in a browser and display a message prompting users to enable JavaScript for the "JRNY" app.
Generated: DETERMINISTIC_8f4789e0fd6d5ba4
Batch ID: 20250612_154344
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
    <title>JRNY App</title>
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
    <div id="no-js-message" class="no-js-message">
        <strong>JavaScript is disabled!</strong> Please enable JavaScript in your browser settings to use the JRNY app.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            }
        }

        // Call the function to show the message
        showNoJsMessage();
    </script>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
