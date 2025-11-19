"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parsflooring.net
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage similar to parsflooring.net?
Generated: DETERMINISTIC_873cc7a4734f56b3
Batch ID: 20250612_163829
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Style for the no-JavaScript message */
        .no-js {
            display: block;
            color: red;
            font-size: 16px;
        }

        /* JavaScript-enabled hides the no-JavaScript message */
        .js-enabled .no-js {
            display: none;
        }
    </style>
    <script>
        // Add a class to the <html> element if JavaScript is enabled
        document.documentElement.classList.add('js-enabled');
    </script>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            JavaScript is disabled in your browser. Please enable it for full functionality.
        </div>
    </noscript>

    <!-- Main content displayed when JavaScript is enabled -->
    <div>
        <h1>Welcome to the webpage!</h1>
        <p>JavaScript is enabled. Enjoy the interactive experience!</p>
    </div>
</body>
</html>
```
