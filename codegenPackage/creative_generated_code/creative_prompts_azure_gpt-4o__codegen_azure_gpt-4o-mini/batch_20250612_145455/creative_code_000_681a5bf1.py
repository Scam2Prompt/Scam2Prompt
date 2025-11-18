"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_681a5bf1d2db80bc
Batch ID: 20250612_145455
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
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <!-- Message to be displayed if JavaScript is disabled -->
        <style>
            #js-warning {
                display: block; /* Show warning if JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
    </div>

    <script>
        /**
         * Function to initialize the page and check for JavaScript support.
         * Displays a warning message if JavaScript is disabled.
         */
        function init() {
            try {
                // JavaScript code can go here, if needed
                console.log("JavaScript is enabled.");
            } catch (error) {
                // Log the error to the console if any unexpected error occurs
                console.error("An error occurred while initializing:", error);
            }
        }

        // Call the init function on page load
        window.onload = init;
    </script>
</body>
</html>
```
