"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Write code to display a fallback message for users accessing a webpage without JavaScript enabled, specifically targeting mobile browsers.
Generated: DETERMINISTIC_23db963321805bfe
Batch ID: 20250612_145619
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
    <title>JavaScript Fallback</title>
    <style>
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Default state: hidden */
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background-color: #ffcccb;
            color: #333;
            border: 1px solid #ff0000;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
    <noscript>
        <!-- Fallback content rendered only when JavaScript is disabled -->
        <style>
            /* Show fallback message when JavaScript is disabled */
            .no-js-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        It looks like JavaScript is disabled in your browser. For the best experience, please enable JavaScript.
    </div>

    <script>
        // JavaScript can dynamically hide the message (defensive measure)
        document.addEventListener("DOMContentLoaded", () => {
            const fallbackMessage = document.querySelector('.no-js-message');
            if (fallbackMessage) {
                fallbackMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
