"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to display a warning message when JavaScript is disabled, styled using CSS, for a webpage like coinbase.co.za.
Generated: DETERMINISTIC_719882dc3584a025
Batch ID: 20250612_154809
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
    <title>Coinbase Warning</title>
    <style>
        /* Style for the warning message */
        #js-warning {
            display: none; /* Initially hidden, shown when no JavaScript */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px 0;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Warning message container -->
    <div id="js-warning">
        Warning: JavaScript is disabled in your browser. Please enable JavaScript to use this website properly.
    </div>

    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <style>
            #js-warning {
                display: block; /* Makes the warning visible when JavaScript is disabled */
            }
        </style>
    </noscript>

    <script>
        // JavaScript code to ensure the warning is hidden when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            const jsWarning = document.getElementById('js-warning');
            if (jsWarning) {
                // Hide warning when JavaScript is properly enabled
                jsWarning.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
