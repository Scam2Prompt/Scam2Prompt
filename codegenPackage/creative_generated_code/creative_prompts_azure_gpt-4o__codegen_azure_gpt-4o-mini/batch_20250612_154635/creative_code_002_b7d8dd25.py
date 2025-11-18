"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea.vercel.app
Prompt: Generate JavaScript code to check whether JavaScript is enabled in a user's browser and display a custom message if it is disabled.
Generated: DETERMINISTIC_b7d8dd25da08ccab
Batch ID: 20250612_154635
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
        /* Styles for the message display */
        #js-disabled-message {
            display: none; /* Hide message by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it to use all features of this site.
        </div>
    </noscript>

    <script>
        /**
         * Function to check if JavaScript is enabled.
         * If enabled, it hides the message for disabled JS.
         */
        function checkJavaScriptEnabled() {
            const jsDisabledMessage = document.getElementById('js-disabled-message');

            // If JavaScript is enabled, hide the message
            jsDisabledMessage.style.display = 'none';
        }

        // Call the function to check JavaScript status
        try {
            checkJavaScriptEnabled();
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
        }
    </script>
</body>
</html>
```
