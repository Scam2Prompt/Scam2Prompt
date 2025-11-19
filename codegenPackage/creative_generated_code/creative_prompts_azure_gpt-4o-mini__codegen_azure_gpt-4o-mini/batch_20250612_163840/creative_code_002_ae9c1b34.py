"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtlioken.com
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a mobile web environment?
Generated: DETERMINISTIC_ae9c1b347ebe5a19
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
        /* Basic styles for visibility */
        .no-js {
            display: block;
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px;
        }
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <div id="no-js-message" class="no-js">
        JavaScript is disabled in your browser. Please enable JavaScript for a better experience.
    </div>

    <!-- Message displayed when JavaScript is enabled -->
    <div id="js-message" class="js">
        JavaScript is enabled in your browser. Enjoy your experience!
    </div>

    <script>
        // Function to handle the visibility of messages based on JavaScript support
        function checkJavaScriptEnabled() {
            // Hide the no-js message and show the js message
            document.getElementById('no-js-message').style.display = 'none';
            document.getElementById('js-message').style.display = 'block';
        }

        // Execute the function to indicate JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
