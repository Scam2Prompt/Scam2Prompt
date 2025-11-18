"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message like "You need to enable JavaScript to run this app," similar to the BONKBOXES whitelist page.
Generated: DETERMINISTIC_7e84b6366254f4f5
Batch ID: 20250612_150602
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
    <title>JavaScript Check</title>
    <style>
        /* Basic styling for the message */
        #no-js-message {
            display: none; /* Hide the message by default */
            background-color: #ffcccc;
            color: #cc0000;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 1px solid #cc0000;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        You need to enable JavaScript to run this app.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Make the message visible
            }
        }

        // Invoke the function to display the message if JavaScript is enabled
        showNoJsMessage();
    </script>

    <noscript>
        <!-- This block is displayed only if JavaScript is disabled -->
        <div id="no-js-message" style="display: block;">
            You need to enable JavaScript to run this app.
        </div>
    </noscript>
</body>
</html>
```
