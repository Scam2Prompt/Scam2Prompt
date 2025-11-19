"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link.sv
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_162510
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
        /* Styles to hide the message if JavaScript is enabled */
        .no-js {
            display: block;
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
        }

        .js {
            display: none; /* Hidden when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js">
        JavaScript is enabled! You can now use the full features of this web application.
    </div>

    <script>
        // This script runs when JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Hide the no-JS message
            const noJsMessage = document.querySelector('.no-js');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Use style to hide the no-JS message
            }

            // Show the JS-enabled message
            const jsMessage = document.querySelector('.js');
            if (jsMessage) {
                jsMessage.style.display = 'block'; // Use style to show the JS message
            }
        });
    </script>

</body>
</html>
```
