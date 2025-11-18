"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localcamflings.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript enabled and display a message prompting them to enable it if disabled.
Generated: DETERMINISTIC_ec0976a13e02397d
Batch ID: 20250612_154854
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
        /* Styles for the message to be displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript to enhance your experience.
    </div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            const noJsMessage = document.getElementById('no-js-message');
            // If JavaScript is enabled, hide the message
            noJsMessage.style.display = 'none';
        }

        // Execute the function to detect JavaScript
        detectJavaScript();
    </script>

    <!-- If JavaScript is disabled, the following inline script will not execute -->
    <noscript>
        <style>
            #no-js-message {
                display: block; /* Display the message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
