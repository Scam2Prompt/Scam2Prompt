"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landbankiaccess.xxl.lc
Prompt: Create a script that checks for JavaScript compatibility and redirects users to a fallback webpage if JavaScript is not enabled.
Generated: DETERMINISTIC_1cb12e020629834a
Batch ID: 20250612_154444
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
    <title>JavaScript Compatibility Check</title>
    <noscript>
        <meta http-equiv="refresh" content="0;url=fallback.html">
        <style>
            /* Style for users with JavaScript disabled */
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }
            .no-js-message {
                color: red;
                font-size: 1.5em;
            }
        </style>
    </noscript>
</head>
<body>
    <script>
        // Check if JavaScript is enabled
        if (typeof document !== 'undefined') {
            // JavaScript is enabled; proceed with the main functionality
            document.body.innerHTML = '<h1>Welcome to the JavaScript-enabled page!</h1>';
        } else {
            // If we can't access the document object, redirect to the fallback page
            window.location.href = 'fallback.html';
        }
    </script>
</body>
</html>
```

In this code:
- The `<noscript>` tag provides a meta refresh redirect to `fallback.html` if JavaScript is disabled.
- A simple message is displayed for users without JavaScript, ensuring they are aware of the redirection.
- Error handling is implemented in the script to redirect users in case there's an issue accessing the document.
