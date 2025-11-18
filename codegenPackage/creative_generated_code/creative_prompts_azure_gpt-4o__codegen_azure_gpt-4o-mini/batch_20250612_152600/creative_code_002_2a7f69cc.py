"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethplo.com
Prompt: Generate code to enable JavaScript detection and display a custom message if JavaScript is disabled on a cryptocurrency pledging website.
Generated: DETERMINISTIC_2a7f69cc2d2e9244
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
    <title>Cryptocurrency Pledging</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            font-size: 1.2em;
            color: red;
            margin: 20px;
        }
        /* Style for the message when JavaScript is enabled */
        .js-message {
            display: block; /* Show by default when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the best experience on our cryptocurrency pledging website.
        </div>
    </noscript>

    <div class="js-message">
        <!-- This content will be shown only if JavaScript is enabled -->
        <h1>Welcome to the Cryptocurrency Pledging Site!</h1>
        <p>Your support helps us grow the community and improve the platform.</p>
        <!-- More content can go here -->
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Log a message to the console for debugging purposes
            console.log("JavaScript is enabled.");

            // Additional JavaScript functionality can be initialized here
        });
    </script>

</body>
</html>
```
