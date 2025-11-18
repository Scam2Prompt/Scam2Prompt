"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the Webmail login page of https://webmail.everclear.pk.
Generated: DETERMINISTIC_6f4a62cffe5f1077
Batch ID: 20250612_153447
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
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Border color */
            padding: 10px;
            margin: 10px 0;
            font-family: Arial, sans-serif;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <!-- Warning message container -->
    <noscript>
        <!-- Fallback for when JavaScript is disabled -->
        <div id="js-warning">
            Warning: JavaScript is disabled in your browser. This website requires JavaScript for full functionality. Please enable JavaScript to proceed.
        </div>
    </noscript>

    <script>
        // JavaScript code runs only if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Hide the warning message if JavaScript is enabled
                const warningElement = document.getElementById("js-warning");
                if (warningElement) {
                    warningElement.style.display = "none"; // Ensure it stays hidden
                }
            } catch (error) {
                console.error("An error occurred while handling the JavaScript detection:", error);
            }
        });
    </script>
</body>
</html>
```
