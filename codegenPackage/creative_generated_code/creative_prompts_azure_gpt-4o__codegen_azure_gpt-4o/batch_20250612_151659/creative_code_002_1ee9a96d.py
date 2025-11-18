"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop.gti.finance
Prompt: Generate code to detect if JavaScript is enabled in a browser and display a message prompting users to enable it, as required by web apps like GTI Finance's airdrop service.
Generated: DETERMINISTIC_1ee9a96dc80d39dd
Batch ID: 20250612_151659
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
        /* This message will show if JavaScript is disabled */
        .no-js-message {
            display: block;
            font-size: 18px;
            color: red;
            text-align: center;
            margin-top: 50px;
        }
        /* When JavaScript is enabled, this message will be hidden */
        .js-enabled {
            display: none;
        }
    </style>
    <noscript>
        <!-- Message for users with JavaScript disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this service.
        </div>
    </noscript>
</head>
<body>
    <!-- Content for users with JavaScript enabled -->
    <div class="js-enabled">
        <h1>Welcome to GTI Finance Airdrop Service!</h1>
        <p>JavaScript is enabled in your browser. You can now continue using this service.</p>
    </div>

    <script>
        // Ensure the proper message is displayed for users with JavaScript enabled
        document.addEventListener('DOMContentLoaded', () => {
            try {
                const jsEnabledContent = document.querySelector('.js-enabled');
                const noJsMessage = document.querySelector('.no-js-message');

                // Hide the no-JS message and show the JS-enabled content
                if (jsEnabledContent) {
                    jsEnabledContent.style.display = 'block';
                }
                if (noJsMessage) {
                    noJsMessage.style.display = 'none';
                }
            } catch (error) {
                console.error('An error occurred while detecting JavaScript:', error);
            }
        });
    </script>
</body>
</html>
```
