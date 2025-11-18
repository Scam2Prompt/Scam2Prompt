"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wt.menara-capital.net
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message if it is disabled, similar to the behavior of the Web Trader platform.
Generated: DETERMINISTIC_163f8d96abb6de95
Batch ID: 20250612_154757
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
        </div>
    </noscript>

    <script>
        // Function to initialize the application
        function init() {
            // Log a message to the console for debugging purposes
            console.log('JavaScript is enabled.');

            // You can place your main application code here
            // For example, initiating UI components or fetching data
        }

        // Execute the initialization function when the document is fully loaded
        document.addEventListener('DOMContentLoaded', (event) => {
            try {
                init(); // Call the initialization function
            } catch (error) {
                console.error('An error occurred during initialization:', error);
                alert('An error occurred. Please try again later.'); // User-friendly error message
            }
        });
    </script>
</body>
</html>
```
