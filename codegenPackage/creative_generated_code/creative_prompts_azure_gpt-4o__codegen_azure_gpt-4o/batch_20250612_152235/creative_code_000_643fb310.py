"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting users to enable it, similar to the functionality required for the FRONK web app.
Generated: DETERMINISTIC_643fb310228fdf60
Batch ID: 20250612_152235
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
        /* Styling for the fallback message when JavaScript is disabled */
        .no-js-message {
            display: none;
            font-family: Arial, sans-serif;
            font-size: 18px;
            color: red;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Fallback message for when JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use this application.
        </div>
    </noscript>

    <!-- Main content that depends on JavaScript -->
    <div id="app">
        <!-- Content will be dynamically loaded by JavaScript -->
    </div>

    <script>
        /**
         * Check if JavaScript is enabled.
         * If JavaScript is enabled, display the main content.
         */
        document.addEventListener('DOMContentLoaded', () => {
            try {
                // Select the main content container
                const appElement = document.getElementById('app');

                // Safeguard to ensure the element exists
                if (!appElement) {
                    console.error('Error: Main application container not found.');
                    return;
                }

                // Populate the app content
                appElement.innerHTML = '<h1>Welcome to the FRONK Web App!</h1>' +
                    '<p>JavaScript is enabled in your browser.</p>';

            } catch (error) {
                // Log any unexpected errors for debugging
                console.error('An error occurred while initializing the app:', error.message);
            }
        });
    </script>
</body>
</html>
```
