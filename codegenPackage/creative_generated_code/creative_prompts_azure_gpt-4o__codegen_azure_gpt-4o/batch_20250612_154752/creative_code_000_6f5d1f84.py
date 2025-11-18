"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://combo.magiceden.nl
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on the Magic Eden NL domain details page.
Generated: DETERMINISTIC_6f5d1f8455c31d50
Batch ID: 20250612_154752
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
    <title>JavaScript Disabled Detection</title>
    <style>
        /* Style for the no-JavaScript message */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-size: 1.2em;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this site.
        </div>
    </noscript>

    <!-- Content of the page -->
    <div id="app">
        <h1>Welcome to Our Website!</h1>
        <p>The content of this page requires JavaScript to be enabled in your browser.</p>
    </div>

    <script>
        // JavaScript section
        // Ensure the functionality works and hides the no-JavaScript message
        // when JavaScript is enabled

        (function () {
            'use strict';
        
            // Select all elements with the class "no-js-message"
            const noJsMessage = document.querySelector('.no-js-message');
            
            // Hide the message if JavaScript is enabled
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        })();
    </script>
</body>
</html>
```
