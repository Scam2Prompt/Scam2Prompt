"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: Generate a script that checks if JavaScript is enabled in a user's browser before loading content.
Generated: DETERMINISTIC_c59ccfd9acd71562
Batch ID: 20250612_163231
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
        /* Hide the content by default */
        .content {
            display: none;
        }
        
        /* Show the JavaScript disabled message if needed */
        .no-js-message {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="js-disabled" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to view the content.
    </div>

    <div id="content" class="content">
        <h1>Welcome to Our Website!</h1>
        <p>This content is only visible when JavaScript is enabled.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function enableContent() {
            // Hide the JavaScript disabled message
            const jsDisabledMessage = document.getElementById('js-disabled');
            if (jsDisabledMessage) {
                jsDisabledMessage.style.display = 'none';
            }

            // Show the main content
            const content = document.getElementById('content');
            if (content) {
                content.style.display = 'block';
            }
        }

        // Execute the function to enable content if JavaScript is enabled
        enableContent();
    </script>
</body>
</html>
```
