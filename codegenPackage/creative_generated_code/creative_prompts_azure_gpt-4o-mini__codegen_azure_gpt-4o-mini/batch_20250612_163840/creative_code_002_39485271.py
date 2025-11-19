"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethdrt.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_163840
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
            try {
                // Select the elements to manipulate
                const noJsMessage = document.querySelector('.no-js');
                const jsEnabledMessage = document.querySelector('.js-enabled');
                
                // Check if elements are found before attempting to manipulate them
                if (noJsMessage && jsEnabledMessage) {
                    // Hide the no-JS message and show the JS-enabled message
                    noJsMessage.style.display = 'none';
                    jsEnabledMessage.style.display = 'block';
                } else {
                    // Log an error if elements are not found
                    console.error('Unable to find message elements for JavaScript detection.');
                }
            } catch (error) {
                // Log any unexpected errors
                console.error('An error occurred while detecting JavaScript:', error);
            }
        }

        // Run the detection function when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', detectJavaScript);
    </script>

</body>
</html>
```
