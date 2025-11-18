"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message, similar to the behavior described on the mtec.cyou webpage.
Generated: DETERMINISTIC_82b48da5070ed64e
Batch ID: 20250612_150446
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default, will be shown if JS is disabled */
            color: red;
            font-size: 18px;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Container for the custom message -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>

    <script>
        // Function to show the no-JS message
        function showNoJsMessage() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'block'; // Show the message
            }
        }

        // Self-invoking function to hide the no-JS message if JS is enabled
        (function() {
            const messageElement = document.getElementById('no-js-message');
            if (messageElement) {
                messageElement.style.display = 'none'; // Hide the message
            }
        })();
    </script>
</body>
</html>
```
