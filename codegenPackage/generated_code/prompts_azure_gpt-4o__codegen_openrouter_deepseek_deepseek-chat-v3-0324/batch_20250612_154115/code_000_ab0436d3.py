"""
Generated Code Metadata:
========================
Original URL: https://monada.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message.
Generated: DETERMINISTIC_ab0436d31d9d639c
Batch ID: 20250612_154115
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
    <title>JavaScript Detection</title>
    <noscript>
        <style>
            .no-script-message {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                padding: 20px;
                background-color: #ff4444;
                color: white;
                text-align: center;
                z-index: 9999;
                font-family: Arial, sans-serif;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Content that requires JavaScript -->
    <div id="app">
        <!-- Your JavaScript-dependent content goes here -->
    </div>

    <noscript>
        <div class="no-script-message">
            <h2>JavaScript is Disabled</h2>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
        </div>
    </noscript>

    <script>
        // Remove noscript message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const noscriptElements = document.getElementsByTagName('noscript');
            while (noscriptElements.length > 0) {
                noscriptElements[0].parentNode.removeChild(noscriptElements[0]);
            }
            
            // Additional JavaScript functionality can be added here
            console.log('JavaScript is enabled');
        });
    </script>
</body>
</html>
```
