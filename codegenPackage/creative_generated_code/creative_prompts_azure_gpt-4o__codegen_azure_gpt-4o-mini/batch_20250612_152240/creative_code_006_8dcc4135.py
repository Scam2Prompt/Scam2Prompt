"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-coinio.pages.dev
Prompt: Create a JavaScript function to check if JavaScript is enabled in the browser for an app named "W-Coin" and display a warning if it is disabled.
Generated: DETERMINISTIC_8dcc413533655005
Batch ID: 20250612_152240
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
    <title>W-Coin</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Initially hidden */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Red border */
            padding: 15px; /* Some padding */
            margin: 20px; /* Margin around the warning */
            border-radius: 5px; /* Slightly rounded corners */
        }
    </style>
</head>
<body>
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it to use W-Coin.
    </div>

    <script>
        /**
         * Function to check if JavaScript is enabled.
         * Displays a warning message if JavaScript is disabled in the browser.
         */
        function checkJavaScriptEnabled() {
            // Get the warning element
            const warningElement = document.getElementById('js-warning');

            // Check if the warning element exists
            if (!warningElement) {
                console.error('Warning element not found in the DOM.');
                return;
            }

            // Display the warning message if JavaScript is disabled
            warningElement.style.display = 'block';
        }

        // Invoke the function to check for JavaScript
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
