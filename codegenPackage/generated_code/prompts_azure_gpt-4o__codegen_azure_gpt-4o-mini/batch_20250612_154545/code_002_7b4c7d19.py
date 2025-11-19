"""
Generated Code Metadata:
========================
Original URL: https://ravitechworld.com
Prompt: Provide code examples for enabling and testing JavaScript functionality on a website, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_7b4c7d1958172b00
Batch ID: 20250612_154545
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
    <title>JavaScript Functionality Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>JavaScript Functionality Test</h1>
    <button id="testButton">Click Me!</button>
    <div id="result"></div>

    <script>
        // Function to display a message when the button is clicked
        function displayMessage() {
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = 'JavaScript is working correctly!';
        }

        // Function to handle errors
        function handleError(error) {
            console.error('An error occurred:', error);
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = 'An error occurred. Please check the console for details.';
        }

        // Event listener for the button click
        document.getElementById('testButton').addEventListener('click', () => {
            try {
                displayMessage();
            } catch (error) {
                handleError(error);
            }
        });

        // Check for modern browser compatibility
        if (!('addEventListener' in window)) {
            alert('Your browser does not support modern JavaScript features. Please update your browser.');
        }
    </script>
</body>
</html>
```
