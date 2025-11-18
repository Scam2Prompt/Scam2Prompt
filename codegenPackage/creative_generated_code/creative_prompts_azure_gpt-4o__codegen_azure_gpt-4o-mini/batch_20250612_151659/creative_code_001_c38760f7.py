"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flippingclub.xyz
Prompt: Create a JavaScript function that checks for JavaScript compatibility and redirects users to an error page if JavaScript is disabled, as described on flippingclub.xyz.
Generated: DETERMINISTIC_c38760f7ebe87883
Batch ID: 20250612_151659
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
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // If JavaScript is enabled, set a flag in session storage
            sessionStorage.setItem('jsEnabled', 'true');
        }

        // Redirects to the error page if JavaScript is disabled
        function redirectIfJSDisabled() {
            // Check if the 'jsEnabled' flag is set in session storage
            if (!sessionStorage.getItem('jsEnabled')) {
                // Redirect the user to the error page
                window.location.href = 'error.html'; // Change this to the actual error page URL
            }
        }

        // Call the checkJavaScript function on page load
        window.onload = function() {
            checkJavaScript();
        };
        
        // Call the redirect function on page load
        window.onload = function() {
            redirectIfJSDisabled();
        };
    </script>
</head>
<body>
    <noscript>
        <!-- Notify users that JavaScript is disabled -->
        <meta http-equiv="refresh" content="0; url=error.html">
        <div style="display: none;">
            You are being redirected to an error page because JavaScript is disabled in your browser.
        </div>
    </noscript>
    <h1>Welcome to the site!</h1>
    <p>This site works best with JavaScript enabled.</p>
</body>
</html>
```
