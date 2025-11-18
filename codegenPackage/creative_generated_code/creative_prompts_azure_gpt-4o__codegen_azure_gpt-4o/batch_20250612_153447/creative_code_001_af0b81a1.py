"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Create a script that checks if a user is accessing a webpage using Internet Explorer 11 and displays a message recommending an alternative browser, as mentioned in the Webmail login page of https://webmail.everclear.pk.
Generated: DETERMINISTIC_af0b81a18d306a11
Batch ID: 20250612_153447
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
    <title>Browser Check</title>
    <style>
        /* Basic styling for the warning message */
        .browser-warning {
            display: none; /* Hidden by default */
            padding: 20px;
            margin: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Warning message that will be displayed if user is on IE11 -->
    <div id="warning" class="browser-warning">
        You are using Internet Explorer 11, which is outdated. For a better experience, please use a modern browser like Google Chrome, Mozilla Firefox, or Microsoft Edge.
    </div>

    <script>
        /**
         * Function to detect Internet Explorer 11.
         * Returns true if the browser is IE11, otherwise false.
         */
        function isIE11() {
            // Check the user agent for IE11 signature
            return !!window.MSInputMethodContext && !!document.documentMode;
        }

        // Main logic to check the browser and display the warning if necessary
        (function () {
            try {
                // If browser is IE11, show the warning message
                if (isIE11()) {
                    const warningDiv = document.getElementById('warning');
                    warningDiv.style.display = 'block'; // Make the warning visible
                }
            } catch (error) {
                // Log unexpected errors to the console for debugging
                console.error('An error occurred while detecting the browser:', error);
            }
        })();
    </script>
</body>
</html>
```
