"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.sophon.am
Prompt: Create a script that checks for the browser version and alerts users if they are using Internet Explorer 11, as cPanel & WHM no longer supports it.
Generated: DETERMINISTIC_d8b2a1fd41758e4c
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
    <title>Browser Compatibility Check</title>
    <script>
        // Function to check if the user's browser is Internet Explorer 11
        function checkBrowserVersion() {
            // User-Agent string of the browser
            var userAgent = window.navigator.userAgent;

            // Regular expression to match Internet Explorer 11
            var isIE11 = userAgent.indexOf('Trident/') > -1 && userAgent.indexOf('rv:11.0') > -1;

            // If the browser is IE11, display an alert
            if (isIE11) {
                alert("You are using Internet Explorer 11, which is no longer supported by cPanel & WHM. Please upgrade to a modern browser.");
            }
        }

        // Execute the browser check on page load
        window.onload = function() {
            try {
                checkBrowserVersion();
            } catch (error) {
                console.error("An error occurred while checking the browser version:", error);
            }
        };
    </script>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p>Please ensure your browser is up-to-date for the best experience.</p>
</body>
</html>
```
