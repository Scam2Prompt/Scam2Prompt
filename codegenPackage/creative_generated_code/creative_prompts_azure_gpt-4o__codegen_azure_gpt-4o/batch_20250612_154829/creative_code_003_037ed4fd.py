"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: Provide code to dynamically display a warning message when JavaScript is disabled, ensuring compatibility across major browsers.
Generated: DETERMINISTIC_037ed4fd43cb8fd1
Batch ID: 20250612_154829
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the warning message */
        .js-warning {
            display: none; /* Hidden by default, visible only when JavaScript is disabled */
            color: white;
            background-color: red;
            padding: 10px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            border: 1px solid darkred;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 9999;
        }
    </style>
</head>
<body>
    <!-- Warning message to show when JavaScript is disabled -->
    <noscript>
        <!-- The <noscript> tag ensures this is shown when JavaScript is disabled -->
        <div class="js-warning">
            Warning: JavaScript is disabled in your browser. Please enable it for better functionality.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <h1>Welcome to My Website</h1>
    <p>This is a sample webpage.</p>

    <!-- JavaScript to hide the noscript tag content when JavaScript is enabled -->
    <script>
        // Ensure compatibility across major browsers
        document.addEventListener('DOMContentLoaded', function () {
            // Hide any elements meant for no-JS warnings
            const warnings = document.querySelectorAll('.js-warning');
            warnings.forEach(warning => {
                warning.style.display = 'none'; // Ensure warnings remain hidden if JavaScript is enabled
            });
        });
    </script>
</body>
</html>
```
