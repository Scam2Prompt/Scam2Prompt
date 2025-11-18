"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://600n-wl-mint.vercel.app
Prompt: Write code to check if JavaScript is enabled in a web application like "600N Mint" and display a warning if it is disabled.
Generated: DETERMINISTIC_e09d2c64212392a6
Batch ID: 20250612_153401
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Warning message styling */
        #js-warning {
            display: none; /* Initially hidden */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="js-warning">Warning: JavaScript is disabled in your browser. Please enable it for the best experience.</div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // If this script runs, JavaScript is enabled
                document.getElementById('js-warning').style.display = 'none';
            } catch (error) {
                // If an error occurs, display the warning
                console.error("Error checking JavaScript status:", error);
                displayWarning();
            }
        }

        // Function to display the warning message
        function displayWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block';
        }

        // Execute the check when the document is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScript);
    </script>
</body>
</html>
```
