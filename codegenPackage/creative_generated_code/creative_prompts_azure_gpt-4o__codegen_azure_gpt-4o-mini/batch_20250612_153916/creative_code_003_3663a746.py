"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-dex-contest-nine.vercel.app
Prompt: Write code to check if JavaScript is enabled in a user's browser and display a message if it is disabled.
Generated: DETERMINISTIC_3663a7465a0d4b14
Batch ID: 20250612_153916
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
        /* Styling for the message when JavaScript is disabled */
        .no-js {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
        /* Styling for when JavaScript is enabled */
        .js-enabled {
            display: block; /* Show when JS is enabled */
            color: green;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <div class="js-enabled">
        JavaScript is enabled in your browser. Enjoy our website!
    </div>

    <script>
        // This script checks if JavaScript is enabled.
        // Upon loading the page, if JavaScript is enabled, 
        // the message for the enabled state will be displayed.

        // Function to show a friendly message when JavaScript is enabled
        function showJsEnabledMessage() {
            const jsEnabledMessage = document.querySelector('.js-enabled');
            jsEnabledMessage.style.display = 'block'; // Display the message
        }

        // Check for the presence of DOMContentLoaded event for fully loaded HTML
        document.addEventListener('DOMContentLoaded', () => {
            try {
                showJsEnabledMessage();
            } catch (error) {
                console.error('An error occurred while checking JavaScript status:', error);
            }
        });
    </script>
</body>
</html>
```
