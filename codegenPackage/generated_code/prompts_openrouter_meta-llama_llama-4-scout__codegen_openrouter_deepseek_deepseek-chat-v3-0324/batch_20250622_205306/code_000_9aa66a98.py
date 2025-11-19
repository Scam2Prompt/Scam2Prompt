"""
Generated Code Metadata:
========================
Original URL: https://huijiatw.com
Prompt: Write a JavaScript-enabled webpage that displays a "Please enable JavaScript to continue" message when JavaScript is disabled.
Generated: DETERMINISTIC_9aa66a985f003ce2
Batch ID: 20250622_205306
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
            color: #333;
        }
        .js-disabled {
            background-color: #ffebee;
            padding: 20px;
            border-radius: 5px;
            max-width: 600px;
            margin: 0 auto;
            border: 1px solid #ffcdd2;
        }
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="js-disabled">
            <h1>JavaScript Required</h1>
            <p>Please enable JavaScript to continue using this website.</p>
            <p>This site relies on JavaScript for core functionality.</p>
        </div>
    </noscript>

    <div class="js-enabled">
        <!-- Your normal page content goes here -->
        <h1>Welcome to our website</h1>
        <p>JavaScript is enabled. Enjoy your experience!</p>
    </div>

    <script>
        // Hide the noscript message and show normal content when JS is enabled
        document.addEventListener('DOMContentLoaded', function() {
            var jsEnabledElements = document.querySelectorAll('.js-enabled');
            jsEnabledElements.forEach(function(element) {
                element.style.display = 'block';
            });
        });
    </script>
</body>
</html>
```
