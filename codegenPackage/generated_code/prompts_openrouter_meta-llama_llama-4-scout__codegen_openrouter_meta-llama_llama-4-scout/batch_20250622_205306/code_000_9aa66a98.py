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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style the noscript element to display the message prominently */
        noscript {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <h1>Please enable JavaScript to continue</h1>
        <p>Your browser has JavaScript disabled. Please enable it to access this page.</p>
    </noscript>
    <script>
        // Check if JavaScript is enabled by adding a dynamic element to the page
        document.addEventListener('DOMContentLoaded', function() {
            const jsEnabledElement = document.createElement('p');
            jsEnabledElement.id = 'js-enabled';
            jsEnabledElement.textContent = 'JavaScript is enabled on this page.';
            document.body.appendChild(jsEnabledElement);
        });
    </script>
</body>
</html>
```
