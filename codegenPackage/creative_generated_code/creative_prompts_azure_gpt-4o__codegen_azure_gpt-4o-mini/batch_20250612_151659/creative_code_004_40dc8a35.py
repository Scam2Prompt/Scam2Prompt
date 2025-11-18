"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokensea-dapp.pages.dev
Prompt: Write code to detect if JavaScript is disabled in the browser and display a message like "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_40dc8a35eba92f51
Batch ID: 20250612_151659
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;   /* Red color for visibility */
            font-weight: bold;
            margin: 20px;
        }
    </style>
    <noscript>
        <!-- This message will be displayed if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        You need to enable JavaScript to run this app.
    </div>

    <script>
        // This script is for normal execution when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Additional code can go here
            console.log("JavaScript is enabled."); // Log confirmation
        });
    </script>
</body>
</html>
```
