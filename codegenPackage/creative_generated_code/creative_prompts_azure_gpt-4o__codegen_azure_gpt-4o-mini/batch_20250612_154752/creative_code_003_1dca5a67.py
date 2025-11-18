"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://combo.magiceden.nl
Prompt: Generate JavaScript code to display a warning message and block access to a webpage if JavaScript is not enabled, mimicking the behavior described on the Magic Eden NL site.
Generated: DETERMINISTIC_1dca5a6746abb2c6
Batch ID: 20250612_154752
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
    <title>JavaScript Check</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 24px;
            z-index: 1000;
        }
    </style>
</head>
<body>
    <div id="js-warning">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript to access this website.</p>
    </div>

    <script>
        // Function to display the warning message
        function displayWarning() {
            const warningDiv = document.getElementById('js-warning');
            warningDiv.style.display = 'block'; // Show the warning message
        }

        // Check if JavaScript is enabled
        if (typeof document !== 'undefined' && document.readyState !== 'loading') {
            // JavaScript is enabled, do nothing
        } else {
            // JavaScript is not enabled, display the warning
            displayWarning();
        }
    </script>
</body>
</html>
```
