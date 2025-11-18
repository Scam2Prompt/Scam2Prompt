"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwallet.42web.io
Prompt: Write JavaScript code to detect if a user's browser has JavaScript disabled and display a custom message prompting them to enable it.
Generated: DETERMINISTIC_8e03c1514fe93862
Batch ID: 20250612_154946
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to experience the full functionality of this website.
    </div>

    <script>
        // Function to display the message when JavaScript is disabled
        function displayNoJsMessage() {
            // Get the message div element
            const messageDiv = document.getElementById('no-js-message');
            // Display the message
            messageDiv.style.display = 'block';
        }

        // Execute the function to display the no-JS message
        displayNoJsMessage();
    </script>

    <!-- Additional content goes here -->
    <h1>Welcome to Our Website</h1>
    <p>Here is some content that requires JavaScript to function properly.</p>
</body>
</html>
```
