"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Write a script to display a custom error message if a user tries to access a web app without enabling JavaScript, similar to the Honey App's requirement.
Generated: DETERMINISTIC_7cfb9939a0641ea0
Batch ID: 20250612_153401
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
    <title>JavaScript Required</title>
    <style>
        /* Style for the error message */
        #js-error-message {
            display: none; /* Hidden by default */
            text-align: center;
            padding: 20px;
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            font-size: 18px; /* Font size */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <div id="js-error-message">
        <h1>JavaScript is Disabled</h1>
        <p>This web application requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
    </div>

    <script>
        // Function to display the error message
        function displayErrorMessage() {
            const errorMessage = document.getElementById('js-error-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // Check if JavaScript is enabled
        window.onload = function() {
            // If JavaScript is working, hide the error message
            const errorMessage = document.getElementById('js-error-message');
            errorMessage.style.display = 'none'; // Hide the error message
        };
    </script>

    <!-- Fallback content for non-JavaScript users -->
    <noscript>
        <style>
            /* Ensures the error message is visible if JavaScript is disabled */
            #js-error-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>

</body>
</html>
```
