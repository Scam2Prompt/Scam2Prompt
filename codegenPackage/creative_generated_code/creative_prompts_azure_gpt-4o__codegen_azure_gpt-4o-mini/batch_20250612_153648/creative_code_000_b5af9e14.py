"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earndrop.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message prompting the user to enable it.
Generated: DETERMINISTIC_b5af9e14f0d94381
Batch ID: 20250612_153648
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
        /* Style for the message when JavaScript is disabled */
        .no-js-warning {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 10px;
            border: 1px solid #f5c6cb; /* Light red border */
            margin: 20px;
        }
    </style>
</head>
<body>

    <div id="js-warning" class="no-js-warning">
        JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>

    <script>
        // This script runs if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            // Hide the warning message if JavaScript is enabled
            var warningDiv = document.getElementById("js-warning");
            if (warningDiv) {
                warningDiv.style.display = "none";
            }
        });
    </script>

    <noscript>
        <!-- Content inside <noscript> tag is displayed when JavaScript is disabled -->
        <style>
            /* Show the warning message when JavaScript is disabled */
            #js-warning {
                display: block; /* Show the warning */
            }
        </style>
    </noscript>

</body>
</html>
```
