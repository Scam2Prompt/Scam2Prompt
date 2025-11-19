"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiacelestia.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in the browser for Celestia's Glow Node?
Generated: DETERMINISTIC_a9830a912a4fda66
Batch ID: 20250612_163231
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
    <title>JavaScript Check for Celestia's Glow Node</title>
    <style>
        /* Fallback message styling when JavaScript is disabled */
        .no-js-message {
            display: none; /* Default state when JavaScript is enabled */
            color: red;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the fallback message
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</head>
<body>
    <h1>Welcome to Celestia's Glow Node</h1>

    <!-- Fallback message for browsers with JavaScript disabled -->
    <noscript>
        <div id="no-js-message" class="no-js-message">
            JavaScript is required to use Celestia's Glow Node. Please enable JavaScript in your browser.
        </div>
    </noscript>

    <!-- Main application content -->
    <div id="app">
        <!-- Content that requires JavaScript will go here -->
        <p>JavaScript is enabled. You can use Celestia's Glow Node functionalities.</p>
    </div>
</body>
</html>
```
