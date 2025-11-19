"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.fi
Prompt: Create a code example that detects JavaScript support in browsers for a site like Polkadot.fi.
Generated: DETERMINISTIC_6b18b50aa3d40419
Batch ID: 20250612_162605
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
    <title>JavaScript Detection</title>
    <style>
        /* Message styles for users with/without JavaScript */
        .no-js-message {
            display: none;
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
        .js-message {
            display: none;
            color: green;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Messages for JavaScript detection -->
    <noscript>
        <div class="no-js-message">JavaScript is disabled or not supported in your browser. Please enable JavaScript to use this site.</div>
    </noscript>
    <div id="js-message" class="js-message">JavaScript is supported and enabled in your browser!</div>

    <script>
        // Wrap code to ensure proper execution and prevent global variable pollution
        (function() {
            try {
                // Detect JavaScript capability and display appropriate message
                const jsMessage = document.getElementById('js-message');
                if (jsMessage) {
                    jsMessage.style.display = 'block'; // Show JavaScript-supported message
                }
            } catch (error) {
                // Handle unexpected errors gracefully
                console.error('An error occurred while detecting JavaScript support:', error);
            }
        })();
    </script>
</body>
</html>
```
