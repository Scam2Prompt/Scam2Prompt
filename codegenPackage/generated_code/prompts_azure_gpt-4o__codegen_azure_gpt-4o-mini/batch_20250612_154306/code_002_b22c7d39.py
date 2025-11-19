"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, inspired by the Step App's functionality.
Generated: DETERMINISTIC_b22c7d393d61436a
Batch ID: 20250612_154306
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
    <title>JavaScript Support Check</title>
    <style>
        /* Basic styles for the fallback message */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript or use a different browser to access this site.
    </div>

    <script>
        // Function to redirect users if JavaScript is disabled
        function checkJavaScriptSupport() {
            // Redirect to an alternative page
            window.location.href = "alternative-page.html"; // Change to your alternative page URL
        }

        // If JavaScript is enabled, we can hide the no-JS message
        document.getElementById('no-js-message').style.display = 'none';

        // If JavaScript is disabled, the following code will not run
        // Therefore, we set a timeout to redirect after a short delay
        setTimeout(checkJavaScriptSupport, 1000); // 1 second delay before redirecting
    </script>

    <noscript>
        <!-- This block will only be executed if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
