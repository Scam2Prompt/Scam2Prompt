"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message like the one on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_137aec55ec9f8b30
Batch ID: 20250612_154752
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles for the error message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <div class="no-js-message" id="no-js-message">
        <strong>Error:</strong> It seems that JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>

    <script>
        // Function to display the error message if JavaScript is disabled
        function showErrorMessage() {
            const errorMessage = document.getElementById('no-js-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // Execute the function to show the error message
        showErrorMessage();
    </script>

    <noscript>
        <!-- This block will be executed if JavaScript is disabled -->
        <style>
            /* Ensure the error message is displayed when JavaScript is disabled */
            #no-js-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>

</body>
</html>
```
