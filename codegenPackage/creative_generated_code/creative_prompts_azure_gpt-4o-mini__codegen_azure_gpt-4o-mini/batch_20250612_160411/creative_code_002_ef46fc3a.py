"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbgemcredentialorg.web.app
Prompt: Can you provide a code snippet for checking if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_ef46fc3a399dca52
Batch ID: 20250612_160411
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
        /* Styles for content when JS is disabled */
        .no-js {
            display: block;
        }
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable JavaScript to use this web application.</p>
        </div>
    </noscript>

    <!-- Content that requires JavaScript -->
    <div class="js">
        <h1>Welcome to the Web Application!</h1>
        <p>JavaScript is enabled. You can now use all features of this application.</p>
    </div>

    <script>
        // Function to execute when the page loads
        document.addEventListener('DOMContentLoaded', () => {
            // Switch the visibility based on JS support
            const jsEnabledDiv = document.querySelector('.js');
            const noJsDiv = document.querySelector('.no-js');

            try {
                // Show the JS-enabled content
                jsEnabledDiv.style.display = 'block';
                noJsDiv.style.display = 'none';
            } catch (error) {
                console.error('Error while checking JavaScript support:', error);
            }
        });
    </script>
</body>
</html>
```
