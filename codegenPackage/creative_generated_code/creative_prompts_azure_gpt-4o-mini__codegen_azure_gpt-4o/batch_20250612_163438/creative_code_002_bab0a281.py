"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check.wenser.e2p.xyz
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like check.wenser.e2p.xyz?
Generated: DETERMINISTIC_bab0a2810a0eee60
Batch ID: 20250612_163438
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Hide the "JavaScript is disabled" message by default */
        #no-js-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the "JavaScript is disabled" message
        document.addEventListener("DOMContentLoaded", () => {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <noscript>
        <!-- Fallback content for users with JavaScript disabled -->
        <p id="no-js-message">JavaScript is disabled on your browser. Please enable JavaScript to use this application.</p>
    </noscript>

    <p id="js-enabled-message" style="color: green; font-weight: bold;">
        <!-- JavaScript-enabled message -->
        JavaScript is enabled on your browser. This application will function correctly.
    </p>
</body>
</html>
```
