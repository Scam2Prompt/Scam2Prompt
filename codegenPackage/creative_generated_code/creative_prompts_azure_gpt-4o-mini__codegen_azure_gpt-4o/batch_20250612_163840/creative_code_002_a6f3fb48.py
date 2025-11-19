"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovkean.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage?
Generated: DETERMINISTIC_a6f3fb48fa9e0192
Batch ID: 20250612_163840
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
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* The message is hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <noscript>
        <!-- The <noscript> tag displays content when JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <!-- This message will be displayed if JavaScript is disabled -->
    <div class="no-js-message">
        JavaScript is disabled. Please enable JavaScript to use this webpage.
    </div>

    <script>
        // JavaScript is enabled, so ensure the "no-js-message" element remains hidden
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.querySelector('.no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
