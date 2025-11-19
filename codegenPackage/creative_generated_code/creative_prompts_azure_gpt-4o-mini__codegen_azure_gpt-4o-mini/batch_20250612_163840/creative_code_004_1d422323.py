"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethzao.com
Prompt: How can I create a fallback message for users who have JavaScript disabled on my website?
Generated: DETERMINISTIC_1d422323bdd50a9e
Batch ID: 20250612_163840
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
    <title>Fallback Message Example</title>
    <style>
        /* Basic styles for the fallback message */
        .fallback-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <!-- Fallback message for users with JavaScript disabled -->
    <noscript>
        <div class="fallback-message">
            <strong>Notice:</strong> It seems JavaScript is disabled in your browser. 
            For the best experience on this site, please enable JavaScript or upgrade to a modern browser.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to Our Website!</h1>
        <p>This is where the main content goes. Enjoy your stay!</p>
    </div>

    <script>
        // JavaScript code for dynamic content can go here
        // Example: Show a greeting after checking if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            console.log("JavaScript is enabled.");
            // Additional dynamic functionalities can be added here
        });
    </script>
    
</body>
</html>
```
