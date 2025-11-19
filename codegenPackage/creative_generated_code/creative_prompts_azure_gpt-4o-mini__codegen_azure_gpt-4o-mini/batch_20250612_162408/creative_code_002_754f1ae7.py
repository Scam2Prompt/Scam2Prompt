"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.coinbasenft.eu
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_754f1ae758165e3b
Batch ID: 20250612_162408
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
        /* Basic styling for the no-JS message */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is not enabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>

    <!-- Main content of the web application -->
    <div id="content">
        <h1>Welcome to Our Web Application</h1>
        <p>Your JavaScript is enabled!</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Select the no-JS message element
            const noJsMessage = document.querySelector('.no-js-message');

            // If the message element exists, we can assume JS is enabled
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the no-JS message
            }
        }

        // Call the function on page load
        window.onload = function() {
            try {
                checkJavaScriptEnabled(); // Check if JS is enabled
            } catch (error) {
                console.error('Error checking JavaScript status:', error);
            }
        };
    </script>
</body>
</html>
```
