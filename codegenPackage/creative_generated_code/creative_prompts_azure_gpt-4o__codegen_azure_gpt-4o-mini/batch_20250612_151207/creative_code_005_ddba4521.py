"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientoption2tradepresale.pages.dev
Prompt: Write code to detect whether JavaScript is enabled in a user's browser and display a warning if it is disabled, as seen on the Option2Trade website.
Generated: DETERMINISTIC_ddba45214e21d6f1
Batch ID: 20250612_151207
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
            display: none; /* Hide the warning by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Light red border */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning!</strong> JavaScript is currently disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to display the JavaScript warning
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block'; // Show the warning message
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            // If this script runs, it means JavaScript is enabled, so we hide the warning
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'none';
        });

        // If JavaScript is disabled, the warning message will remain displayed
        // The following code only runs if JavaScript is enabled, as expected
        window.onload = function() {
            // Uncomment the line below to simulate showing the warning (for testing purposes)
            // showWarning();
        };
    </script>

</body>
</html>
```
