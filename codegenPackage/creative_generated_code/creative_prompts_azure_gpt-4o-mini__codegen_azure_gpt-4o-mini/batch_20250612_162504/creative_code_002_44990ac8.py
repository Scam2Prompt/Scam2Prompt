"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beejustice.com
Prompt: Can you provide a code snippet that demonstrates how to check if JavaScript is enabled in a user's browser, as seen on Bee Justice?
Generated: DETERMINISTIC_44990ac8d4300a48
Batch ID: 20250612_162504
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
            display: none; /* Initially hidden */
            color: green;
            font-weight: bold;
        }
        .js-disabled {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="js-disabled">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>

    <div class="js-enabled">
        JavaScript is enabled in your browser. Welcome!
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Display the message for JavaScript enabled users
                document.querySelector('.js-enabled').style.display = 'block';
            } catch (err) {
                // Log error to console for debugging
                console.error('Error displaying JavaScript enabled message:', err);
            }
        }

        // Run the function to check JavaScript status
        checkJavaScript();
    </script>
    
</body>
</html>
```
