"""
Generated Code Metadata:
========================
Original URL: https://dcqey.com
Prompt: Given that dcqey.com seems to require JavaScript, can you write a basic example of how JavaScript can be used to create an interactive element on a webpage?
Generated: DETERMINISTIC_c71590944c3de86b
Batch ID: 20250622_211317
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
    <title>Interactive Element Example</title>
    <style>
        /* Basic styling for the button and message */
        #interactiveButton {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
        }

        #message {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>

    <h1>Interactive JavaScript Example</h1>
    <button id="interactiveButton">Click Me!</button>
    <div id="message"></div>

    <script>
        // Function to handle button click
        function handleButtonClick() {
            try {
                // Get the message div
                const messageDiv = document.getElementById('message');
                
                // Update the message content
                messageDiv.textContent = 'Button was clicked!';

                // Log the action to the console
                console.log('Button clicked successfully.');
            } catch (error) {
                // Handle any errors that occur during the button click
                console.error('An error occurred while handling the button click:', error);
            }
        }

        // Add event listener to the button
        document.getElementById('interactiveButton').addEventListener('click', handleButtonClick);
    </script>

</body>
</html>
```
