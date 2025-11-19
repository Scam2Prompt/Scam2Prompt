"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Generate code for a landing page that displays a "JavaScript required" message when JavaScript is disabled, as seen on the Step App domain page.
Generated: DETERMINISTIC_1850fc366c57a499
Batch ID: 20250612_154306
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
    <title>Landing Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            color: #333;
        }
        
        .container {
            text-align: center;
            max-width: 600px;
            padding: 20px;
        }
        
        .js-disabled-message {
            display: none;
            background-color: #fff;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .js-disabled-message h1 {
            color: #e74c3c;
            margin-bottom: 20px;
        }
        
        .js-disabled-message p {
            margin-bottom: 20px;
            line-height: 1.6;
        }
        
        .content {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- This div will be shown when JavaScript is disabled -->
        <noscript>
            <div class="js-disabled-message">
                <h1>JavaScript is required</h1>
                <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
                <p>If you need assistance enabling JavaScript, please refer to your browser's help documentation.</p>
            </div>
        </noscript>
        
        <!-- Main content that will be hidden when JavaScript is disabled -->
        <div class="content" id="main-content">
            <!-- Your landing page content goes here -->
            <h1>Welcome to Our Website</h1>
            <p>This is the main content of your landing page.</p>
        </div>
    </div>

    <script>
        // Hide the main content if JavaScript is disabled (fallback)
        document.getElementById('main-content').style.display = 'none';
        
        // When JavaScript is enabled, show the main content and hide the noscript message
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('main-content').style.display = 'block';
            
            // Optional: You can also remove the noscript content if desired
            var noscriptElements = document.getElementsByTagName('noscript');
            for (var i = 0; i < noscriptElements.length; i++) {
                noscriptElements[i].style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
