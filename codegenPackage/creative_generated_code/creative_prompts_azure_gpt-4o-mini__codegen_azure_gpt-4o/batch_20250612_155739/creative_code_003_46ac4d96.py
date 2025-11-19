"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxlbank.com
Prompt: Provide a code snippet to detect if JavaScript is enabled and display a message if it's not, similar to the MaxL Bank warning.
Generated: DETERMINISTIC_46ac4d9693544690
Batch ID: 20250612_155739
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
        /* Style for the no-JavaScript warning message */
        .no-js-warning {
            display: none; /* Start hidden, displayed only if JS is disabled */
            color: red;
            font-size: 1.2em;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div class="no-js-warning">JavaScript is not enabled. Please enable JavaScript to fully experience this website.</div>
    </noscript>

    <!-- Content of the page -->
    <div>
        <h1>Welcome to MaxL Bank</h1>
        <p>Your trusted partner in banking and financial solutions.</p>
    </div>

    <script>
        // JavaScript code here - if JavaScript is enabled, this will run and no warning will be shown.
        document.addEventListener("DOMContentLoaded", function () {
            // All functionality goes here.
            console.log("JavaScript is enabled.");
        });
    </script>
</body>
</html>
```
