"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbsc.com
Prompt: Provide an example of JavaScript code that checks for JavaScript being enabled in a browser and displays a warning if it is disabled.
Generated: DETERMINISTIC_d42663643150a3c5
Batch ID: 20250612_152329
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border: 1px solid #f5c6cb; /* Border color */
        }
    </style>
</head>
<body>

    <div class="warning" id="js-warning">
        Warning: JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <noscript>
        <style>
            /* Style the warning message visible when JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning */
            }
        </style>
    </noscript>

    <script>
        // Function to show a warning if JavaScript is disabled
        function checkJavaScriptEnabled() {
            // Get the warning element
            const warningElement = document.getElementById('js-warning');

            // If JavaScript is enabled, hide the warning
            if (warningElement) {
                warningElement.style.display = 'none';
            } else {
                // If the element is not found, log an error
                console.error('Warning element not found in the DOM.');
            }
        }

        // Execute the function to check JavaScript status
        try {
            checkJavaScriptEnabled();
        } catch (error) {
            // Catch any unexpected errors and log them
            console.error('An error occurred while checking for JavaScript:', error);
        }
    </script>

</body>
</html>
```
