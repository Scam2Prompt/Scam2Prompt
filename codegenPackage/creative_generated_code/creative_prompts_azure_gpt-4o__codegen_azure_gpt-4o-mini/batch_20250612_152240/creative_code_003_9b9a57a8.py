"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-coin.pages.dev
Prompt: Write code to display a message prompting users to enable JavaScript for a web app named "W-Coin."
Generated: DETERMINISTIC_9b9a57a85f250de2
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
        /* Basic styling for the message */
        #js-warning {
            display: none; /* Hide by default */
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
        <strong>Warning:</strong> Please enable JavaScript to use the W-Coin web app.
    </div>

    <script>
        // Function to display the warning message
        function displayJsWarning() {
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'block'; // Show the warning message
            } else {
                console.error('Warning div not found in the DOM.');
            }
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JavaScript is enabled, hide the warning
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'none'; // Hide the warning message
            } else {
                console.error('Warning div not found in the DOM.');
            }
        });
    </script>

    <noscript>
        <style>
            /* This style is applied when JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
