"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yepbit1.com
Prompt: How do I write a script that prompts users to enable JavaScript for better functionality on ex_web?
Generated: DETERMINISTIC_c9ec5be3ad490543
Batch ID: 20250612_155242
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
    <title>Enable JavaScript Notification</title>
    <style>
        /* Hidden by default, visible when JavaScript is disabled */
        .no-js-message {
            display: none;
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            margin: 20px 0;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <!-- Content inside <noscript> will display if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled on your browser. For better functionality, please enable JavaScript.
    </div>

    <!-- This script hides the message when JavaScript is enabled -->
    <script>
        try {
            // Attempt to hide the no-js message
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        } catch (error) {
            // Log errors to the console for debugging
            console.error('An error occurred while hiding the no-js message:', error);
        }
    </script>
</body>
</html>
```
