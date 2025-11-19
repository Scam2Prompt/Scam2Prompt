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
        /* Basic styling for the chatbot container */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        .chatbot-container {
            width: 100%;
            max-width: 400px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .chat-header {
            background-color: #0078d7;
            color: #fff;
            padding: 10px;
            text-align: center;
            font-size: 18px;
        }

        .chat-body {
            padding: 20px;
            height: 300px;
            overflow-y: auto;
        }

        .chat-footer {
            padding: 10px;
            border-top: 1px solid #ddd;
            display: flex;
            gap: 10px;
        }

        .chat-footer input {
            flex: 1;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .chat-footer button {
            padding: 8px 12px;
            background-color: #0078d7;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .chat-footer button:hover {
            background-color: #005fa3;
        }

        /* Message displayed when JavaScript is disabled */
        .no-js-message {
            text-align: center;
            color: #ff0000;
            font-size: 16px;
            padding: 20px;
        }
    </style>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            Please enable JavaScript to continue.
        </div>
    </noscript>

    <!-- Chatbot container -->
    <div class="chatbot-container">
        <div class="chat-header">
            Chatbot
        </div>
        <div class="chat-body" id="chat-body">
            <!-- Chat messages will be dynamically added here -->
        </div>
        <div class="chat-footer">
            <input type="text" id="user-input" placeholder="Type your message..." />
            <button id="send-button">Send</button>
        </div>
    </div>

    <script>
        // JavaScript code for chatbot functionality

        // Select DOM elements
        const chatBody = document.getElementById('chat-body');
        const userInput = document.getElementById('user-input');
        const sendButton = document.getElementById('send-button');

        // Function to add a message to the chat
        function addMessage(message, sender = 'user') {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            messageElement.style.marginBottom = '10px';
            messageElement.style.padding = '10px';
            messageElement.style.borderRadius = '4px';
            messageElement.style.maxWidth = '80%';

            if (sender === 'user') {
                messageElement.style.backgroundColor = '#0078d7';
                messageElement.style.color = '#fff';
                messageElement.style.alignSelf = 'flex-end';
            } else {
                messageElement.style.backgroundColor = '#f4f4f4';
                messageElement.style.color = '#000';
                messageElement.style.alignSelf = 'flex-start';
            }

            chatBody.appendChild(messageElement);
            chatBody.scrollTop = chatBody.scrollHeight; // Scroll to the bottom
        }

        // Event listener for the send button
        sendButton.addEventListener('click', () => {
            const message = userInput.value.trim();
            if (message) {
                addMessage(message, 'user'); // Add user message
                userInput.value = ''; // Clear input field

                // Simulate chatbot response
                setTimeout(() => {
                    addMessage('Hello! How can I assist you today?', 'bot');
                }, 1000);
            }
        });

        // Allow pressing Enter to send a message
        userInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                sendButton.click();
            }
        });
    </script>
</body>
</html>
```
