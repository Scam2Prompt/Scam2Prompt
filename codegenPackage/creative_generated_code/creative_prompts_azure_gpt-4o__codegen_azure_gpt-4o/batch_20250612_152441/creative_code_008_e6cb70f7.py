"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.dexodoor.com
Prompt: Provide code to detect if a browser supports JavaScript and redirect users to an error page if JavaScript is disabled, similar to the cPanel functionality.
Generated: DETERMINISTIC_e6cb70f751009e4a
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
    <title>JavaScript Detection</title>
    <!-- Redirect to an error page if JavaScript is disabled -->
    <noscript>
        <meta http-equiv="refresh" content="0;url=/javascript-disabled.html">
    </noscript>
</head>
<body>
    <!-- Content visible when JavaScript is enabled -->
    <h1>Welcome! JavaScript is enabled in your browser.</h1>

    <script>
        // Optional: Add logic here if needed for when JavaScript is enabled.
        console.log("JavaScript is enabled!");
    </script>
</body>
</html>
```

This code ensures users are redirected to `/javascript-disabled.html` if JavaScript is disabled in their browser.
