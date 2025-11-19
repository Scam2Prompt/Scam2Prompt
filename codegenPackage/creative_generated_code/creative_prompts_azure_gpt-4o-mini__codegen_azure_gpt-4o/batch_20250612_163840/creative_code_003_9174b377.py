"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Provide an example of how to create a fallback message for users who have JavaScript disabled on their mobile devices.
Generated: DETERMINISTIC_9174b3771418252d
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
            text-align: center;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <div class="no-js-message">
        It seems that JavaScript is disabled on your device. Please enable JavaScript for the best experience on this website.
    </div>

    <script>
        // Hide the fallback message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            const fallbackMessage = document.querySelector('.no-js-message');
            if (fallbackMessage) {
                fallbackMessage.style.display = 'none'; // Ensure it is hidden when JS is enabled
            }
        });
    </script>
    
    <!-- No-JavaScript fallback -->
    <noscript>
        <style>
            .no-js-message {
                display: block; /* Display the message for no-JS users */
            }
        </style>
    </noscript>
</body>
</html>
```
