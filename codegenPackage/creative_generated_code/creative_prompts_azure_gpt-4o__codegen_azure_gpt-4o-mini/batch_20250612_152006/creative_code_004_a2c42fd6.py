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
    <title>JavaScript Redirect Example</title>
    <script>
        // Function to redirect users if JavaScript is enabled
        function redirectToErrorPage() {
            window.location.href = '/error-page.html'; // URL of the error page
        }
        
        // Call the redirect function on page load
        window.onload = redirectToErrorPage;
    </script>
</head>
<body>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/error-page.html" />
        <!-- Inform the user that JavaScript is required -->
        <div style="text-align: center; margin-top: 20%;">
            <h1>JavaScript Disabled</h1>
            <p>It seems that JavaScript is disabled in your browser. Please enable JavaScript to access this page.</p>
        </div>
    </noscript>
    
    <h1>Welcome to the JavaScript Required Page</h1>
    <p>This content is only visible if JavaScript is enabled.</p>
</body>
</html>
```
