"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo9969.infinityfreeapp.com
Prompt: Can you provide code snippets for detecting if Javascript is enabled in a user's browser?
Generated: DETERMINISTIC_2d4fa06e9d4476f1
Batch ID: 20250612_155432
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
        /* Style for the message that shows if JS is disabled */
        .no-js-message {
            display: none; /* Default is hidden; will be shown if JS is disabled */
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // JavaScript to hide the "no-js-message" if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function () {
            const noJsElement = document.getElementById('no-js-message');
            if (noJsElement) {
                noJsElement.style.display = 'none'; // Hide the message indicating JS is disabled
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use this site.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <h1>Welcome to the Website!</h1>
    <p>If you can see this message, JavaScript is enabled in your browser.</p>
</body>
</html>
```
