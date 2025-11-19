"""
Generated Code Metadata:
========================
Original URL: https://foxylinea.presale.com
Prompt: Create a function that detects JavaScript support in a user's browser and displays a message if it's disabled.
Generated: DETERMINISTIC_77485abcf452a50c
Batch ID: 20250612_135152
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
    <title>JavaScript Support Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to detect JavaScript support
        function detectJavaScriptSupport() {
            // Get the message element
            const noJsMessage = document.getElementById('no-js-message');

            // Check if the message element exists
            if (noJsMessage) {
                // If JavaScript is enabled, hide the message
                noJsMessage.style.display = 'none';
            } else {
                // Log an error if the message element is not found
                console.error('No JavaScript support message element found.');
            }
        }

        // Call the function to detect JavaScript support
        detectJavaScriptSupport();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</body>
</html>
```
