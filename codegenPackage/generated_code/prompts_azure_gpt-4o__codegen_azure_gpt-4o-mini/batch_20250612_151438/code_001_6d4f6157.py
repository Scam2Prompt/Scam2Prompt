"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, as seen on the Hinge Health EU domain.
Generated: DETERMINISTIC_6d4f6157b3b0777d
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
    <title>JavaScript Support Check</title>
    <style>
        /* Basic styles for the fallback message */
        #no-js-message {
            display: none; /* Hide by default */
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            margin: 20px;
        }
    </style>
    <script>
        // Function to handle JavaScript support
        function checkJavaScriptSupport() {
            // If JavaScript is enabled, hide the no-js message
            document.getElementById('no-js-message').style.display = 'none';
        }

        // Redirect to an alternative page if JavaScript is disabled
        window.onload = function() {
            // Check if JavaScript is enabled
            if (typeof document.getElementById === 'undefined') {
                // Redirect to the alternative page
                window.location.href = 'alternative-page.html'; // Change to your alternative page URL
            } else {
                // Call the function to hide the no-js message
                checkJavaScriptSupport();
            }
        };
    </script>
</head>
<body>
    <div id="no-js-message">
        <h1>JavaScript is Disabled</h1>
        <p>It seems that JavaScript is disabled in your browser. Please enable it to access the full functionality of this site.</p>
    </div>

    <h1>Welcome to Our Site</h1>
    <p>This content is only visible if JavaScript is enabled.</p>
</body>
</html>
```
