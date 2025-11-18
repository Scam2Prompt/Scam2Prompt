"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgo.web.app
Prompt: Create a JavaScript function that displays an error message if JavaScript is disabled, similar to the behavior of the Shibonk Gang web app.
Generated: DETERMINISTIC_f2ab85520672376d
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
    <title>Error Handling for Disabled JavaScript</title>
    <style>
        /* Styling for the error message */
        .error-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <!-- This message will be shown if JavaScript is disabled -->
    <div id="error-message" class="error-message">
        JavaScript is disabled in your browser. Please enable it to use this application.
    </div>

    <script>
        // Function to show the error message if JavaScript is disabled
        function showError() {
            const errorMessage = document.getElementById('error-message');
            if (errorMessage) {
                errorMessage.style.display = 'block'; // Show the error message
            } else {
                console.error('Error: Error message element not found.'); // Log error to console
            }
        }

        // Ensure this function is called when the script loads
        // In a production environment, this could be called based on certain conditions
        showError();
    </script>

    <!-- Fallback content for browsers with JavaScript disabled -->
    <noscript>
        <style>
            /* Ensure the error message is displayed when JavaScript is disabled */
            .error-message {
                display: block;
            }
        </style>
        <div class="error-message">
            JavaScript is disabled in your browser. Please enable it to use this application.
        </div>
    </noscript>
</body>
</html>
```
