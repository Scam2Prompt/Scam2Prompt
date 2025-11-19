"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrtkn.wuaze.com
Prompt: Can you provide a code snippet that checks if Javascript is enabled in a user's browser?
Generated: DETERMINISTIC_976195827b2cca1a
Batch ID: 20250612_162806
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
        /* Hide the message by default, it will be shown if JS is enabled */
        .js-enabled {
            display: none;
        }
        .no-js {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <div class="no-js">
        <h1>JavaScript is disabled in your browser.</h1>
        <p>Please enable JavaScript for a better experience.</p>
    </div>

    <!-- Message shown when JavaScript is enabled -->
    <div class="js-enabled">
        <h1>JavaScript is enabled!</h1>
        <p>Thank you for enabling JavaScript.</p>
    </div>

    <script>
        // Function to execute when the script loads
        function checkJavaScript() {
            // Hide the no-js message and show the js-enabled message
            document.querySelector('.no-js').style.display = 'none';
            document.querySelector('.js-enabled').style.display = 'block';
        }

        // Call the function to check JavaScript
        try {
            checkJavaScript();
        } catch (error) {
            console.error("An error occurred while checking JavaScript status:", error);
        }
    </script>
</body>
</html>
```
