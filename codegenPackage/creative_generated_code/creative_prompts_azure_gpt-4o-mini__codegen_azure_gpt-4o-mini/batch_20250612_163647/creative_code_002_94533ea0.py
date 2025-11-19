"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tzt.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser for the Tzt application?
Generated: DETERMINISTIC_94533ea0de4f81fd
Batch ID: 20250612_163647
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
        /* Style for the no-JavaScript message */
        .no-js {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <noscript>
        <!-- Message to display if JavaScript is disabled -->
        <div class="no-js">
            JavaScript is disabled in your browser. Please enable it for the Tzt application to function properly.
        </div>
    </noscript>

    <script>
        // Function to display a message if JavaScript is enabled
        function displayJsEnabledMessage() {
            // Create a message container
            const messageContainer = document.createElement('div');
            messageContainer.textContent = 'JavaScript is enabled. Welcome to the Tzt application!';
            messageContainer.style.color = 'green';
            messageContainer.style.fontWeight = 'bold';

            // Append the message to the body
            document.body.appendChild(messageContainer);
        }

        // Execute the function to display message
        try {
            displayJsEnabledMessage();
        } catch (error) {
            console.error('Error displaying JavaScript enabled message:', error);
            // Optional: alert the user if there’s an issue
            alert('An error occurred while checking JavaScript support. Please refresh the page.');
        }
    </script>
</body>
</html>
```
