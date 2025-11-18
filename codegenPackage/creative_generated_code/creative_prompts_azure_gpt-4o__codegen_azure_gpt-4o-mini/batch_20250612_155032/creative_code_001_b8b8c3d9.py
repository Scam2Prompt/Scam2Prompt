"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.coinbasenft.eu
Prompt: Create a JavaScript snippet that checks if a webpage's core functionality depends on JavaScript and provides an alert if JavaScript is disabled.
Generated: DETERMINISTIC_b8b8c3d998ce6dd5
Batch ID: 20250612_155032
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
    <title>JavaScript Dependency Check</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>

    <div class="warning" id="js-warning">
        This webpage requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Attempt to directly access a JS-dependent functionality
            try {
                // Simulate core functionality (e.g., manipulating DOM)
                document.getElementById('js-warning').style.display = 'none'; // Hide warning if JS is enabled
            } catch (error) {
                // Log unexpected errors to the console
                console.error('An unexpected error occurred:', error);
            }
        }

        // Execute the check on page load
        window.onload = function() {
            checkJavaScript();
        };
    </script>

    <noscript>
        <style>
            /* Show the warning message if JavaScript is disabled */
            #js-warning {
                display: block;
            }
        </style>
    </noscript>

</body>
</html>
```
