"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc106.d952.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the behavior of the "mining-h5" platform.
Generated: DETERMINISTIC_1a275ed4cb105c5d
Batch ID: 20250612_154737
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
        /* Style for the JavaScript disabled message */
        .js-disabled {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <style>
            /* Style for when JavaScript is disabled */
            .js-disabled {
                display: block; /* Show when JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div class="js-disabled">
        <strong>JavaScript is disabled in your browser.</strong><br>
        Please enable JavaScript to use this website's features.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            console.log("JavaScript is enabled."); // Log to console for debugging
        }

        // Execute the function to confirm JavaScript is running
        try {
            checkJavaScript();
        } catch (error) {
            console.error("An error occurred while checking JavaScript: ", error);
            // In production, consider notifying the user or logging the error
        }
    </script>
</body>
</html>
```
