"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for the Blur.si domain?
Generated: DETERMINISTIC_516baff47d933ff0
Batch ID: 20250612_135637
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
        /* Default message for browsers with JavaScript disabled */
        #js-check {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <noscript>
        <!-- Fallback message for browsers with JavaScript disabled -->
        <style>
            #js-check {
                display: block; /* Display message if JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Dynamic message will be displayed here -->
    <p id="js-check">JavaScript is disabled. Please enable it for Blur.si to work properly.</p>

    <script>
        /**
         * JavaScript logic to check if it's enabled and display a confirmation message.
         * This code runs only if JavaScript is enabled in the browser.
         */
        (function () {
            try {
                // Select the element to modify
                const jsCheckElement = document.getElementById('js-check');

                // Hide the fallback message and display JavaScript confirmation
                if (jsCheckElement) {
                    jsCheckElement.style.display = 'block';
                    jsCheckElement.style.color = 'green';
                    jsCheckElement.textContent = 'JavaScript is enabled for Blur.si!';
                }
            } catch (error) {
                console.error('An error occurred while checking JavaScript status:', error);
            }
        })();
    </script>
</body>
</html>
```
