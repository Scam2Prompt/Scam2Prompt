"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakewise.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_163717
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
        /* Styles to hide the message if JavaScript is enabled */
        .no-js {
            display: block;
        }
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js">
        <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
    </div>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js-enabled">
        <p>JavaScript is enabled. Welcome to our web application!</p>
    </div>

    <script>
        // Function to hide the no-JS message and show the JS-enabled message
        function detectJavaScript() {
            const noJsMessage = document.querySelector('.no-js');
            const jsEnabledMessage = document.querySelector('.js-enabled');

            if (noJsMessage && jsEnabledMessage) {
                noJsMessage.style.display = 'none'; // Hide the no-JS message
                jsEnabledMessage.style.display = 'block'; // Show the JS-enabled message
            } else {
                console.error('Could not find the necessary elements for JavaScript detection.');
            }
        }

        // Execute the detection function
        detectJavaScript();
    </script>
</body>
</html>
```
