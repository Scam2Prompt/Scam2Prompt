"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lrt-sym.biotic.fi
Prompt: Create a script that redirects users to an error page if JavaScript is disabled, inspired by the behavior of the "lrt-sym.biotic.fi" domain details page.
Generated: DETERMINISTIC_a2c42fd61c391db6
Batch ID: 20250612_152006
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
    <title>Redirect if JavaScript Disabled</title>
    <noscript>
        <!-- If JavaScript is disabled, users will immediately be redirected to the error page -->
        <meta http-equiv="refresh" content="0;url=/error.html">
    </noscript>
    <script>
        /**
         * Ensure proper handling if JavaScript is enabled.
         * If this script runs without interruption, users will
         * remain on the current page.
         * In case JavaScript is disabled, <noscript> will handle the redirection.
         */
        (function () {
            console.log("JavaScript is enabled, user stays on the page.");
        })();
    </script>
</head>
<body>
    <h1>Welcome to the Page</h1>
    <p>If JavaScript is disabled, you will be redirected to an error page.</p>
</body>
</html>
```
