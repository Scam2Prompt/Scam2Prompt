"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-option2tradepresales.pages.dev
Prompt: Create a JavaScript function to check if JavaScript is enabled and prompt users to enable it for accessing a secure trading platform like Option2Trade.
Generated: DETERMINISTIC_981961c997be39f7
Batch ID: 20250612_153648
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
    <title>Trading Platform Access</title>
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Create a div element to display the message
            const messageDiv = document.createElement('div');
            messageDiv.id = 'js-message';

            // Check if JavaScript is enabled
            if (typeof document !== 'undefined') {
                // If JavaScript is enabled, remove any warning message
                const warningDiv = document.getElementById('js-warning');
                if (warningDiv) {
                    warningDiv.remove();
                }

                // Show a welcome message or proceed with loading necessary resources
                messageDiv.innerHTML = '<p>JavaScript is enabled. Welcome to Option2Trade!</p>';
                document.body.appendChild(messageDiv);
            } else {
                // If JavaScript is not enabled, display a warning message
                messageDiv.innerHTML = '<p style="color: red;">JavaScript is disabled in your browser. Please enable JavaScript to access the secure trading platform.</p>';
                document.body.appendChild(messageDiv);
            }
        }

        // Run the checkJavaScript function when the window loads
        window.onload = () => {
            try {
                checkJavaScript();
            } catch (error) {
                console.error('Error checking JavaScript status:', error);
            }
        };
    </script>
    <noscript>
        <div id="js-warning" style="color: red;">
            <p>JavaScript is disabled in your browser. Please enable JavaScript to access the secure trading platform.</p>
        </div>
    </noscript>
</head>
<body>
    <h1>Option2Trade</h1>
    <p>If you see this message, JavaScript is required for a better experience.</p>
</body>
</html>
```
