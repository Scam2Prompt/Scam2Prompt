"""
Generated Code Metadata:
========================
Original URL: https://bot12.cc
Prompt: Generate a basic HTML structure for a chatbot webpage that displays a "Please enable JavaScript to continue" message when JavaScript is disabled.
Generated: DETERMINISTIC_2bf072082b166510
Batch ID: 20250622_204816
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
    <title>Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }
        .container {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 90%;
        }
        .chatbot-container {
            display: none;
        }
        .no-js-message {
            color: #d32f2f;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <noscript>
            <div class="no-js-message">
                Please enable JavaScript to continue using this chatbot.
            </div>
        </noscript>
        
        <div class="chatbot-container" id="chatbot">
            <!-- Chatbot UI will be loaded here via JavaScript -->
            <h1>Chatbot</h1>
            <div id="chat-messages"></div>
            <input type="text" id="user-input" placeholder="Type your message...">
            <button id="send-button">Send</button>
        </div>
    </div>

    <script>
        // Show chatbot container when JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('chatbot').style.display = 'block';
        });
    </script>
</body>
</html>
```
