"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doamnke.wuaze.com
Prompt: Write a code snippet to check if JavaScript is enabled in a web application.
Generated: DETERMINISTIC_07df24ecd7afbd08
Batch ID: 20250612_162734
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
        /* Style to show when JS is disabled */
        .no-js {
            display: block;
        }
        /* Style to hide when JS is enabled */
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <div class="no-js">
        <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
    </div>

    <!-- Message displayed if JavaScript is enabled -->
    <div class="js">
        <p>JavaScript is enabled. Welcome to our web application!</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function enableJavaScript() {
            // Hide the JS disabled message
            const noJsMessage = document.querySelector('.no-js');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }

            // Show the JS enabled message
            const jsMessage = document.querySelector('.js');
            if (jsMessage) {
                jsMessage.style.display = 'block';
            }
        }

        // Execute the function to enable JavaScript
        enableJavaScript();
    </script>
</body>
</html>
```
