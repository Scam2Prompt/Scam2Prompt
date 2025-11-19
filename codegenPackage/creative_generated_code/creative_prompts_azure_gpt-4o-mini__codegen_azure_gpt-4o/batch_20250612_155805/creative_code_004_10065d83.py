"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstract.co.in
Prompt: How do I create a fallback message for users who have JavaScript disabled when accessing the Abstract website?
Generated: DETERMINISTIC_10065d83b90f89a6
Batch ID: 20250612_155805
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
    <title>Abstract Website</title>
    <style>
        /* Basic styling for the fallback message */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 4px;
            margin: 20px;
            text-align: center;
        }
    </style>
    <script>
        // JavaScript code to hide the fallback message for users with JavaScript enabled
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.querySelector('.no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Ensure the fallback is hidden
            }
        });
    </script>
</head>
<body>
    <!-- Fallback message for users with JavaScript disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled or not supported in your browser. Please enable JavaScript for the best experience on the Abstract website.
        </div>
    </noscript>

    <!-- Main content of the Abstract website -->
    <h1>Welcome to the Abstract Website</h1>
    <p>This website relies on JavaScript for interactive functionality.</p>
</body>
</html>
```
