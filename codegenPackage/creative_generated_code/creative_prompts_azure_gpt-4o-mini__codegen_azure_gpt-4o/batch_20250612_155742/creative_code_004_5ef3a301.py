"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbo.com
Prompt: How do I create a fallback message for users who have JavaScript disabled on their mobile devices?
Generated: DETERMINISTIC_5ef3a301d638dfb0
Batch ID: 20250612_155742
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
    <title>JavaScript Disabled Fallback</title>
    <style>
        /* Style for the fallback message */
        .no-js-message {
            display: none;
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Fallback message for users with JavaScript disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled on your browser. Please enable JavaScript for a better experience.
    </div>

    <!-- Content for users who have JavaScript enabled -->
    <div id="js-content" style="text-align: center;">
        <h1>Welcome to Our Website!</h1>
        <p>Enjoy all the features we have to offer.</p>
    </div>

    <script>
        // JavaScript to hide the fallback message if JavaScript is enabled
        document.getElementById('no-js-message').style.display = 'none';
    </script>
    <noscript>
        <!-- Ensures fallback message is visible for users with JavaScript disabled -->
        <style>
            #no-js-message {
                display: block !important;
            }
            #js-content {
                display: none;
            }
        </style>
    </noscript>
</body>
</html>
```
