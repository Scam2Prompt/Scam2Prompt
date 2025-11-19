"""
Generated Code Metadata:
========================
Original URL: https://localcamflings.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript enabled and display a message prompting them to enable it if disabled.
Generated: DETERMINISTIC_ec0976a13e02397d
Batch ID: 20250612_154854
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message
            } else {
                console.error('No JavaScript message element not found.');
            }
        }

        // Immediately invoked function to check if JavaScript is enabled
        (function() {
            // If this script runs, JavaScript is enabled
            // We can safely hide the no-JS message
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            } else {
                console.error('No JavaScript message element not found.');
            }
        })();
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
