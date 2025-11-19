"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magnekt.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for WordPress.com?
Generated: DETERMINISTIC_1427b4c8434c88a2
Batch ID: 20250612_163117
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
        /* Basic styles for the message display */
        #js-message {
            display: none; /* Hidden by default */
            color: green;
            font-weight: bold;
        }
        #no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div id="js-message">JavaScript is enabled in your browser.</div>
    <div id="no-js-message">JavaScript is not enabled. Please enable it for the best experience.</div>

    <script>
        // Immediately invoked function to check JavaScript status
        (function() {
            try {
                // Show the message if JavaScript is enabled
                document.getElementById('js-message').style.display = 'block';
            } catch (error) {
                console.error('An error occurred while checking JavaScript status:', error);
            }
        })();
    </script>

    <noscript>
        <!-- This message is displayed if JavaScript is disabled -->
        <style>
            #js-message { display: none; } /* Hide JavaScript enabled message */
            #no-js-message { display: block; } /* Show the no-JavaScript message */
        </style>
        <div id="no-js-message">JavaScript is not enabled. Please enable it for the best experience.</div>
    </noscript>

</body>
</html>
```
