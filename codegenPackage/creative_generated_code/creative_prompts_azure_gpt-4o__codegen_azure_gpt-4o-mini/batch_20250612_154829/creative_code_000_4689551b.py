"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it.
Generated: DETERMINISTIC_4689551b0f3bb70f
Batch ID: 20250612_154829
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
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript to improve your experience on this site.
    </div>

    <script>
        // This script will run only if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Hide the no-JS message if JavaScript is enabled
            var noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>

    <noscript>
        <!-- This block will only render if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message when JS is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
