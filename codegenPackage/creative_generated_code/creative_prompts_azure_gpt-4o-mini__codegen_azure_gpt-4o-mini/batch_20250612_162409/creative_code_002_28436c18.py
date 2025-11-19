"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask.com
Prompt: Can you provide a code snippet for checking if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_28436c18da98a455
Batch ID: 20250612_162409
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Message to be shown if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <!-- Main content -->
    <div id="main-content">
        <h1>Welcome to My Website</h1>
        <p>This content is visible if JavaScript is enabled.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // If the script runs without errors, JavaScript is enabled
                console.log("JavaScript is enabled.");
            } catch (error) {
                // Log the error if something goes wrong (unlikely in this case)
                console.error("Error while checking JavaScript:", error);
            }
        }

        // Call the function to check JavaScript
        checkJavaScript();
    </script>
</body>
</html>
```
