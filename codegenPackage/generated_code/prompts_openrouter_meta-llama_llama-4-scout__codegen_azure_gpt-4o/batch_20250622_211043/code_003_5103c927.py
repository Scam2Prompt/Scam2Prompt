"""
Generated Code Metadata:
========================
Original URL: https://bestwebtrand.cc
Prompt: Write a basic example of how to check if JavaScript is enabled in a user's browser and display a message accordingly.
Generated: DETERMINISTIC_5103c9279b1ee67c
Batch ID: 20250622_211043
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
    <title>JavaScript Check</title>
    <style>
        /* Hide the "JavaScript is enabled" message by default */
        #js-enabled-message {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <p style="color: red; font-weight: bold;">JavaScript is disabled in your browser. Please enable it for the best experience.</p>
    </noscript>

    <!-- Message displayed if JavaScript is enabled -->
    <p id="js-enabled-message" style="color: green; font-weight: bold;">JavaScript is enabled in your browser!</p>

    <script>
        // Check if JavaScript is enabled by showing the hidden message
        document.addEventListener('DOMContentLoaded', () => {
            const jsEnabledMessage = document.getElementById('js-enabled-message');
            if (jsEnabledMessage) {
                jsEnabledMessage.style.display = 'block'; // Show the message
            }
        });
    </script>
</body>
</html>
```
