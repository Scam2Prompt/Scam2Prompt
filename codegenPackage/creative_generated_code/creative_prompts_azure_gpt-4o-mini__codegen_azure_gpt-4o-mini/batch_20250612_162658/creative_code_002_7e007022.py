"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerai.eu
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_7e0070227c920f25
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Styles for the message */
        .no-js {
            display: none; /* Hide by default */
        }
        .js {
            display: block; /* Show if JavaScript is enabled */
        }
    </style>
</head>
<body>
    <!-- Message for users with JavaScript disabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
        </div>
    </noscript>

    <!-- Message for users with JavaScript enabled -->
    <div class="js">
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // Immediately invoked function to check for JavaScript support
        (function() {
            try {
                // If this script runs, JavaScript is enabled
                document.querySelector('.js').style.display = 'block';
            } catch (error) {
                // Log any errors to the console
                console.error("Error in checking JavaScript support:", error);
            }
        })();
    </script>
</body>
</html>
```
