"""
Generated Code Metadata:
========================
Original URL: https://huijiatw.com
Prompt: Generate a basic HTML template that includes a JavaScript check to ensure the page functions correctly with JavaScript enabled.
Generated: DETERMINISTIC_e8f59898decfcd33
Batch ID: 20250622_205306
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
    <title>JavaScript Check Template</title>
    <style>
        /* Basic styling for the no-js message */
        .no-js-message {
            padding: 20px;
            background-color: #ffcccc;
            border: 1px solid #ff9999;
            text-align: center;
            margin: 10px;
        }
    </style>
</head>
<body>
    <!-- Content that requires JavaScript -->
    <div id="js-content">
        <h1>Welcome to My Page</h1>
        <p>This content is displayed when JavaScript is enabled.</p>
    </div>

    <!-- Fallback content for when JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            <h2>JavaScript is Disabled</h2>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
        </div>
    </noscript>

    <script>
        // Immediately hide the JavaScript content if JS is disabled
        // (though noscript will handle most cases, this ensures complete coverage)
        document.addEventListener('DOMContentLoaded', function() {
            try {
                // Check if JavaScript is enabled by attempting a basic operation
                if (typeof window !== 'undefined' && window.document) {
                    // JavaScript is enabled - ensure JS content is visible
                    document.getElementById('js-content').style.display = 'block';
                }
            } catch (e) {
                // If any error occurs, assume JavaScript is not fully functional
                console.error('JavaScript error detected:', e);
                document.getElementById('js-content').style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
