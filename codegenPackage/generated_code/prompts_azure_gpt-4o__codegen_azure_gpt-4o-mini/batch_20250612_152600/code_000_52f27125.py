"""
Generated Code Metadata:
========================
Original URL: https://ethlast.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a warning message, similar to the behavior described on the ETH Pledge website.
Generated: DETERMINISTIC_52f271250ab965a0
Batch ID: 20250612_152600
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning message
            }
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JavaScript is enabled, we can hide the warning
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'none'; // Hide the warning message
            }
        });

        // Fallback for browsers that do not support JavaScript
        window.onload = function() {
            // If the page is loaded without JavaScript, show the warning
            showWarning();
        };
    </script>
</body>
</html>
```
