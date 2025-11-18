"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getbonus.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the GetBonus domain details page.
Generated: DETERMINISTIC_177cd614adcf41b4
Batch ID: 20250612_154703
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
    <title>Enable JavaScript</title>
    <style>
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Initially hidden when JavaScript is enabled */
            font-family: Arial, sans-serif;
            font-size: 18px;
            color: red;
            padding: 20px;
            text-align: center;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px auto;
            width: 80%;
        }
    </style>
</head>
<body>
    <!-- This message will be visible only if JavaScript is disabled -->
    <div class="no-js-message" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to view this site properly.
    </div>

    <script>
        /*
         * JavaScript is enabled: Hide the fallback message
         * The message is already present in the HTML for cases where JavaScript is disabled.
         */
        document.getElementById('no-js-message').style.display = 'none';
    </script>
</body>
</html>
```
