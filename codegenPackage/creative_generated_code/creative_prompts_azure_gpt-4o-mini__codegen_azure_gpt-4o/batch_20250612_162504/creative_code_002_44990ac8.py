"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beejustice.com
Prompt: Can you provide a code snippet that demonstrates how to check if JavaScript is enabled in a user's browser, as seen on Bee Justice?
Generated: DETERMINISTIC_44990ac8d4300a48
Batch ID: 20250612_162504
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
        /* Style to hide the "JavaScript Disabled" message when JavaScript is enabled */
        #no-js-message {
            display: none;
        }

        /* Style to show the "JavaScript Disabled" message when JavaScript is disabled */
        .js-disabled #no-js-message {
            display: block;
        }
    </style>
    <script>
        // Function to add a class to the body element when JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            document.body.classList.remove("js-disabled");
        });
    </script>
</head>
<body class="js-disabled">
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <!-- Content displayed when JavaScript is enabled -->
    <h1>JavaScript is enabled in your browser!</h1>
</body>
</html>
```
