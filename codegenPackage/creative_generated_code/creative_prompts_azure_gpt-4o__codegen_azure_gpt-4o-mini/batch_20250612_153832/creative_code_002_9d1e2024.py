"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defia.cc
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a custom message for "mining-h5."
Generated: DETERMINISTIC_9d1e20247c002709
Batch ID: 20250612_153832
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
        /* Style for the non-JavaScript message */
        .no-js-message {
            display: none; /* Hide by default */
            color: red; /* Message color */
            font-weight: bold; /* Make message bold */
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <script>
        // This script runs if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Hide the no-JS message if JS is enabled
            const noJsMessage = document.getElementById("no-js-message");
            noJsMessage.style.display = "none"; // Hide the message
        });
    </script>

    <!-- Fallback for users with JavaScript disabled -->
    <noscript>
        <style>
            /* Styles to show the message if JS is disabled */
            .no-js-message {
                display: block; /* Show the message */
            }
        </style>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use this application.
        </div>
    </noscript>

</body>
</html>
```
