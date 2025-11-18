"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.consesys.io
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a warning message, as required for proper functionality in cPanel.
Generated: DETERMINISTIC_a250c1089d6d1900
Batch ID: 20250612_150329
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
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #ffdddd; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Warning message element -->
    <div id="js-warning">
        JavaScript is disabled in your browser. Please enable it for the full functionality of this site.
    </div>

    <script>
        // Function to show warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning message
            }
        }

        // Attempt to run a script to indicate that JS is enabled
        try {
            // This code will only run if JavaScript is enabled
            console.log('JavaScript is enabled.');
        } catch (error) {
            // Log any errors to the console (although this should not occur in this context)
            console.error('An error occurred:', error);
        }
    </script>

    <!-- This inline script will run when the page loads -->
    <script>
        // Display the warning if JavaScript is disabled
        document.addEventListener('DOMContentLoaded', function() {
            // If this inline script runs, JavaScript is enabled, so we do nothing
        });
    </script>

    <!-- This noscript tag will be rendered if JavaScript is disabled -->
    <noscript>
        <style>
            /* Ensure the warning message is displayed if JS is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
        <div id="js-warning">
            JavaScript is disabled in your browser. Please enable it for the full functionality of this site.
        </div>
    </noscript>

</body>
</html>
```
