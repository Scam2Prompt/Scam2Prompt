"""
Generated Code Metadata:
========================
Original URL: https://sparkfi-sparkfi.net
Prompt: Generate a script that checks if JavaScript is enabled in a user's browser before loading content.
Generated: DETERMINISTIC_c59ccfd9acd71562
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <style>
        .no-js-message {
            padding: 20px;
            background-color: #ffecec;
            border: 1px solid #f5aca6;
            color: #800000;
            text-align: center;
            margin: 20px;
        }
        
        .js-content {
            display: none;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">
            <h1>JavaScript is Disabled</h1>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
        </div>
    </noscript>

    <div id="js-content" class="js-content">
        <!-- Your JavaScript-dependent content goes here -->
        <h1>Welcome to our website!</h1>
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // Immediately show content if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            try {
                var jsContent = document.getElementById('js-content');
                if (jsContent) {
                    jsContent.style.display = 'block';
                }
                
                // Additional JavaScript initialization can go here
                console.log('JavaScript is enabled - loading full content');
            } catch (error) {
                console.error('Error in JavaScript detection:', error);
                // Fallback behavior if there's an error
                var noScriptElements = document.getElementsByTagName('noscript');
                if (noScriptElements.length > 0) {
                    noScriptElements[0].style.display = 'block';
                }
            }
        });
    </script>
</body>
</html>
```
