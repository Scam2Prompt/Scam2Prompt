"""
Generated Code Metadata:
========================
Original URL: https://celestia.online
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a warning message if it is disabled.
Generated: DETERMINISTIC_11dfdc564930f674
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <style>
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 10px;
            border: 1px solid #f5c6cb; /* Light red border */
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        /**
         * Function to check if JavaScript is enabled in the browser.
         * If JavaScript is disabled, it will display a warning message.
         */
        function checkJavaScriptEnabled() {
            // Get the warning message element
            const warningElement = document.getElementById('js-warning');

            // Check if the warning element exists
            if (warningElement) {
                // Display the warning message
                warningElement.style.display = 'block';
            } else {
                console.error('Warning element not found in the DOM.');
            }
        }

        // Call the function to check JavaScript status
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <style>
            /* Ensure the warning message is displayed if JavaScript is disabled */
            #js-warning {
                display: block; /* Show warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
