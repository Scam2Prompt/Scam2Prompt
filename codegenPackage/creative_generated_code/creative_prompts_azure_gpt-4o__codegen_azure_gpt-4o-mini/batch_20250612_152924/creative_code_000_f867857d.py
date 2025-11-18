"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it.
Generated: DETERMINISTIC_f867857d3fd3034b
Batch ID: 20250612_152924
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
            display: none; /* Initially hide the message */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // This function displays the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block'; // Show the warning message
        }

        // Use the onload event to check if JavaScript is enabled
        window.onload = function() {
            // If the page loads, it means JavaScript is enabled,
            // so we do not need to show the warning.
            // If this script is not executed, JavaScript is disabled.
            showWarning();
        };
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            #js-warning {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>
    
</body>
</html>
```
