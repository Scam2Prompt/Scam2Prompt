"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a warning message if it is disabled.
Generated: DETERMINISTIC_11dfdc564930f674
Batch ID: 20250612_153728
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
        /* Basic styles for the warning message */
        #jsWarning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="jsWarning">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        /**
         * Function to check if JavaScript is enabled in the browser.
         * If JavaScript is disabled, display a warning message.
         */
        function checkJavaScriptEnabled() {
            // Selecting the warning message div
            const warningDiv = document.getElementById('jsWarning');
            
            // Check if the warningDiv is accessible
            if (!warningDiv) {
                console.error('Warning message element not found.');
                return; // Exit if element cannot be found
            }

            // Display the warning message
            warningDiv.style.display = 'block';
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <style>
            /* Style to show the warning message when JavaScript is disabled */
            #jsWarning {
                display: block; /* Show warning message */
            }
        </style>
        <div id="jsWarning">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

</body>
</html>
```
