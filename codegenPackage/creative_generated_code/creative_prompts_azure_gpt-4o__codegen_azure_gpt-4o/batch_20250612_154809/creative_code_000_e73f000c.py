"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the behavior described on coinbase.co.za.
Generated: DETERMINISTIC_e73f000cf34e9737
Batch ID: 20250612_154809
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
    <title>JavaScript Disabled Detection</title>
    <style>
        /* Default message styling */
        #js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Placeholder for the JavaScript-disabled message -->
    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable JavaScript to fully access this website.
        </div>
    </noscript>

    <script>
        // Error handling for older browsers or unexpected issues
        try {
            // Ensure no message is displayed if JavaScript is enabled
            window.onload = function () {
                const message = document.getElementById('js-disabled-message');
                if (message) {
                    message.style.display = 'none'; // Hide the message
                }
            };
        } catch (error) {
            console.error('An error occurred while detecting JavaScript support:', error);
        }
    </script>
</body>
</html>
```
