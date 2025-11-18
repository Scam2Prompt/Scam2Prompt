"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Write a JavaScript function that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, similar to the behavior on mtec.cyou.
Generated: DETERMINISTIC_4e776f9f676560b2
Batch ID: 20250612_150446
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
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptSupport() {
            // If this function is executed, JavaScript is enabled
            // Redirect to the main content or home page if needed
            window.location.href = 'mainContent.html'; // Change to your actual main page
        }

        // Function to handle redirection in case JavaScript is disabled
        function redirectToErrorPage() {
            // Redirect users to an error page indicating JavaScript is required
            window.location.href = 'error.html'; // Change to your actual error page
        }

        // Call the check function on page load
        window.onload = function() {
            checkJavaScriptSupport();
        };
    </script>
</head>
<body>
    <noscript>
        <!-- This block will only be displayed if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0; URL='error.html'"> <!-- Change to your actual error page -->
        <p>JavaScript is disabled in your browser. Please enable it to use this site.</p>
    </noscript>
    <h1>Welcome to Our Site</h1>
    <p>This content is only visible if JavaScript is enabled.</p>
</body>
</html>
```
