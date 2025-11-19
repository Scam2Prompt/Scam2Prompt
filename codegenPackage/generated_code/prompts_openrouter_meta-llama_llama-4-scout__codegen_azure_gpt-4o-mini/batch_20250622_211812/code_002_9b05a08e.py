"""
Generated Code Metadata:
========================
Original URL: https://eth-usdc.xyz
Prompt: Generate HTML and JavaScript code to create a simple webpage that checks if JavaScript is enabled and displays a custom message if it is not.
Generated: DETERMINISTIC_9b05a08ec63bdaf5
Batch ID: 20250622_211812
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
    <title>JavaScript Check</title>
    <style>
        /* Basic styling for the message */
        #no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <div id="content">
        <h1>Welcome to the JavaScript Check Page</h1>
        <p>If you see this message, JavaScript is enabled.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Select the no-JS message element
            const noJsMessage = document.getElementById('no-js-message');

            // If JavaScript is enabled, we can hide the no-JS message
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Execute the check on page load
        window.onload = checkJavaScript;
    </script>
</body>
</html>
```
