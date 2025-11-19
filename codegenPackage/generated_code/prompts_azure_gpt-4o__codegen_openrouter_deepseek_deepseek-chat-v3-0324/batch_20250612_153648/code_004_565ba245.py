"""
Generated Code Metadata:
========================
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Develop a simple JavaScript application that checks if JavaScript is enabled and displays a message similar to "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_565ba245807f5efc
Batch ID: 20250612_153648
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
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .message {
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <noscript>
        <div class="message">
            <h1>JavaScript is Disabled</h1>
            <p>You need to enable JavaScript to run this app.</p>
        </div>
    </noscript>

    <!-- Content shown when JavaScript is enabled -->
    <div id="app-content" class="hidden">
        <div class="message">
            <h1>Welcome to the App</h1>
            <p>JavaScript is enabled and working!</p>
        </div>
    </div>

    <script>
        // Check if JavaScript is enabled and show appropriate content
        document.addEventListener('DOMContentLoaded', function() {
            const appContent = document.getElementById('app-content');
            if (appContent) {
                appContent.classList.remove('hidden');
            }
        });
    </script>
</body>
</html>
```
