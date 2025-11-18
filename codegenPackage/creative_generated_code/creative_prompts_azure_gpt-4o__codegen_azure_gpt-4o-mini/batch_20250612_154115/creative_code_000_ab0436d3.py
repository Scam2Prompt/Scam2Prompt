"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom error message.
Generated: DETERMINISTIC_ab0436d31d9d639c
Batch ID: 20250612_154115
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
        /* Style to initially hide the error message */
        .js-disabled {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <!-- Custom error message for users with JavaScript disabled -->
    <div class="js-disabled" id="jsDisabledMessage">
        JavaScript is disabled in your browser. Please enable JavaScript to use this site.
    </div>

    <!-- Main content of the page -->
    <div id="mainContent">
        <h1>Welcome to Our Website!</h1>
        <p>This content is only visible if JavaScript is enabled.</p>
    </div>

    <script>
        // Function to show the message if JavaScript is enabled
        function enableJavaScript() {
            // Hide the error message if JavaScript is running
            const jsDisabledMessage = document.getElementById('jsDisabledMessage');
            jsDisabledMessage.style.display = 'none';

            // Show the main content
            const mainContent = document.getElementById('mainContent');
            mainContent.style.display = 'block';
        }

        // Event listener for DOM content loaded
        document.addEventListener('DOMContentLoaded', () => {
            try {
                // Execute function to show content
                enableJavaScript();
            } catch (error) {
                // Log error to console for debugging
                console.error('An error occurred while enabling JavaScript:', error);
            }
        });

        // Ensure that the main content is hidden initially
        document.getElementById('mainContent').style.display = 'none';
    </script>
</body>
</html>
```
