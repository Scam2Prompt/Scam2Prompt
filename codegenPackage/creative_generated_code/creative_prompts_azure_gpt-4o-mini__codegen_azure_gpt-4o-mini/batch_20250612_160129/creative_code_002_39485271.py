"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-soitinyastro.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_160129
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
        // This function checks if JavaScript is enabled
        function checkJavaScript() {
            // Hide the message for disabled JavaScript
            var noJsMessage = document.querySelector('.no-js');
            var jsEnabledMessage = document.querySelector('.js-enabled');

            // Show message for JavaScript enabled
            noJsMessage.style.display = 'none';
            jsEnabledMessage.style.display = 'block';
        }

        // Execute the function to check for JavaScript
        checkJavaScript();
    </script>

</body>
</html>
```
