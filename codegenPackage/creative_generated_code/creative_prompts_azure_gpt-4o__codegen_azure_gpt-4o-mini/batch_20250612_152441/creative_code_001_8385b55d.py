"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Create a script that checks for Internet Explorer 11 usage and displays a message recommending users to switch browsers, as mentioned on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_8385b55d999fa969
Batch ID: 20250612_152441
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
    <script>
        /**
         * Function to detect if the user is using Internet Explorer 11
         * @returns {boolean} True if the browser is Internet Explorer 11, otherwise false
         */
        function isIE11() {
            // Check for the presence of the 'ActiveXObject' which is specific to IE
            return !!window.ActiveXObject || "ActiveXObject" in window;
        }

        /**
         * Function to display a warning message for Internet Explorer users
         */
        function showIEWarning() {
            const warningMessage = "You are using Internet Explorer 11. For a better experience, please switch to a modern browser like Chrome, Firefox, or Edge.";
            alert(warningMessage);
        }

        // Execute on page load
        window.onload = function() {
            try {
                // If the browser is IE11, show the warning
                if (isIE11()) {
                    showIEWarning();
                }
            } catch (error) {
                console.error("An error occurred while checking the browser: ", error);
            }
        };
    </script>
</head>
<body>
    <h1>Welcome to Dexodoor Webmail</h1>
    <p>Please log in to access your email.</p>
</body>
</html>
```
