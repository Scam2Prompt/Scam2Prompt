"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethzao.com
Prompt: How can I create a fallback message for users who have JavaScript disabled on my website?
Generated: DETERMINISTIC_1d422323bdd50a9e
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
    <title>JavaScript Disabled Fallback</title>
    <style>
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Content that requires JavaScript -->
    <div id="main-content">
        <h1>Welcome to My Website</h1>
        <p>This content is enhanced by JavaScript.</p>
    </div>

    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <div class="no-js-message">
            <p>It seems JavaScript is disabled in your browser. Please enable JavaScript to view the full functionality of this site.</p>
        </div>
    </noscript>

    <script>
        // JavaScript content goes here
        // This script ensures the noscript tag is only relevant when JavaScript is disabled
        console.log('JavaScript is enabled');
    </script>
</body>
</html>
```
