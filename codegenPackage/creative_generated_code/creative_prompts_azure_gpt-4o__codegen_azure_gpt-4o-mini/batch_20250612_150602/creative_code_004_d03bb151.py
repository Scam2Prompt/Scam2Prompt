"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: Write code to dynamically display a message on a webpage if JavaScript is disabled, inspired by the BONKBOXES whitelist page functionality.
Generated: DETERMINISTIC_d03bb151bf5a0031
Batch ID: 20250612_150602
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
        /* Style for the message displayed when JavaScript is disabled */
        .js-disabled-message {
            display: none; /* Hidden by default */
            background-color: #ffcccb; /* Light red background */
            color: #d8000c; /* Dark red text color */
            padding: 20px;
            border: 1px solid #d8000c;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <div class="js-disabled-message" id="js-disabled-message">
        JavaScript is disabled in your browser. Please enable it to see the full functionality of this webpage.
    </div>

    <noscript>
        <!-- Fallback content to display if JavaScript is disabled -->
        <style>
            /* Ensure fallback message is visible when JavaScript is disabled */
            .js-disabled-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

    <script>
        // JavaScript code can be placed here to enhance functionality
        // This script can also handle various interactive features on the page
        document.addEventListener("DOMContentLoaded", function() {
            // Your JavaScript functionality goes here
            // For example, dynamically loading content, handling events, etc.
        });
    </script>
</body>
</html>
```
