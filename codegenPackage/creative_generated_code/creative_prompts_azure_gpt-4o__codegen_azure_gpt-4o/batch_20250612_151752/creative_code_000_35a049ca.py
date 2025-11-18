"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getcoins.eu
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the functionality described on https://getcoins.eu.
Generated: DETERMINISTIC_35a049cad717ba64
Batch ID: 20250612_151752
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
    <title>JavaScript Check</title>
    <style>
        /* Style for the message displayed if JavaScript is disabled */
        .no-js-message {
            display: none; /* Default hidden, visible only when JavaScript is disabled */
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Fallback message for browsers with JavaScript disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use this site effectively.
        </div>
    </noscript>

    <!-- Content visible when JavaScript is enabled -->
    <div id="js-enabled-message" style="text-align: center; margin-top: 20px;">
        <p>JavaScript is enabled. Welcome to the site!</p>
    </div>

    <script>
        // JavaScript code runs only if JavaScript is enabled
        (function () {
            try {
                // Get the element with the "no-js-message" class
                const noJsMessage = document.querySelector('.no-js-message');
                
                // Hide the no-JS message (it will only display if JS is disabled)
                if (noJsMessage) {
                    noJsMessage.style.display = 'none';
                }
            } catch (error) {
                // If an exception occurs, log the error to the console
                console.error('An error occurred while checking for JavaScript availability:', error);
            }
        })();
    </script>
</body>
</html>
```
