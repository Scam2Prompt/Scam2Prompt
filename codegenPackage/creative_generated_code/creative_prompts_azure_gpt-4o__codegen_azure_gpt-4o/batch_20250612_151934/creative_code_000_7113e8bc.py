"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message to enable it.
Generated: DETERMINISTIC_7113e8bc9f53fa00
Batch ID: 20250612_151934
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
        /* Styling for the no-JavaScript message */
        .no-js-message {
            display: none; /* Initially hidden */
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Default message shown when JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <!-- This will be hidden if JavaScript is enabled -->
    <div id="js-enabled-message" style="display: none;">
        JavaScript is enabled. Welcome to the site!
    </div>

    <script>
        // Error handling for scenarios where DOM manipulation might fail
        try {
            // Select the element to display the enabled message
            const jsEnabledMessage = document.getElementById('js-enabled-message');

            // Ensure the element exists before acting on it
            if (jsEnabledMessage) {
                // Reveal the message that JavaScript is enabled
                jsEnabledMessage.style.display = 'block';
            }
        } catch (error) {
            // Log any errors to the console for debugging purposes
            console.error('An error occurred while detecting JavaScript:', error);
        }
    </script>
</body>
</html>
```
