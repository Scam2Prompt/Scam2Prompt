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

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Styles for the warning message */
        #no-js-warning {
            display: none; /* Hidden by default */
            padding: 20px;
            background-color: #ffcccb; /* Light red background */
            color: #000; /* Black text */
            border: 1px solid #f44336; /* Red border */
            border-radius: 5px;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px auto;
            max-width: 600px;
        }
    </style>
</head>
<body>
    <!-- Warning message to be displayed if JavaScript is disabled -->
    <noscript>
        <div id="no-js-warning">
            JavaScript is disabled in your browser. Please enable JavaScript for proper functionality.
        </div>
    </noscript>

    <script>
        // Ensure the warning message doesn't display if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Locating the element that contains the warning message
                const warningElement = document.getElementById('no-js-warning');
                
                // If the warning element exists, hide it (JavaScript is enabled)
                if (warningElement) {
                    warningElement.style.display = 'none';
                }
            } catch (error) {
                // If there's an error while executing, log it for debugging purposes
                console.error('Error handling JavaScript detection:', error);
            }
        });
    </script>
</body>
</html>
```
