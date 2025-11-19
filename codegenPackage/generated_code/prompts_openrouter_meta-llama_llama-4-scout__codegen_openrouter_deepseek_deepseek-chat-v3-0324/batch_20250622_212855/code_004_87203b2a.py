"""
Generated Code Metadata:
========================
Original URL: https://teslax.in
Prompt: Create a simple webpage using HTML, CSS, and JavaScript that displays a message when JavaScript is disabled, similar to the message seen on teslax.in.
Generated: DETERMINISTIC_87203b2a5a76dc57
Batch ID: 20250622_212855
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
    <title>JavaScript Required</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        
        .container {
            max-width: 600px;
            padding: 2rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: #e74c3c;
            margin-bottom: 1rem;
        }
        
        p {
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }
        
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="container">
            <h1>JavaScript is Disabled</h1>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
            <p>If you need assistance enabling JavaScript, please refer to your browser's help documentation.</p>
        </div>
    </noscript>

    <div id="main-content" class="hidden">
        <!-- Your main website content goes here -->
        <div class="container">
            <h1>Welcome to Our Website</h1>
            <p>This is the main content of your website that requires JavaScript.</p>
        </div>
    </div>

    <script>
        // Show main content when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            var mainContent = document.getElementById('main-content');
            mainContent.classList.remove('hidden');
        });
    </script>
</body>
</html>
```
