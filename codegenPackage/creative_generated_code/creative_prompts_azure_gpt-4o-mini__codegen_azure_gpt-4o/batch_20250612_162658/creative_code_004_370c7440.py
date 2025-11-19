"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerai.eu
Prompt: How do I implement a fallback for users who have JavaScript disabled on my website?
Generated: DETERMINISTIC_370c74406a04dfa8
Batch ID: 20250612_162658
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
        /* Basic styles for the fallback message */
        .no-js-message {
            display: none;
            color: red;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Content for JavaScript-enabled users -->
    <div id="js-content">
        <h1>Welcome to Our Website</h1>
        <p>This content is displayed because JavaScript is enabled in your browser.</p>
    </div>

    <!-- Fallback content for users without JavaScript -->
    <noscript>
        <div class="no-js-message">
            <h1>JavaScript Disabled</h1>
            <p>It appears that JavaScript is disabled in your browser. Some functionality may be limited.</p>
        </div>
    </noscript>

    <script>
        // Ensure the fallback message is hidden when JavaScript is enabled
        try {
            document.addEventListener('DOMContentLoaded', () => {
                // Verify that JavaScript is active and hide fallback content
                const fallbackMessage = document.querySelector('.no-js-message');
                if (fallbackMessage) {
                    fallbackMessage.style.display = 'none';
                }
            });
        } catch (error) {
            console.error('An error occurred while processing JavaScript fallback logic:', error);
        }
    </script>
</body>
</html>
```
