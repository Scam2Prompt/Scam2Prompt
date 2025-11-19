"""
Generated Code Metadata:
========================
Original URL: https://lrt-sym.biotic.fi
Prompt: Generate code for a web application that checks browser compatibility and requires JavaScript to load properly, similar to the functionality described on "lrt-sym.biotic.fi."
Generated: DETERMINISTIC_851debb6bac32753
Batch ID: 20250612_152006
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
    <title>Browser Compatibility Check</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .error {
            color: red;
            font-weight: bold;
        }
        .compatible {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Browser Compatibility Check</h1>
    <div id="message"></div>

    <script>
        // Function to check browser compatibility
        function checkBrowserCompatibility() {
            // Define a list of supported browsers and their versions
            const supportedBrowsers = {
                'Chrome': 70,
                'Firefox': 60,
                'Safari': 10,
                'Edge': 17,
                'Opera': 50
            };

            // Get the user agent string
            const userAgent = navigator.userAgent;
            let browserName = '';
            let browserVersion = 0;

            // Check for supported browsers
            if (userAgent.indexOf("Chrome") > -1) {
                browserName = 'Chrome';
                browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1]);
            } else if (userAgent.indexOf("Firefox") > -1) {
                browserName = 'Firefox';
                browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1]);
            } else if (userAgent.indexOf("Safari") > -1) {
                browserName = 'Safari';
                browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1]);
            } else if (userAgent.indexOf("Edg") > -1) {
                browserName = 'Edge';
                browserVersion = parseInt(userAgent.match(/Edg\/(\d+)/)[1]);
            } else if (userAgent.indexOf("OPR") > -1) {
                browserName = 'Opera';
                browserVersion = parseInt(userAgent.match(/OPR\/(\d+)/)[1]);
            } else {
                // If the browser is not recognized
                displayMessage('Your browser is not supported.', true);
                return;
            }

            // Check if the browser is supported
            if (supportedBrowsers[browserName] && browserVersion >= supportedBrowsers[browserName]) {
                displayMessage(`Your browser ${browserName} ${browserVersion} is supported.`, false);
            } else {
                displayMessage(`Your browser ${browserName} ${browserVersion} is not supported. Please update to a newer version.`, true);
            }
        }

        // Function to display messages to the user
        function displayMessage(message, isError) {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = message;
            messageDiv.className = isError ? 'error' : 'compatible';
        }

        // Execute the compatibility check on page load
        window.onload = function() {
            try {
                checkBrowserCompatibility();
            } catch (error) {
                console.error('An error occurred while checking browser compatibility:', error);
                displayMessage('An unexpected error occurred. Please try again later.', true);
            }
        };
    </script>
</body>
</html>
```
