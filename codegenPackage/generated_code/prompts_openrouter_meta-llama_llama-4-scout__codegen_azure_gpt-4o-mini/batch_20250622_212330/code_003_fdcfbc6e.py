"""
Generated Code Metadata:
========================
Original URL: https://softegypt.org
Prompt: Create a simple webpage using JavaScript, HTML, and CSS that displays a message in Arabic, like "القادم أفضل!".
Generated: DETERMINISTIC_fdcfbc6e2b48ef39
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>رسالة إيجابية</title>
    <style>
        /* Basic styling for the body and message */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            margin: 0;
        }
        .message {
            font-size: 2em;
            color: #4CAF50; /* Green color for the message */
            text-align: center;
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div class="message" id="message"></div>

    <script>
        // Function to display a message in Arabic
        function displayMessage() {
            try {
                const messageElement = document.getElementById('message');
                const message = "القادم أفضل!"; // Positive message in Arabic
                messageElement.textContent = message; // Set the message text
            } catch (error) {
                console.error("Error displaying message:", error); // Log any errors
            }
        }

        // Call the function to display the message when the page loads
        window.onload = displayMessage;
    </script>
</body>
</html>
```
