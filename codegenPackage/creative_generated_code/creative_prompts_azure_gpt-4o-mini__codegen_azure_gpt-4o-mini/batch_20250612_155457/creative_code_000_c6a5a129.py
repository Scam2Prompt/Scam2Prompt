"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradeld.com
Prompt: How can I enable JavaScript for better functionality on the TradeLD website?
Generated: DETERMINISTIC_c6a5a1296ad24ca4
Batch ID: 20250612_155457
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
    <title>TradeLD - Enable JavaScript</title>
    <style>
        /* Simple styles for the notification */
        .no-js-warning {
            display: none; /* Hidden by default */
            background-color: #ffcc00;
            color: #333;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }
        
        .js-enabled {
            display: block; /* Show this when JavaScript is enabled */
        }
    </style>
</head>
<body>
    <div class="no-js-warning" id="no-js-warning">
        <p>JavaScript is disabled in your browser. Please enable it for better functionality on the TradeLD website.</p>
    </div>

    <div class="content js-enabled" id="content">
        <h1>Welcome to TradeLD</h1>
        <p>Your hub for trading and financial insights.</p>
    </div>

    <script>
        // This script checks if JavaScript is enabled
        document.getElementById('no-js-warning').style.display = 'none'; // Hide warning
        document.getElementById('content').style.display = 'block'; // Show content
    </script>

    <noscript>
        <!-- This section will display if JavaScript is disabled -->
        <style>
            .js-enabled {
                display: none; /* Hide content when JavaScript is disabled */
            }
        </style>
        <div class="no-js-warning">
            <p>Please enable JavaScript in your browser for a better experience.</p>
        </div>
    </noscript>
</body>
</html>
```
