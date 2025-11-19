"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Can you provide a code example for implementing the Fannie AI chatbot on a web page?
Generated: DETERMINISTIC_ab3160da348c1094
Batch ID: 20250612_162050
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
  <title>Fannie AI Chatbot</title>
  <style>
    /* Basic styling for the chatbot UI */
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
    #chatbot-container {
      width: 400px;
      height: 600px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      background-color: #fff;
      display: flex;
      flex-direction: column;
    }
    #chat-log {
      flex: 1;
      padding: 10px;
      overflow-y: auto;
      border-bottom: 1px solid #ddd;
    }
    #chat-log p {
      margin: 0;
      padding: 8px;
      border-radius: 5px;
    }
    #chat-log .user-message {
      background-color: #e1f5fe;
      text-align: right;
    }
    #chat-log .bot-message {
      background-color: #ffe0e0;
      text-align: left;
    }
    #user-input-container {
      display: flex;
      padding: 10px;
    }
    #user-input {
      flex: 1;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
    #submit-button {
      margin-left: 10px;
      padding: 8px 16px;
      border: none;
      background-color: #0288d1;
      color: #fff;
      border-radius: 5px;
      cursor: pointer;
    }
    #submit-button:hover {
      background-color: #0277bd;
    }
  </style>
</head>
<body>
  <div id="chatbot-container">
    <div id="chat-log"></div>
    <div id="user-input-container">
      <input type="text" id="user-input" placeholder="Type your message..." />
      <button id="submit-button">Send</button>
    </div>
  </div>

  <script>
    // Chatbot logic
    document.addEventListener('DOMContentLoaded', () => {
      const chatLog = document.getElementById('chat-log');
      const userInput = document.getElementById('user-input');
      const submitButton = document.getElementById('submit-button');

      // Function to append messages to the chat log
      const appendMessage = (message, sender) => {
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        messageElement.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
        chatLog.appendChild(messageElement);
        chatLog.scrollTop = chatLog.scrollHeight; // Auto-scroll to the latest message
      };

      // Function to simulate the Fannie AI chatbot response
      const getBotResponse = (userMessage) => {
        // Example responses for a simple chatbot
        const responses = {
          'hello': 'Hi there! How can I assist you today?',
          'how are you?': 'I\'m just a chatbot, but I\'m here to help!',
          'bye': 'Goodbye! Have a great day!'
        };
        return responses[userMessage.toLowerCase()] || 'Sorry, I didn\'t understand that. Can you rephrase?';
      };

      // Event listener for the submit button
      submitButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
          // Append the user's message
          appendMessage(userMessage, 'user');
          userInput.value = ''; // Clear input field

          // Simulate bot response with a slight delay
          setTimeout(() => {
            const botResponse = getBotResponse(userMessage);
            appendMessage(botResponse, 'bot');
          }, 500);
        }
      });

      // Enable "Enter" key to send messages
      userInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
          submitButton.click();
        }
      });
    });
  </script>
</body>
</html>
```
