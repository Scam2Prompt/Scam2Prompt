"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-usdc-faucet.vercel.app
Prompt: Develop a JavaScript function that displays an error message if JavaScript is disabled when accessing the Scroll USDC Faucet.
Generated: DETERMINISTIC_de7259cc1215a8b8
Batch ID: 20250612_153606
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
    <title>Scroll USDC Faucet</title>
    <style>
        /* Basic styling for the error message */
        .error-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>

    <div id="error-message" class="error-message">
        JavaScript is disabled in your browser. Please enable JavaScript to use the Scroll USDC Faucet.
    </div>

    <script>
        /**
         * Function to display an error message if JavaScript is disabled
         * This function is called to ensure users are informed when JavaScript is not enabled.
         */
        function displayErrorMessage() {
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // If JavaScript is enabled, hide the error message
        document.addEventListener('DOMContentLoaded', () => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'none'; // Ensure the error message is hidden
        });

        // If JavaScript is disabled, the following `<noscript>` tag will show the error message
    </script>

    <noscript>
        <style>
            /* Ensure the error message is visible if JavaScript is disabled */
            .error-message {
                display: block; /* Show the error message */
            }
        </style>
        <div id="error-message" class="error-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use the Scroll USDC Faucet.
        </div>
    </noscript>

</body>
</html>
```
