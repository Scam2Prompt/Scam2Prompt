"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, inspired by the Step App's functionality.
Generated: DETERMINISTIC_b22c7d393d61436a
Batch ID: 20250612_154306
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
        /* Basic styles for the fallback message */
        #no-js-message {
            display: none; /* Hide by default */
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
    <noscript>
        <style>
            /* Display the message if JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>
    <script>
        // Function to check JavaScript support
        function checkJavaScriptSupport() {
            // Logic to redirect if JavaScript is disabled
            if (typeof window !== 'undefined') {
                // Everything is fine; JavaScript is supported
                console.log("JavaScript is supported.");
            } else {
                // Redirect to an alternative page if JavaScript is not supported
                window.location.href = "alternative-page.html"; // Change this to your desired URL
            }
        }

        // Call the function on window load
        window.onload = checkJavaScriptSupport;
    </script>
</head>
<body>
    <div id="no-js-message">
        <h2>JavaScript Disabled</h2>
        <p>It seems that JavaScript is disabled in your browser. Please enable it or use a browser that supports JavaScript to access this site.</p>
    </div>

    <h1>Welcome to the Main Page</h1>
    <p>This is the main content that requires JavaScript to function properly.</p>
</body>
</html>
```
