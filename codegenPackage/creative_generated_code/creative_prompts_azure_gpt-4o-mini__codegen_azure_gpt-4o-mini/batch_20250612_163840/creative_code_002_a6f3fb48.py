"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovkean.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage?
Generated: DETERMINISTIC_a6f3fb48fa9e0192
Batch ID: 20250612_163840
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
        /* Style for the message when JavaScript is disabled */
        #no-js-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <!-- Main content of the page -->
    <h1>Welcome to Our Website!</h1>
    <p>This page requires JavaScript to function properly.</p>

    <script>
        // Function to show the message if JavaScript is disabled
        function checkJavaScriptEnabled() {
            // Hide the JavaScript disabled message
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none';
        }

        // Execute the function to indicate JavaScript is enabled
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <!-- Fallback content for when JavaScript is disabled -->
        <style>
            /* Show the message when JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>

</body>
</html>
```
