"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a user's browser and display a message prompting them to enable it if it is disabled.
Generated: DETERMINISTIC_b2ec5b13b0870605
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* This message will only show if JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden if JavaScript is enabled */
        }
    </style>
    <noscript>
        <style>
            /* Overwrite display property when JavaScript is disabled */
            .no-js-message {
                display: block; /* Visible only if JavaScript is disabled */
                color: red;
                font-size: 18px;
                margin-top: 20px;
                text-align: center;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site properly.
    </div>

    <script>
        // This script ensures the no-js message is hidden if JavaScript is enabled

        // Find the message element
        const noJsMessage = document.querySelector('.no-js-message');

        // Hide the message (should already be hidden via CSS, but ensure it programmatically)
        if (noJsMessage) {
            noJsMessage.style.display = 'none';
        }

        // Optionally, you can add a message for JavaScript-enabled users
        console.log('JavaScript is enabled in the browser.'); // For debugging or analytics
    </script>
</body>
</html>
```
