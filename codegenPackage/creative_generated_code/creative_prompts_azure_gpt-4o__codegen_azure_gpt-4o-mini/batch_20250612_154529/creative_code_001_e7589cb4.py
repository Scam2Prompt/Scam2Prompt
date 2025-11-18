"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixdrop.eu
Prompt: Create a JavaScript function that checks for browser compatibility and prompts users to enable JavaScript if it is disabled.
Generated: DETERMINISTIC_e7589cb4b545a4a0
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
    <title>Browser Compatibility Check</title>
    <style>
        /* Basic styles for the message */
        #js-warning {
            display: none;
            background-color: #ffcc00;
            padding: 1em;
            border: 1px solid #cc9900;
            margin: 1em 0;
            color: #333;
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JavaScript disabled -->
    <div id="js-warning">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <script>
        /**
         * Checks for browser compatibility and displays a warning if JavaScript is disabled.
         */
        function checkBrowserCompatibility() {
            // Check if the browser supports JavaScript
            if (typeof window !== "undefined" && typeof document !== "undefined") {
                // JavaScript is enabled, hide the warning message
                const warningMessage = document.getElementById('js-warning');
                warningMessage.style.display = 'none';
            } else {
                // JavaScript is not enabled, show the warning message
                const warningMessage = document.getElementById('js-warning');
                warningMessage.style.display = 'block';
            }
        }

        // Execute the browser compatibility check on page load
        window.onload = checkBrowserCompatibility;
    </script>
</body>
</html>
```
