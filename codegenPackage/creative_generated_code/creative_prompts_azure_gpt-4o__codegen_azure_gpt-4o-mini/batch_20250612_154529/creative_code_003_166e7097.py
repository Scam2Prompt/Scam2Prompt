"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixdrop.eu
Prompt: Write a script to display a warning message when JavaScript is disabled, ensuring it works on both desktop and mobile browsers.
Generated: DETERMINISTIC_166e7097975457a2
Batch ID: 20250612_154529
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 15px; /* Padding around the text */
            margin: 20px; /* Margin around the warning box */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Center the text */
            font-family: Arial, sans-serif; /* Use a sans-serif font */
        }
    </style>
</head>
<body>
    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        // Function to display the warning message when JavaScript is disabled
        function showWarning() {
            const warningDiv = document.getElementById('js-warning');
            warningDiv.style.display = 'block'; // Show the warning message
        }

        // Check if JavaScript is enabled by setting a flag
        window.onload = function() {
            const warningDiv = document.getElementById('js-warning');
            warningDiv.style.display = 'none'; // Hide warning on page load
        };

        // If JavaScript is disabled, the warning div will remain visible
        // No need to run any additional scripts if JS is disabled
    </script>
</body>
</html>
```
