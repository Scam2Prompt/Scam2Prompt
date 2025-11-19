"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialmelaniatrump.me
Prompt: Generate code for a fallback message that appears when JavaScript is not enabled, based on the approach used on the Melania Trump website.
Generated: DETERMINISTIC_86122597a1932e9a
Batch ID: 20250612_155959
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Style the fallback message */
        .no-js-message {
            display: none; /* Default is hidden */
            color: #ff0000;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            border: 2px solid #ff0000;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Content for users with JavaScript -->
    <div id="main-content">
        <h1>Welcome to Our Website</h1>
        <p>This site is best experienced with JavaScript enabled.</p>
    </div>

    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <div class="no-js-message">
            JavaScript is not enabled in your browser. Please enable JavaScript to view this website properly.
        </div>
    </noscript>

    <script>
        // Ensure no-js-message remains hidden if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.querySelector('.no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = "none"; // Hide fallback message explicitly
            }
        });
    </script>
</body>
</html>
```
