"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcqee.com
Prompt: Create a script to detect if JavaScript is disabled on a user's browser and display an alert for enabling it, specifically for Bitcoin-related services.
Generated: DETERMINISTIC_d565303c7807ebe9
Batch ID: 20250612_152600
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
    <title>Bitcoin Service - JavaScript Check</title>
    <style>
        /* Fallback message styling */
        #no-js-alert {
            display: none; /* Hidden by default, only visible if JS is disabled */
            background-color: #ffcccc;
            color: #000;
            padding: 15px;
            border: 2px solid #ff0000;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
        }
    </style>
    <noscript>
        <!-- Display message if JavaScript is disabled -->
        <div id="no-js-alert">
            JavaScript is disabled in your browser. For Bitcoin-related services, please enable JavaScript for proper functionality.
        </div>
    </noscript>
</head>
<body>
    <!-- Main content -->
    <h1>Welcome to Bitcoin Service</h1>
    <p>Please ensure JavaScript is enabled for a seamless experience.</p>

    <script>
        // JavaScript-enabled fallback logic
        document.addEventListener('DOMContentLoaded', function () {
            try {
                // Ensure the no-script alert is hidden if JS is enabled
                const noJsAlert = document.getElementById('no-js-alert');
                if (noJsAlert) {
                    noJsAlert.style.display = 'none';
                }
            } catch (error) {
                // Log any unexpected errors
                console.error('An error occurred while hiding the no-JS alert:', error);
            }
        });
    </script>
</body>
</html>
```
