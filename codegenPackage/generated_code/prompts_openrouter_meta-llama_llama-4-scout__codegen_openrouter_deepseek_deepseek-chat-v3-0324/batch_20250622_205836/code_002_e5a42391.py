"""
Generated Code Metadata:
========================
Original URL: https://beta-echodot.pages.dev
Prompt: Can you provide an example code snippet to create a simple webpage that requires JavaScript to display content, similar to how Echo Beta needs JavaScript to run?
Generated: DETERMINISTIC_e5a42391713df2ef
Batch ID: 20250622_205836
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
            text-align: center;
            padding: 50px;
            background-color: #f5f5f5;
        }
        .no-script {
            background-color: #ffebee;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .content {
            display: none;
            background-color: #e8f5e9;
            padding: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <noscript>
        <div class="no-script">
            <h2>JavaScript is Required</h2>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
        </div>
    </noscript>

    <!-- Main content that will be displayed when JavaScript is enabled -->
    <div id="main-content" class="content">
        <h1>Welcome to Our Website</h1>
        <p>This content is displayed because JavaScript is enabled in your browser.</p>
        <button id="interactive-btn">Click Me</button>
        <p id="response-text"></p>
    </div>

    <script>
        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Show the main content
            document.getElementById('main-content').style.display = 'block';
            
            // Add interactive functionality
            document.getElementById('interactive-btn').addEventListener('click', function() {
                document.getElementById('response-text').textContent = 'JavaScript is working!';
            });
        });
    </script>
</body>
</html>
```
