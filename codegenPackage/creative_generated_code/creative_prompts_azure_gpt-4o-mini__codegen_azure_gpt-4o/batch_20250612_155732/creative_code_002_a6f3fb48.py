"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aircash.club
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage?
Generated: DETERMINISTIC_a6f3fb48fa9e0192
Batch ID: 20250612_155732
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
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* The message is hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the "no-js-message" element
        document.addEventListener("DOMContentLoaded", function() {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- This message will be visible if JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled on this browser. Please enable it to view the content.
    </div>

    <!-- Content of the website -->
    <div>
        <h1>Welcome to the JavaScript-enabled webpage!</h1>
        <p>If you're seeing this, JavaScript is enabled on your browser.</p>
    </div>
</body>
</html>
```
