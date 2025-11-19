"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltoiken.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a mobile browser for a web app?
Generated: DETERMINISTIC_c85ff560440e68e5
Batch ID: 20250612_163840
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
        /* Styles to show/hide content based on JavaScript availability */
        .no-js {
            display: none;
        }
        .js {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Content to show if JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript in your browser settings to use this web app.</p>
        </div>
    </noscript>

    <!-- Content that requires JavaScript -->
    <div class="js">
        <h1>JavaScript is Enabled</h1>
        <p>Welcome to our web app!</p>
    </div>

    <script>
        /**
         * Function to check if the browser is mobile
         * @returns {boolean} True if the device is mobile, false otherwise
         */
        function isMobileBrowser() {
            return /Mobi|Android/i.test(navigator.userAgent);
        }

        // Log whether JavaScript is enabled and the device type
        if (isMobileBrowser()) {
            console.log("JavaScript is enabled on a mobile browser.");
        } else {
            console.log("JavaScript is enabled, but not on a mobile browser.");
        }
    </script>
</body>
</html>
```
