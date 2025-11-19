"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lp.btcc.limited
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like BTCC?
Generated: DETERMINISTIC_e0ed40f75a53a5da
Batch ID: 20250612_163958
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
        /* Styles for the message display */
        .js-enabled {
            display: none; /* Hide by default */
        }
        .no-js {
            display: none; /* Hide by default */
        }
    </style>
</head>
<body>
    <noscript>
        <style>
            /* Show the message if JavaScript is disabled */
            .no-js {
                display: block;
                color: red;
                font-weight: bold;
            }
        </style>
        <div class="no-js">
            JavaScript is disabled in your browser. Please enable JavaScript to use this application.
        </div>
    </noscript>

    <div class="js-enabled">
        JavaScript is enabled! Welcome to the application.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Show the message for JavaScript enabled
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (error) {
                // Log error to console for debugging
                console.error('Error displaying JS enabled message:', error);
            }
        }

        // Call the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
