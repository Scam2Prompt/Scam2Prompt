"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Generate a JavaScript snippet to detect if JavaScript is enabled in the browser, inspired by Tim Mansell's website functionality.
Generated: DETERMINISTIC_58a3a1e20d07a620
Batch ID: 20250612_151018
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
    <title>JavaScript Detection</title>
    <style>
        /* Basic styles for the message display */
        .js-enabled {
            display: none;
            color: green;
            font-weight: bold;
        }
        .js-disabled {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="js-disabled">JavaScript is disabled in your browser.</div>
    </noscript>
    <div class="js-enabled">JavaScript is enabled in your browser.</div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            try {
                // Show the message for JavaScript enabled
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                // Log any errors to the console for debugging
                console.error('Error displaying JavaScript enabled message:', error);
            }
        }

        // Call the function to detect JavaScript
        detectJavaScript();
    </script>
</body>
</html>
```
