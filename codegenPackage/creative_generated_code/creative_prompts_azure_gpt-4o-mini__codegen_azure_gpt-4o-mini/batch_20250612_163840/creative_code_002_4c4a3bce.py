"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imotokaen.com
Prompt: Can you provide code snippets to detect if JavaScript is enabled on a mobile device and display a message if it is not?
Generated: DETERMINISTIC_4c4a3bce0e0a3c02
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
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display a message if JavaScript is not enabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show message
            } else {
                console.error('Message div not found');
            }
        }

        // Check for JavaScript enabled status
        window.onload = function() {
            // Hide the no-js message if JavaScript is enabled
            const messageDiv = document.getElementById('no-js-message');
            if (messageDiv) {
                messageDiv.style.display = 'none'; // Hide message
            } else {
                console.error('Message div not found');
            }
        };

        // If JavaScript is disabled, "noscript" tag will show the message
    </script>

    <noscript>
        <style>
            #no-js-message {
                display: block; /* Show message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
