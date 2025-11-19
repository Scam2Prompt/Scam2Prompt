"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://confluence.dr-ex02.coinbaseindexfund.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_161125
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
        JavaScript is enabled! Welcome to our web application.
    </div>

    <script>
        // Enable the .js class if JavaScript is detected
        document.addEventListener("DOMContentLoaded", function() {
            // Hide the no-js message and show the js message
            document.querySelector('.no-js').style.display = 'none';
            document.querySelector('.js').style.display = 'block';
        });
    </script>

</body>
</html>
```
