"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: Create a script that checks for JavaScript support in a browser and redirects users to a fallback page if JavaScript is disabled.
Generated: DETERMINISTIC_2900a3ff568b41f1
Batch ID: 20250612_151018
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
    <title>JavaScript Support Check</title>
    <style>
        /* Basic styles for fallback page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
    <noscript>
        <!-- Fallback content for users without JavaScript -->
        <meta http-equiv="refresh" content="0;url=fallback.html">
    </noscript>
    <script>
        // Check if JavaScript is enabled
        (function() {
            // This function will execute if JavaScript is enabled
            console.log("JavaScript is enabled.");

            // Add your main script functionality here
            // ...

            // Optionally: Redirect to a main page if needed
            // window.location.href = 'main.html';
        })();
    </script>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p>If you see this message, JavaScript is enabled.</p>
    <p>If you don't see this message, JavaScript is likely disabled, and you will be redirected.</p>
</body>
</html>
```
