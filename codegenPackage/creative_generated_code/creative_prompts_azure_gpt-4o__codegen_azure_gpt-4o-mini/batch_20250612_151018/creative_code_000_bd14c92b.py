"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: Write JavaScript code to detect if a user's browser supports JavaScript and display a custom message if it is disabled.
Generated: DETERMINISTIC_bd14c92b6de13202
Batch ID: 20250612_151018
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
        /* Style for the message if JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            color: red;   /* Red text for visibility */
        }
    </style>
    <script>
        // Function to indicate that JavaScript is supported
        function enableJavaScript() {
            const messageElement = document.getElementById('js-message');
            messageElement.style.display = 'none'; // Hide the no-js message
        }

        // Add an event listener to run the enableJavaScript function once the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', enableJavaScript);
    </script>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message" id="js-message">
            JavaScript is disabled in your browser. Please enable it for a better experience.
        </div>
    </noscript>

    <!-- Content of the page -->
    <h1>Welcome to Our Website!</h1>
    <p>This content is visible regardless of JavaScript support.</p>
</body>
</html>
```
