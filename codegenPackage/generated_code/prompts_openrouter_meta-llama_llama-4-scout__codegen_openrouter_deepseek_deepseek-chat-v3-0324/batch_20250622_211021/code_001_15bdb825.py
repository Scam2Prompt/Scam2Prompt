"""
Generated Code Metadata:
========================
Original URL: https://aussbitte.com
Prompt: Write a basic HTML page that checks if JavaScript is enabled in the browser and displays a different message based on its status.
Generated: DETERMINISTIC_15bdb8255187c29f
Batch ID: 20250622_211021
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
    <title>JavaScript Status Check</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            line-height: 1.6;
        }
        .message {
            padding: 20px;
            border-radius: 5px;
            max-width: 600px;
            margin: 0 auto;
        }
        .enabled {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .disabled {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
    </style>
    <noscript>
        <style>
            #js-enabled { display: none; }
        </style>
    </noscript>
</head>
<body>
    <div id="js-enabled" class="message enabled">
        JavaScript is enabled in your browser.
    </div>
    <noscript>
        <div class="message disabled">
            JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
        </div>
    </noscript>

    <script>
        // This script will only run if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            console.log('JavaScript is enabled and working correctly.');
        });
    </script>
</body>
</html>
```
