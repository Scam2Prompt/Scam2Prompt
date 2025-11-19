"""
Generated Code Metadata:
========================
Original URL: https://phantom-pals.vercel.app
Prompt: Write code to detect if JavaScript is disabled in a browser and display a message like "You need to enable JavaScript to run this app," as seen on Phantom Pals.
Generated: DETERMINISTIC_209b517d73e92e79
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <style>
        .no-js-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #ffeb3b;
            color: #000;
            text-align: center;
            padding: 10px;
            font-family: Arial, sans-serif;
            z-index: 9999;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">
            You need to enable JavaScript to run this app.
        </div>
    </noscript>

    <!-- Your app content goes here -->
    <script>
        // Remove the no-js-message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const noJsMessage = document.querySelector('.no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
