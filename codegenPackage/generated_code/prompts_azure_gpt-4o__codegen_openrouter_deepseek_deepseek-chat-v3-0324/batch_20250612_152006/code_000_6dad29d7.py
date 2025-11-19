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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <noscript>
        <style>
            .no-script-message {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                padding: 1em;
                background-color: #ffeb3b;
                color: #000;
                text-align: center;
                z-index: 9999;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Content that requires JavaScript -->
    
    <noscript>
        <div class="no-script-message">
            <p>This app doesn't work properly without JavaScript enabled. Please enable JavaScript to continue.</p>
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
