"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aubi.online
Prompt: Provide an example of how to implement a fallback for users who have JavaScript disabled on aubi.online.
Generated: DETERMINISTIC_b926911ead07389a
Batch ID: 20250612_162203
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
    <title>Aubi Online</title>
    <style>
        /* Style for the fallback content */
        .no-js-message {
            display: none; /* Default hidden, shown if JS is disabled */
            color: #ff0000;
            font-size: 1.2em;
            text-align: center;
            margin-top: 20px;
        }
        .js-enabled-content {
            display: none; /* Hide until JS enables it */
        }
    </style>
</head>
<body>
    <!-- Fallback content for users with JavaScript disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. To use this site properly, please enable JavaScript or contact support for assistance.
        </div>
    </noscript>

    <!-- Content visible only when JavaScript is enabled -->
    <div class="js-enabled-content">
        <p>Welcome to Aubi Online! JavaScript is enabled, and the site is fully functional.</p>
    </div>

    <script>
        try {
            // Enable content if JavaScript is functional
            const jsEnabledContent = document.querySelector('.js-enabled-content');
            if (jsEnabledContent) {
                jsEnabledContent.style.display = 'block';
            }
        } catch (error) {
            console.error('An error occurred while enabling JavaScript content:', error);
        }
    </script>
</body>
</html>
```
