"""
Generated Code Metadata:
========================
Original URL: https://monada.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message.
Generated: DETERMINISTIC_ab0436d31d9d639c
Batch ID: 20250612_154115
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
        /* Style for the error message */
        .error-message {
            display: none; /* Hide by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="error-message" id="js-error-message">
        JavaScript is disabled in your browser. Please enable it to use this site.
    </div>

    <script>
        // Function to show the error message if JavaScript is disabled
        function showErrorMessage() {
            const errorMessage = document.getElementById('js-error-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // Execute the function to show the error message
        showErrorMessage();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            #js-error-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>
</body>
</html>
```
