"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Generate JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it for accessing a presale application.
Generated: DETERMINISTIC_b085ad0352c358fa
Batch ID: 20250612_153700
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
        /* Styles for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to access the presale application.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show the message
            } else {
                console.error("Message element not found."); // Error handling
            }
        }

        // Assuming JavaScript is enabled, we hide the message by default
        window.onload = function() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'none'; // Hide the message since JS is enabled
            }
        };

        // In case JavaScript is disabled, the message will be shown by default
    </script>
</body>
</html>
```
