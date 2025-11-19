"""
Generated Code Metadata:
========================
Original URL: https://lending-ui-beta.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the functionality of the Honey App.
Generated: DETERMINISTIC_2e69ce101c89a396
Batch ID: 20250612_153401
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
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript to use this application.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Immediately invoked function to set up the message
        (function() {
            // Check if JavaScript is enabled
            if (document.readyState === 'complete') {
                // If the document is fully loaded, hide the message
                const messageDiv = document.getElementById('no-js-message');
                messageDiv.style.display = 'none'; // Hide the message
            } else {
                // If the document is not fully loaded, show the message
                showNoJsMessage();
            }
        })();
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
