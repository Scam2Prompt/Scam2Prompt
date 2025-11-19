"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_3e97df1a94519038
Batch ID: 20250612_160220
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
        /* Styles for the message displayed when JS is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <div id="content">
        <p>Welcome to our web application!</p>
    </div>

    <script>
        // Function to handle JavaScript enabled scenario
        function initApp() {
            // Your application initialization code goes here
            console.log('JavaScript is enabled. Application is ready to use.');
            // More logic can be added here as necessary
        }

        // Ensuring the DOM is fully loaded before executing scripts
        document.addEventListener('DOMContentLoaded', function() {
            // Call the function to initialize the app
            initApp();
        });
    </script>

</body>
</html>
```
