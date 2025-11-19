"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foxylinea.presale.com
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and prompts the user to enable it if not.
Generated: DETERMINISTIC_286390ba9bb8104d
Batch ID: 20250612_135152
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
    <noscript>
        <style>
            /* Hides content if JavaScript is disabled */
            body {
                display: none;
            }
            #no-js-warning {
                display: block;
                background-color: #f44336; /* Red background */
                color: white; /* White text */
                padding: 20px;
                text-align: center;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
            }
        </style>
    </noscript>
</head>
<body>
    <div id="no-js-warning" style="display:none;">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript to improve your experience.</p>
    </div>

    <script>
        // Function to show warning if JavaScript is disabled
        function checkJavaScriptEnabled() {
            const warningDiv = document.getElementById('no-js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'none'; // Hide warning if JavaScript is enabled
            }
        }

        // Invoke the function to check for JavaScript
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
