"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethupea.com
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a message prompting users to enable it for Ethereum pledge functionality.
Generated: DETERMINISTIC_9baa1baa95bf5ed6
Batch ID: 20250612_145619
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
    <title>Enable JavaScript for Ethereum Pledge</title>
    <style>
        /* Styling for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default, shown only if JavaScript is disabled */
            color: red;
            font-size: 1.2rem;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use the Ethereum pledge functionality.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="app">
        <h1>Welcome to the Ethereum Pledge Page</h1>
        <p>Enjoy seamless contributions using Ethereum, powered by JavaScript.</p>
    </div>

    <script>
        // This script ensures the page behaves properly when JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            // Example message to verify JavaScript is running
            console.log("JavaScript is successfully enabled.");
            // You can add Ethereum pledge functionality here
        });

        // If JavaScript is enabled, hide the no-js-message (though it won't be visible due to <noscript>)
        const noJsMessage = document.querySelector('.no-js-message');
        if (noJsMessage) {
            noJsMessage.style.display = 'none';
        }
    </script>
</body>
</html>
```
