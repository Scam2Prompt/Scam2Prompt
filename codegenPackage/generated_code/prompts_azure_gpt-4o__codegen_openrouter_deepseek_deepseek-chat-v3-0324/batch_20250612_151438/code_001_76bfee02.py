"""
Generated Code Metadata:
========================
Original URL: https://equinix.online
Prompt: Create a script that redirects users to a custom error page if JavaScript is disabled on their browser.
Generated: DETERMINISTIC_76bfee027ac9eca1
Batch ID: 20250612_151438
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
        // This script is intentionally left empty to ensure it runs when JS is enabled
    </script>
</head>
<body>
    <!-- Main content of your page goes here -->
    <h1>Welcome to our website</h1>
    <p>This page requires JavaScript to function properly.</p>
</body>
</html>
```

```html
<!-- error/nojs.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Required</title>
</head>
<body>
    <h1>JavaScript is Disabled</h1>
    <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
    <p>If you need assistance, please contact support.</p>
</body>
</html>
```
