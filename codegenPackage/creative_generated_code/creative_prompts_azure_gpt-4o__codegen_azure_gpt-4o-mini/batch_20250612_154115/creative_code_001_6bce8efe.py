"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Recommend a library or API to dynamically enable JavaScript functionality for a web application that displays an error when JavaScript is disabled.
Generated: DETERMINISTIC_6bce8efe2fd1a346
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
    <title>Dynamic JavaScript Functionality</title>
    <style>
        /* Basic styles for the error message */
        .no-js-alert {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <style>
            .no-js-alert {
                display: block; /* Show the alert if JS is disabled */
            }
        </style>
        <div class="no-js-alert">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>
</head>
<body>
    <div id="content">
        <h1>Welcome to Our Web Application</h1>
        <p>This application uses JavaScript to enhance functionality.</p>
        <button id="dynamicButton">Click Me</button>
        <div id="message"></div>
    </div>

    <script>
        // Function to handle button click event
        function handleButtonClick() {
            try {
                const messageDiv = document.getElementById('message');
                messageDiv.textContent = 'Button clicked! JavaScript is working.';
            } catch (error) {
                console.error('Error handling button click:', error);
                alert('An error occurred while processing your request.');
            }
        }

        // Adding event listener to the button
        document.getElementById('dynamicButton').addEventListener('click', handleButtonClick);
    </script>
</body>
</html>
```
