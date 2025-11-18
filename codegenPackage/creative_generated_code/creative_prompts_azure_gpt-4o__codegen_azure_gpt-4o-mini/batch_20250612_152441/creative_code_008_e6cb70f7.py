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
    <style>
        /* Style to inform users that JavaScript is required */
        .noscript-warning {
            display: none;
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <script>
        // Function to redirect users if JavaScript is enabled
        function redirectIfDisabled() {
            // Redirect to the error page if this function is executed
            window.location.href = 'error.html'; // Change 'error.html' to the actual error page URL
        }

        // Execute the redirection function if JavaScript is disabled
        window.onload = function() {
            redirectIfDisabled();
        };
    </script>
</head>
<body>
    <noscript>
        <!-- Message displayed to users with JavaScript disabled -->
        <div class="noscript-warning">
            JavaScript is disabled in your browser. Please enable it to access this page.
        </div>
    </noscript>

    <h1>Welcome to Our Website</h1>
    <p>This website requires JavaScript to function properly.</p>
</body>
</html>
```
