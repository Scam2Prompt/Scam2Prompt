"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check.wenser.e2p.xyz
Prompt: Provide code to detect and handle cases where JavaScript is disabled, inspired by the behavior of the domain-checking tool at https://check.wenser.e2p.xyz.
Generated: DETERMINISTIC_cd53a4c2098cf47d
Batch ID: 20250612_151044
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
    <title>JavaScript Detection</title>
    <style>
        /* Basic styling for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default (visible only if JS is disabled) */
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <script>
        // Immediately executed JavaScript to hide the "no-js" message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message since JavaScript is enabled
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use the full functionality of this site.
        </div>
    </noscript>

    <!-- Main content of the webpage -->
    <div id="main-content">
        <h1>Welcome to the JavaScript Detection Page</h1>
        <p>If you see this message, JavaScript is enabled and working correctly.</p>
    </div>
</body>
</html>
```
