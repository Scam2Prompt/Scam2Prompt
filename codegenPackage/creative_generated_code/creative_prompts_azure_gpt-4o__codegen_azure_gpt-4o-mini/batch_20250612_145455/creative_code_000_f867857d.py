"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigbonus.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message prompting them to enable it.
Generated: DETERMINISTIC_f867857d3fd3034b
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
        // Function to show the warning message if JavaScript is disabled
        function showJsWarning() {
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'block'; // Show the warning message
            } else {
                console.error('Warning div not found in the document.');
            }
        }

        // Check if JavaScript is working
        window.onload = function() {
            // This function will run when the page loads
            // If the page has loaded, we can assume JavaScript is enabled
        };
    </script>

    <noscript>
        <style>
            /* If JavaScript is disabled, display the warning message */
            #js-warning {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
