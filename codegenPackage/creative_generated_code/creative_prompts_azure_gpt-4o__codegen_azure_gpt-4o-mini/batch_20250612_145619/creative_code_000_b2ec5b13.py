"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a user's browser and display a message prompting them to enable it if it is disabled.
Generated: DETERMINISTIC_b2ec5b13b0870605
Batch ID: 20250612_145619
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
    <title>Check JavaScript Status</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>

    <noscript>
        <!-- Message displayed if JavaScript is disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience on this site.
        </div>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            const noJsMessage = document.querySelector('.no-js-message');

            // If JavaScript is enabled, we can hide the message
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the no-JS message
            }
        }

        // Error handling to catch any unexpected issues
        try {
            checkJavaScriptEnabled(); // Call the function to check JS status
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
        }
    </script>

</body>
</html>
```
