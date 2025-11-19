"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrop.net
Prompt: How do I check if JavaScript is enabled in my browser for accessing Basedrop?
Generated: DETERMINISTIC_e4bb5fecd5431a11
Batch ID: 20250612_135839
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* If JavaScript is disabled, this message will be visible */
        #no-js-message {
            display: block;
            color: red;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }

        /* If JavaScript is enabled, hide this message */
        .js-enabled #no-js-message {
            display: none;
        }
    </style>
    <script>
        // If JavaScript is enabled, add a specific class to the <html> element
        document.documentElement.classList.add('js-enabled');
    </script>
</head>
<body>
    <noscript>
        <!-- Fallback message if JavaScript is disabled -->
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to access Basedrop.
        </div>
    </noscript>

    <!-- Page content -->
    <div id="content">
        <h1>Welcome to Basedrop</h1>
        <p>JavaScript is enabled in your browser. Enjoy your experience!</p>
    </div>
</body>
</html>
```
