"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ribbons.bond
Prompt: Generate code to detect if MetaMask is installed and enabled in a browser, and display an error message if JavaScript is disabled.
Generated: DETERMINISTIC_25fcb91cfc13236c
Batch ID: 20250612_155042
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
    <title>MetaMask Detection</title>
    <style>
        /* Basic styling for the error message */
        #error-message {
            display: none;
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="error-message">JavaScript is disabled in your browser. Please enable it to use this application.</div>
    <script>
        // Function to check if MetaMask is installed and enabled
        function detectMetaMask() {
            // Check if window.ethereum is available
            if (typeof window.ethereum !== 'undefined') {
                console.log('MetaMask is installed and enabled.');
                // You can proceed with your application logic here
            } else {
                console.error('MetaMask is not installed or enabled.');
                alert('Please install MetaMask to use this application.');
            }
        }

        // Function to display an error message if JavaScript is disabled
        function showError() {
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'block'; // Show error message
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', () => {
            // Run MetaMask detection
            detectMetaMask();
        });

        // Fallback for JavaScript disabled scenario
        window.onload = function() {
            // If JavaScript is disabled, this will still run to show an error message
            showError();
        };
    </script>
</body>
</html>
```
