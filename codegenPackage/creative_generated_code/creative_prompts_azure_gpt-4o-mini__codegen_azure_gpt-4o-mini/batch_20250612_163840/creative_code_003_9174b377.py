"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Provide an example of how to create a fallback message for users who have JavaScript disabled on their mobile devices.
Generated: DETERMINISTIC_9174b3771418252d
Batch ID: 20250612_163840
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
    <title>Fallback Message Example</title>
    <style>
        /* Style for fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <script>
        // Function to show content when JavaScript is enabled
        function enableContent() {
            const content = document.getElementById('main-content');
            if (content) {
                content.style.display = 'block'; // Show main content
            }
            const fallback = document.getElementById('fallback-message');
            if (fallback) {
                fallback.style.display = 'none'; // Hide fallback message
            }
        }

        // Call enableContent to display main content
        document.addEventListener('DOMContentLoaded', enableContent);
    </script>
</head>
<body>
    <div id="fallback-message" class="fallback-message">
        <strong>JavaScript is disabled.</strong> Please enable JavaScript in your browser settings to view the full content of this page.
    </div>

    <div id="main-content" style="display: none;">
        <h1>Welcome to Our Website!</h1>
        <p>This content is only visible when JavaScript is enabled.</p>
        <!-- Add more interactive content here -->
    </div>
</body>
</html>
```
