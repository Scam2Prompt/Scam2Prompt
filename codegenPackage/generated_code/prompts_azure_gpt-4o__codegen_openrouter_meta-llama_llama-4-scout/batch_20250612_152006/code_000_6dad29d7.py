"""
Generated Code Metadata:
========================
Original URL: https://lrt-sym.biotic.fi
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_6dad29d76354783c
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <style>
        #js-detection-message {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f44336;
            color: #ffffff;
            padding: 1em;
            text-align: center;
        }
    </style>
</head>
<body>
    <noscript id="js-detection-message">
        This app doesn't work properly without JavaScript enabled.
    </noscript>

    <script>
        // Check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            const jsDetectionMessage = document.getElementById('js-detection-message');
            if (jsDetectionMessage) {
                jsDetectionMessage.style.display = 'none';
            }
        }

        // Run the check on page load
        document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
    </script>
</body>
</html>
```
