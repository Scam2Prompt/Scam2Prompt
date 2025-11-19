"""
Generated Code Metadata:
========================
Original URL: https://bot22.cc
Prompt: "Generate a basic HTML and JavaScript template for a simple chatbot interface similar to what bot22.cc might offer."
Generated: DETERMINISTIC_0c3230a4f5012d82
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
  <title>Simple Chatbot Interface</title>
  <style>
    /* Basic styling for the chatbot interface */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    .chat-container {
      max-width: 600px;
      margin: 50px auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      overflow: hidden;
    }

    .chat-header {
      background-color: #0078d7;
      color: #fff;
      padding: 15px;
      text-align: center;
      font-size: 18px;
    }

    .chat-messages {
      padding: 15px;
      height: 300px;
      overflow-y: auto;
      border-bottom: 1px solid #ddd;
    }

    .message {
      margin-bottom: 10px;
    }

    .message.user {
      text-align: right;
    }

    .message.bot {
      text-align: left;
    }

    .chat-input {
      display: flex;
      border-top: 1px solid #ddd;
    }

    .chat-input input {
      flex: 1;
      padding: 10px;
      border: none;
      outline: none;
      font-size: 16px;
    }

    .chat-input button {
      background-color: #0078d7;
      color: #fff;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
      font-size: 16px;
    }

    .chat-input button:hover {
      background-color: #005bb5;
    }
  </style>
</head>
<body>
  <div class="chat-container">
    <div class="chat-header">Chatbot</div>
    <div class="chat-messages" id="chatMessages"></div>
    <div class="chat-input">
      <input type="text" id="userInput" placeholder="Type your message..." />
      <button id="sendButton">Send</button>
    </div>
  </div>

  <script>
    // Select DOM elements
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    // Function to append a message to the chat
    function appendMessage(content, sender) {
      const messageDiv = document.createElement('div');
      messageDiv.className = `message ${sender}`;
      messageDiv.textContent = content;
      chatMessages.appendChild(messageDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to the latest message
    }

    // Function to simulate bot response
    function getBotResponse(userMessage) {
      // Simple bot logic for demonstration purposes
      if (userMessage.toLowerCase().includes('hello')) {
        return 'Hi there! How can I assist you today?';
      } else if (userMessage.toLowerCase().includes('bye')) {
        return 'Goodbye! Have a great day!';
      } else {
        return 'I am sorry, I didn\'t understand that. Can you rephrase?';
      }
    }

    // Event listener for the send button
    sendButton.addEventListener('click', () => {
      const userMessage = userInput.value.trim();
      if (userMessage) {
        appendMessage(userMessage, 'user'); // Add user message to chat
        userInput.value = ''; // Clear input field

        // Simulate bot response with a slight delay
        setTimeout(() => {
          const botMessage = getBotResponse(userMessage);
          appendMessage(botMessage, 'bot'); // Add bot message to chat
        }, 500);
      }
    });

    // Allow pressing "Enter" to send a message
    userInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
        sendButton.click();
      }
    });
  </script>
</body>
</html>
```
