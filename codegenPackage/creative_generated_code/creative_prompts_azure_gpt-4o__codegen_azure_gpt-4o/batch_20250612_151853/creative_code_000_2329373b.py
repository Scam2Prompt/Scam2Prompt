"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the functionality described on the "debridge.global-connect.eu" domain details page.
Generated: DETERMINISTIC_2329373b831d3884
Batch ID: 20250612_151853
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
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            color: red;
            font-size: 18px;
            text-align: center;
            margin: 20px;
            display: none; /* Hidden by default, only shown if JavaScript is disabled */
        }
    </style>
</head>
<body>
    <!-- Fallback message for browsers with JavaScript disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript to view this page properly.
        </div>
    </noscript>

    <!-- Main content for browsers with JavaScript enabled -->
    <div id="js-enabled-content">
        <h1>Welcome to the Website</h1>
        <p>JavaScript is enabled in your browser. Enjoy your stay!</p>
    </div>

    <script>
        // Ensure JavaScript-enabled content is visible
        document.addEventListener('DOMContentLoaded', () => {
            try {
                // Select the main content area
                const jsEnabledContent = document.getElementById('js-enabled-content');

                // Display the content when JavaScript is enabled
                if (jsEnabledContent) {
                    jsEnabledContent.style.display = 'block';
                }
            } catch (error) {
                // Log any unexpected error to the console
                console.error('An error occurred while checking JavaScript status:', error);
            }
        });
    </script>
</body>
</html>
```
