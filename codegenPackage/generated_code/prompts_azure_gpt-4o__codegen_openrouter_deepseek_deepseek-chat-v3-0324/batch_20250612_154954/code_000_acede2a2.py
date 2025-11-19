"""
Generated Code Metadata:
========================
Original URL: https://d952.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message like "mining-h5 doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_acede2a23bea3833
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <noscript>
        <style>
            .no-script-message {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #ffcccc;
                color: #cc0000;
                padding: 10px;
                text-align: center;
                z-index: 9999;
                border-bottom: 1px solid #cc0000;
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Content that requires JavaScript -->
    
    <noscript>
        <div class="no-script-message">
            mining-h5 doesn't work properly without JavaScript enabled. Please enable JavaScript to continue.
        </div>
    </noscript>

    <script>
        // Remove noscript message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const noscriptElements = document.getElementsByTagName('noscript');
            while (noscriptElements.length > 0) {
                noscriptElements[0].parentNode.removeChild(noscriptElements[0]);
            }
        });
    </script>
</body>
</html>
```
