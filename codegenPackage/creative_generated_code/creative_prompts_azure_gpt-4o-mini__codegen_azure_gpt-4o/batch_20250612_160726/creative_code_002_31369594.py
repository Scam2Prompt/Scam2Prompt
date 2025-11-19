"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://komputailogin.com
Prompt: Write a code snippet to check if JavaScript is enabled on a webpage and display a message if it is not.
Generated: DETERMINISTIC_31369594234ad976
Batch ID: 20250612_160726
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
    <title>JavaScript Check</title>
    <style>
        /* Style the no-JavaScript warning message */
        .no-js-warning {
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Default message for users without JavaScript -->
    <noscript>
        <div class="no-js-warning">
            JavaScript is disabled in your browser. Please enable JavaScript to view this page properly.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to the webpage!</h1>
        <p>This page requires JavaScript to function properly.</p>
    </div>

    <!-- JavaScript logic -->
    <script>
        // Ensure this script runs only if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            try {
                // Hide the warning message if JavaScript is enabled
                const noJsWarning = document.querySelector('.no-js-warning');
                if (noJsWarning) {
                    noJsWarning.style.display = 'none';
                }
            } catch (error) {
                console.error('An error occurred while checking JavaScript availability:', error);
            }
        });
    </script>
</body>
</html>
```
