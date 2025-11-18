"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mokent.com
Prompt: Write code to display a custom error message when JavaScript is disabled on a trading website like MOKENT Trading.
Generated: DETERMINISTIC_7dc19e67cb595f7a
Batch ID: 20250612_154145
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
    <title>MOKENT Trading</title>
    <style>
        /* Styling for the error message */
        .no-js-message {
            display: none; /* Hidden by default */
            color: #fff;
            background-color: #ff0000;
            padding: 20px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Custom error message for when JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is required to use the MOKENT Trading platform. Please enable JavaScript in your browser settings to continue.
        </div>
    </noscript>

    <!-- Main content of the website -->
    <div id="main-content">
        <h1>Welcome to MOKENT Trading</h1>
        <p>Loading trading tools...</p>
    </div>

    <script>
        // Ensure proper functionality only if JavaScript is enabled
        // If JavaScript is enabled, the no-js-message is already hidden by default
        document.addEventListener("DOMContentLoaded", () => {
            // JavaScript logic for the trading platform goes here
            console.log("JavaScript is enabled. Trading platform initialized.");
        });
    </script>
</body>
</html>
```
