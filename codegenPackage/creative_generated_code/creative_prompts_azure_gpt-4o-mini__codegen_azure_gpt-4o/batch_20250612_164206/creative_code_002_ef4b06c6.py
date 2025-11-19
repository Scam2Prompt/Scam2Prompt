"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbpiaccess.jzta.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser for lbpiaccess.jzta.com?
Generated: DETERMINISTIC_ef4b06c60799f115
Batch ID: 20250612_164206
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-size: 18px;
        }
    </style>
    <script>
        // When JavaScript is enabled, hide the "no-js-message" element
        document.addEventListener("DOMContentLoaded", function () {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed to users when JavaScript is disabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to access lbpiaccess.jzta.com.
        </div>
    </noscript>

    <!-- Content that requires JavaScript -->
    <div>
        <h1>Welcome to lbpiaccess.jzta.com</h1>
        <p>If you are seeing this, JavaScript is enabled in your browser.</p>
    </div>
</body>
</html>
```
