"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cqzh5.com
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a mobile web environment?
Generated: DETERMINISTIC_ae9c1b347ebe5a19
Batch ID: 20250612_161041
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
        /* Shows a message if JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            text-align: center;
            font-size: 18px;
            margin-top: 20px;
        }
    </style>
    <noscript>
        <!-- Fallback message if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block;
            }
        </style>
        <div class="no-js-message">
            JavaScript is disabled or not supported in your browser. Please enable JavaScript for the best experience.
        </div>
    </noscript>
</head>
<body>
    <h1>Welcome to the Mobile Web App</h1>

    <!-- Content that requires JavaScript -->
    <script>
        // This script ensures dynamic behavior only when JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            const message = document.createElement("p");
            message.textContent = "JavaScript is enabled in your browser.";
            message.style.color = "green";
            message.style.fontSize = "18px";
            message.style.textAlign = "center";
            document.body.appendChild(message);
        });
    </script>
</body>
</html>
```
