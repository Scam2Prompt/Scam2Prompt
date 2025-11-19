"""
Generated Code Metadata:
========================
Original URL: https://ethlast.com
Prompt: Create a script that checks for JavaScript support on a mobile device and redirects users to an alternative page if JavaScript is disabled, inspired by the ETH Pledge website functionality.
Generated: DETERMINISTIC_4d9e3fc7db80489a
Batch ID: 20250612_152600
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
    <title>JavaScript Check</title>
    <noscript>
        <meta http-equiv="refresh" content="0; url=/nojs.html">
    </noscript>
    <script>
        // Check for mobile device and JavaScript support
        function checkDeviceAndJS() {
            // Mobile device detection regex
            const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            
            // If JavaScript is disabled, the noscript tag will handle redirection
            // This additional check is for cases where JS might be partially broken
            try {
                if (isMobile) {
                    // Additional mobile-specific checks can be added here
                    console.log("Mobile device detected");
                }
            } catch (e) {
                console.error("JavaScript error detected:", e);
                window.location.href = "/nojs.html";
            }
        }

        // Run check when DOM is loaded
        document.addEventListener('DOMContentLoaded', checkDeviceAndJS);
    </script>
</head>
<body>
    <!-- Main content will be loaded here if JavaScript is enabled -->
    <div id="content">
        <h1>Welcome to our website</h1>
        <p>This content requires JavaScript to function properly.</p>
    </div>
</body>
</html>
```
