"""
Generated Code Metadata:
========================
Original URL: https://fannie.ai
Prompt: Generate code to create a simple chatbot interface similar to the one on fannie.ai, including a feature to enable JavaScript for the chatbot tool.
Generated: DETERMINISTIC_01cc44e2a8f5e65c
Batch ID: 20250622_210650
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
    <title>Simple Chatbot Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        #chat-container {
            width: 100%;
            max-width: 600px;
            margin: auto;
            border: 1px solid #ccc;
            border-radius: 5px;
            background: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        #messages {
            height: 400px;
            overflow-y: auto;
            padding: 10px;
            border-bottom: 1px solid #ccc;
        }
        .message {
            margin: 5px 0;
        }
        .user-message {
            text-align: right;
            color: blue;
        }
        .bot-message {
            text-align: left;
            color: green;
        }
        #input-container {
            display: flex;
            padding: 10px;
        }
        #user-input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        #send-button {
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        #send-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div id="chat-container">
    <div id="messages"></div>
    <div id="input-container">
        <input type="text" id="user-input" placeholder="Type your message..." />
        <button id="send-button">Send</button>
    </div>
</div>

<script>
    // Function to append messages to the chat window
    function appendMessage(text, sender) {
        const messagesDiv = document.getElementById('messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message ' + (sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = text;
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to the bottom
    }

    // Function to handle sending messages
    function sendMessage() {
        const userInput = document.getElementById('user-input');
        const messageText = userInput.value.trim();

        // Validate user input
        if (messageText === '') {
            alert('Please enter a message.');
            return;
        }

        // Append user message to chat
        appendMessage(messageText, 'user');
        userInput.value = ''; // Clear input field

        // Simulate bot response after a delay
        setTimeout(() => {
            const botResponse = getBotResponse(messageText);
            appendMessage(botResponse, 'bot');
        }, 1000);
    }

    // Function to generate a simple bot response
    function getBotResponse(userMessage) {
        // Basic responses based on user input
        const responses = {
            'hello': 'Hi there! How can I help you today?',
            'how are you?': 'I am just a bot, but thanks for asking!',
            'bye': 'Goodbye! Have a great day!',
        };

        // Return a response or a default message
        return responses[userMessage.toLowerCase()] || "I'm sorry, I don't understand that.";
    }

    // Event listener for the send button
    document.getElementById('send-button').addEventListener('click', sendMessage);

    // Event listener for the Enter key
    document.getElementById('user-input').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
</script>

</body>
</html>
```
