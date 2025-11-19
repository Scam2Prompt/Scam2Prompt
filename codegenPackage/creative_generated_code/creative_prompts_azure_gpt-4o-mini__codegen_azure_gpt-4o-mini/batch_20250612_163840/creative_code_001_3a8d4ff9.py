"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btxumh.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled in the browser and displays a message if it is not.
Generated: DETERMINISTIC_3a8d4ff97a398b1e
Batch ID: 20250612_163840
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
        /* Style for the message to be displayed when JS is disabled */
        .no-js-message {
            display: none; /* Initially hide the message */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            const messageElement = document.querySelector('.no-js-message');
            // If JavaScript is running, hide the message (if it exists)
            if (messageElement) {
                messageElement.style.display = 'none';
            }
        }

        // Execute the check on script load
        try {
            checkJavaScriptEnabled();
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
        }
    </script>
</body>
</html>
```
