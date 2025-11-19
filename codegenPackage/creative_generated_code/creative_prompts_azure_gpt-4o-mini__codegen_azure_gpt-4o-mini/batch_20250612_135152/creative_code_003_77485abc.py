"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxylinea.presale.com
Prompt: Create a function that detects JavaScript support in a user's browser and displays a message if it's disabled.
Generated: DETERMINISTIC_77485abcf452a50c
Batch ID: 20250612_135152
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
    <title>JavaScript Support Detection</title>
    <style>
        /* Styling for the message */
        #js-disabled-message {
            display: none; /* Hide by default */
            color: red; /* Message color */
            font-weight: bold; /* Bold text */
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        /**
         * Function to detect JavaScript support.
         * Displays a message if JavaScript is disabled in the browser.
         */
        function detectJavaScriptSupport() {
            try {
                // Check if the function is running
                console.log('JavaScript is enabled.');

                // If JavaScript is enabled, hide the message
                document.getElementById('js-disabled-message').style.display = 'none';
            } catch (error) {
                // Log any errors that occur
                console.error('An error occurred while detecting JavaScript support:', error);
            }
        }

        // Call the function to detect JavaScript support
        detectJavaScriptSupport();
    </script>

    <!-- The following <noscript> tag provides a message for users with JavaScript disabled -->
    <noscript>
        <style>
            #js-disabled-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

</body>
</html>
```
