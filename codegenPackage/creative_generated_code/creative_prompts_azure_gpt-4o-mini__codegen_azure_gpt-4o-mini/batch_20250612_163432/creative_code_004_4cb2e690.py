"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potexclusiveofficialsite.online
Prompt: How do I create a fallback message for users without JavaScript enabled?
Generated: DETERMINISTIC_4cb2e690613e8bd4
Batch ID: 20250612_163432
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
        /* Basic styling for fallback message */
        .fallback-message {
            display: none; /* Hidden by default */
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px 0;
        }
    </style>
</head>
<body>

    <div id="content">
        <h1>Welcome to Our Website!</h1>
        <p>This content requires JavaScript to function correctly.</p>
    </div>

    <noscript>
        <div class="fallback-message" id="fallback-message">
            Your browser does not support JavaScript or it is disabled. Please enable JavaScript for a better experience.
        </div>
    </noscript>

    <script>
        // This script will execute if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // You can add interactive features here
            console.log('JavaScript is enabled.'); // For debugging purposes
        });
    </script>

</body>
</html>
```
