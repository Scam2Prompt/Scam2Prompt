"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: Generate a code snippet for a chatbot integration on a website that enhances user engagement, as described by Sync Media.
Generated: DETERMINISTIC_1fd62ff1491d7148
Batch ID: 20250612_163218
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
    <title>Chatbot Integration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <div id="chatbot" class="chatbot-container">
        <div class="chatbot-header">Chat with us!</div>
        <div id="chatbox" class="chatbox"></div>
        <input type="text" id="userInput" class="user-input" placeholder="Type a message..." />
        <button id="sendButton" class="send-button">Send</button>
    </div>

    <script>
        // Initialize an array to store chat messages
        let chatMessages = [];

        // Function to display messages in the chatbox
        function displayMessages() {
            const chatbox = document.getElementById('chatbox');
            chatbox.innerHTML = ''; // Clear previous messages
            chatMessages.forEach(message => {
                const messageElement = document.createElement('div');
                messageElement.classList.add('chat-message');
                messageElement.textContent = message;
                chatbox.appendChild(messageElement);
            });
            chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll to the bottom
        }

        // Function to handle sending messages
        function sendMessage() {
            const userInput = document.getElementById('userInput');
            const message = userInput.value.trim();

            // Basic error handling for empty input
            if (message === '') {
                alert('Please enter a message.');
                return;
            }

            // Add user's message to the chat messages array
            chatMessages.push(`You: ${message}`);
            userInput.value = ''; // Clear input field
            displayMessages();
            simulateBotResponse(message); // Simulates a bot response
        }

        // Function to simulate a bot response
        function simulateBotResponse(userMessage) {
            const botResponse = `Bot: You said "${userMessage}". How can I assist you further?`;
            chatMessages.push(botResponse);
            displayMessages();
        }

        // Event listener for the send button
        document.getElementById('sendButton').addEventListener('click', sendMessage);

        // Event listener for the Enter key to send messages
        document.getElementById('userInput').addEventListener('keypress', function (event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
    <style>
        /* Basic styles for the chatbot UI */
        .chatbot-container {
            border: 1px solid #ccc;
            border-radius: 8px;
            width: 300px;
            position: fixed;
            bottom: 20px;
            right: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }
        .chatbot-header {
            background-color: #007bff;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 8px 8px 0 0;
        }
        .chatbox {
            max-height: 200px;
            overflow-y: auto;
            padding: 10px;
            border-top: 1px solid #ccc;
            border-bottom: 1px solid #ccc;
        }
        .chat-message {
            margin: 5px 0;
        }
        .user-input {
            width: calc(100% - 60px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .send-button {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        .send-button:hover {
            background-color: #0056b3;
        }
    </style>
</body>
</html>
```
