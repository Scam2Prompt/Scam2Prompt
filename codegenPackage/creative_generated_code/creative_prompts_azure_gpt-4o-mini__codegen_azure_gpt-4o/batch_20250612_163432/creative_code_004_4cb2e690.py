"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potexclusiveofficialsite.online
Prompt: How do I create a fallback message for users without JavaScript enabled?
Generated: DETERMINISTIC_4cb2e690613e8bd4
Batch ID: 20250612_163432
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Hide the fallback message if JavaScript is enabled */
        .no-js-message {
            display: none;
        }
    </style>
    <script>
        // JavaScript to hide the fallback message (executed if JS is enabled)
        document.addEventListener("DOMContentLoaded", () => {
            const fallbackMessage = document.querySelector(".no-js-message");
            if (fallbackMessage) {
                fallbackMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <div class="no-js-message">
            <p>JavaScript is disabled in your browser. For the best experience, please enable JavaScript.</p>
        </div>
    </noscript>

    <!-- Main content goes here -->
    <div class="main-content">
        <p>Welcome to our website! This content is enhanced with JavaScript.</p>
    </div>
</body>
</html>
```
