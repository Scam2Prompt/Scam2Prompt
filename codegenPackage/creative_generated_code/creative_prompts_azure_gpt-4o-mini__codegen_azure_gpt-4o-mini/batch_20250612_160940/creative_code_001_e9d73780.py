"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiggzfgkcug3orqglqbsuqq3hz4xsex7t33fmchtsyoasmxw6jrmyi.ipfs.dweb.link
Prompt: What are the best practices for ensuring JavaScript is enabled in web applications?
Generated: DETERMINISTIC_e9d73780da4239eb
Batch ID: 20250612_160940
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Basic styles for informational message */
        .js-enabled {
            display: none;
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
            JavaScript is disabled in your browser. Please enable JavaScript to experience the full functionality of this website.
        </div>
    </noscript>

    <div class="js-enabled">
        JavaScript is enabled! Welcome to our website.
    </div>

    <script>
        // This function displays a message if JavaScript is enabled
        function showJsEnabledMessage() {
            // Select the elements for messages
            const jsEnabledMessage = document.querySelector('.js-enabled');
            const jsDisabledMessage = document.querySelector('.js-disabled');

            // Check if the elements exist before modifying them
            if (jsEnabledMessage && jsDisabledMessage) {
                jsEnabledMessage.style.display = 'block'; // Show JS enabled message
                jsDisabledMessage.style.display = 'none'; // Hide JS disabled message
            } else {
                console.error('Error: Message elements not found in the DOM.');
            }
        }

        // Invoke the function to show the message
        showJsEnabledMessage();
    </script>
</body>
</html>
```
