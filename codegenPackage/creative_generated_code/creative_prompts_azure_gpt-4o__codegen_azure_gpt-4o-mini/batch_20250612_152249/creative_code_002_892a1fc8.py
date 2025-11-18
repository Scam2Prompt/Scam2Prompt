"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mybonkbox.web.app
Prompt: Generate a basic HTML and JavaScript template for a web app that displays a "JavaScript is required" message if JavaScript is disabled.
Generated: DETERMINISTIC_892a1fc8ad8e585e
Batch ID: 20250612_152249
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
    <title>JavaScript Required Example</title>
    <style>
        /* Basic styling for the message */
        #no-js-message {
            display: none; /* Hide the message by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div id="no-js-message">
            JavaScript is required to view this content. Please enable JavaScript in your browser settings.
        </div>
    </noscript>

    <div id="content">
        <h1>Welcome to Our Web App</h1>
        <p>This app requires JavaScript to function properly.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // This function runs once the DOM is fully loaded
            console.log('JavaScript is enabled.'); // Log message for debugging

            // Your app logic can go here
        });
    </script>
</body>
</html>
```
