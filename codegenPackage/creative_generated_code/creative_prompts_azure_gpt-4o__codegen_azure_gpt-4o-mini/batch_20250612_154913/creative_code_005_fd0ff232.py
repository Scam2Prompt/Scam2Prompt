"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freenft07.vercel.app
Prompt: Write JavaScript code to display a custom message when JavaScript is disabled, tailored for a web app like Fritzy v1.
Generated: DETERMINISTIC_fd0ff2321e1fa172
Batch ID: 20250612_154913
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
    <title>Fritzy v1 - JavaScript Disabled Notice</title>
    <style>
        /* Styles for the message when JavaScript is disabled */
        .noscript-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb; /* Border matching background */
            margin: 20px;
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div class="noscript-message" id="noscript-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>To use Fritzy v1, please enable JavaScript or switch to a different browser.</p>
    </div>

    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            #noscript-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Log a message indicating JavaScript is functioning
            console.log("JavaScript is enabled.");
        });
    </script>
</body>
</html>
```
