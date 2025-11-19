"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Develop a code snippet that integrates a customer support chatbot for a website like Bio Green Asia, which offers 24/7 support for natural cleaning and beauty products.
Generated: DETERMINISTIC_de2d37e95dab37a1
Batch ID: 20250612_163924
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
    <title>Bio Green Asia Support Chatbot</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <div id="chatbot" class="chatbot-container">
        <div class="chatbot-header">
            <h2>Support Chatbot</h2>
            <button id="close-chat" aria-label="Close Chat">×</button>
        </div>
        <div id="chat-window" class="chat-window">
            <div id="messages" class="messages"></div>
            <input type="text" id="user-input" placeholder="Type your message here..." aria-label="User message" />
            <button id="send-button" aria-label="Send Message">Send</button>
        </div>
    </div>

    <button id="open-chat" aria-label="Open Chat">Chat with us!</button>

    <script>
        // Selectors for DOM elements
        const chatbot = document.getElementById('chatbot');
        const messages = document.getElementById('messages');
        const userInput = document.getElementById('user-input');
        const sendButton = document.getElementById('send-button');
        const openChatButton = document.getElementById('open-chat');
        const closeChatButton = document.getElementById('close-chat');

        // Open chatbot on button click
        openChatButton.onclick = () => {
            chatbot.style.display = 'block';
            userInput.focus();
        };

        // Close chatbot
        closeChatButton.onclick = () => {
            chatbot.style.display = 'none';
        };

        // Function to handle sending messages
        function sendMessage() {
            const messageText = userInput.value.trim();
            if (messageText) {
                // Display user's message
                appendMessage('User', messageText);
                userInput.value = ''; // Clear input field
                // Simulate a bot response (replace with actual API call)
                setTimeout(() => {
                    appendMessage('Bot', generateBotResponse(messageText));
                }, 1000);
            }
        }

        // Function to append messages to the chat window
        function appendMessage(sender, text) {
            const messageElement = document.createElement('div');
            messageElement.className = sender === 'User' ? 'user-message' : 'bot-message';
            messageElement.textContent = `${sender}: ${text}`;
            messages.appendChild(messageElement);
            messages.scrollTop = messages.scrollHeight; // Scroll to latest message
        }

        // Simple bot response simulation (replace with actual logic)
        function generateBotResponse(userMessage) {
            // Basic keyword detection for demo purposes
            if (userMessage.toLowerCase().includes('cleaning')) {
                return 'We offer a variety of natural cleaning products. How can I assist you?';
            } else if (userMessage.toLowerCase().includes('beauty')) {
                return 'Check out our range of beauty products. What would you like to know?';
            } else {
                return 'I am here to help! Please ask me anything about our products.';
            }
        }

        // Event listener for 'send' button and 'Enter' key
        sendButton.onclick = sendMessage;
        userInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
    <style>
        /* Basic styles for the chatbot interface */
        .chatbot-container {
            position: fixed;
            bottom: 0;
            right: 20px;
            width: 300px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: none; /* Hidden by default */
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .chatbot-header {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .chat-window {
            padding: 10px;
            height: 300px;
            overflow-y: auto;
        }
        .messages {
            margin-bottom: 10px;
        }
        .user-message {
            text-align: right;
            color: blue;
        }
        .bot-message {
            text-align: left;
            color: green;
        }
        input[type="text"] {
            width: calc(100% - 60px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            border: none;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</body>
</html>
```
