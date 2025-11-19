"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddgghb.pages.dev
Prompt: What are the best practices for ensuring JavaScript is enabled on a web page?
Generated: DETERMINISTIC_f5471d4544a1c8fe
Batch ID: 20250612_163541
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
        /* Styles for the no-JS message */
        .no-js {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div class="no-js">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>

    <script>
        // Function to handle the absence of JavaScript
        function displayNoJsMessage() {
            const noJsMessage = document.querySelector('.no-js');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message if JavaScript is disabled
            }
        }

        // Example of a function that requires JavaScript
        function initApp() {
            console.log('JavaScript is enabled. Initializing application.');
            // Application initialization code goes here
        }

        // Check if JavaScript is enabled and execute the app initialization
        try {
            initApp(); // Attempt to run the app initialization
        } catch (error) {
            console.error('An error occurred during initialization:', error);
            displayNoJsMessage(); // Fallback to show no-JS message in case of error
        }
    </script>
</body>
</html>
```
