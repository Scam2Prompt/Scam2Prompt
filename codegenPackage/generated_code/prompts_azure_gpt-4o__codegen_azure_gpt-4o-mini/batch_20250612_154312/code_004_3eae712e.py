"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Write code for a JavaScript snippet that displays a custom error message when JavaScript is disabled, similar to the behavior described on the DogeAI website.
Generated: DETERMINISTIC_3eae712e5a38d7ae
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the error message */
        .error-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            border: 1px solid #f5c6cb; /* Red border */
            padding: 15px; /* Padding around the message */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div class="error-message" id="error-message">
        <strong>Error:</strong> JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to display the error message if JavaScript is disabled
        function showErrorMessage() {
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // Check if JavaScript is enabled
        if (typeof showErrorMessage === 'function') {
            // JavaScript is enabled, do nothing
        } else {
            // JavaScript is disabled, show the error message
            showErrorMessage();
        }
    </script>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            /* Ensure the error message is displayed when JavaScript is disabled */
            .error-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>

</body>
</html>
```
