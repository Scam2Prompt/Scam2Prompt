"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: What are the best practices for ensuring JavaScript is enabled for web applications like Ignitus?
Generated: DETERMINISTIC_20658a64b8f77728
Batch ID: 20250612_163408
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style for the message to show when JS is disabled */
        .no-js-message {
            display: none;
            background-color: #ffcc00;
            color: #333;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }
        /* Show this when JavaScript is enabled */
        .js-enabled {
            display: block;
        }
    </style>
</head>
<body>

    <div id="no-js-warning" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <div id="content" class="js-enabled">
        <h1>Welcome to Ignitus</h1>
        <p>JavaScript is enabled. Enjoy our interactive features!</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Show the warning message if JS is disabled
            const noJsWarning = document.getElementById('no-js-warning');
            const content = document.getElementById('content');

            // Hide the warning and show the content if JS is enabled
            if (noJsWarning && content) {
                noJsWarning.style.display = 'none'; // Hide the warning
                content.style.display = 'block'; // Show the content
            } else {
                console.error("Element selection failed. Ensure the IDs are correct.");
            }
        }

        // Run the check on page load
        window.onload = checkJavaScriptEnabled;
    </script>
</body>
</html>
```
