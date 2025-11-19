"""
Generated Code Metadata:
========================
Original URL: https://usgddm.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "mobiles doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_fc9c451fc955ea82
Batch ID: 20250612_145619
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
            .noscript-message {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                padding: 1rem;
                background-color: #ffeb3b;
                color: #000;
                text-align: center;
                z-index: 9999;
                font-family: Arial, sans-serif;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Content goes here -->
    
    <noscript>
        <div class="noscript-message">
            This site (especially on mobile) doesn't work properly without JavaScript enabled. 
            Please enable JavaScript to continue.
        </div>
    </noscript>

    <script>
        // This script will run only if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Optional: You can add code here to remove the noscript message if needed
            // Though it won't be visible since JavaScript is enabled
        });
    </script>
</body>
</html>
```
