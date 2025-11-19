"""
Generated Code Metadata:
========================
Original URL: https://lrt-sym.biotic.fi
Prompt: Create a script that redirects users to an error page if JavaScript is disabled, inspired by the behavior of the "lrt-sym.biotic.fi" domain details page.
Generated: DETERMINISTIC_a2c42fd61c391db6
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
    <title>JavaScript Required</title>
    <noscript>
        <meta http-equiv="refresh" content="0; url=/error/nojs.html">
    </noscript>
    <script>
        // This script checks if JavaScript is enabled and removes the noscript tag
        document.addEventListener('DOMContentLoaded', function() {
            var noscript = document.querySelector('noscript');
            if (noscript) {
                noscript.parentNode.removeChild(noscript);
            }
        });
    </script>
</head>
<body>
    <!-- Your normal page content goes here -->
    <h1>Welcome to our website</h1>
    <p>This page requires JavaScript to function properly.</p>
</body>
</html>
```
