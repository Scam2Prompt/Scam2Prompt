"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstract.co.in
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and displays a message if it is not.
Generated: DETERMINISTIC_04440d8175906668
Batch ID: 20250612_155805
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red; /* Message color */
            font-weight: bold; /* Make the text bold */
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message" id="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this site.
        </div>
    </noscript>

    <script>
        // Function to display a message if JavaScript is not enabled
        function checkJavaScriptEnabled() {
            // Get the message element
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                // If JavaScript is enabled, hide the no-JS message
                noJsMessage.style.display = 'none';
            } else {
                // Log an error if the message element is not found
                console.error('No JavaScript message element not found.');
            }
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
