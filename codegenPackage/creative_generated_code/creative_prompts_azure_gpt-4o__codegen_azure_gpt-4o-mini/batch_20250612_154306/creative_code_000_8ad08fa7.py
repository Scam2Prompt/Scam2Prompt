"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, as suggested by the functionality described on the Step App domain page.
Generated: DETERMINISTIC_8ad08fa70cebd9a2
Batch ID: 20250612_154306
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
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Immediately invoke the function to show the message
        showNoJsMessage(); // This will not run if JavaScript is enabled

        // If JavaScript is enabled, hide the message
        document.addEventListener('DOMContentLoaded', function () {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'none'; // Hide the message
        });
    </script>
</body>
</html>
```
