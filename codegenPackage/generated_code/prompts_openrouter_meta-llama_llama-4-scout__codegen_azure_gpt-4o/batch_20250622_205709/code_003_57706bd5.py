"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-io.web.app
Prompt: Design a basic user interface for ScottyChat, the AI-powered crypto companion, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_57706bd54f0b859f
Batch ID: 20250622_205709
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
  <title>ScottyChat - AI Crypto Companion</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Main container for the chat application -->
  <div id="scottyChatApp">
    <!-- Header section -->
    <header class="chat-header">
      <h1>ScottyChat</h1>
      <p>Your AI-powered crypto companion</p>
    </header>

    <!-- Chat window -->
    <div id="chatWindow" class="chat-window">
      <!-- Messages will be dynamically added here -->
    </div>

    <!-- Input section -->
    <div class="chat-input-container">
      <input 
        type="text" 
        id="userInput" 
        placeholder="Type your message here..." 
        class="chat-input"
      />
      <button id="sendButton" class="send-button">Send</button>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General reset for consistent styling */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  color: #333;
}

/* Main container styling */
#scottyChatApp {
  max-width: 600px;
  margin: 50px auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* Header styling */
.chat-header {
  background-color: #4caf50;
  color: #fff;
  text-align: center;
  padding: 20px;
}

.chat-header h1 {
  margin: 0;
  font-size: 24px;
}

.chat-header p {
  margin: 5px 0 0;
  font-size: 14px;
}

/* Chat window styling */
.chat-window {
  height: 400px;
  overflow-y: auto;
  padding: 10px;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}

/* Chat input container styling */
.chat-input-container {
  display: flex;
  padding: 10px;
}

.chat-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.send-button {
  margin-left: 10px;
  padding: 10px 20px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.send-button:hover {
  background-color: #45a049;
}

/* Message styling */
.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 4px;
}

.message.user {
  background-color: #e0f7fa;
  text-align: right;
}

.message.bot {
  background-color: #f1f8e9;
  text-align: left;
}
```

```javascript
// script.js

// Select DOM elements
const chatWindow = document.getElementById('chatWindow');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

// Function to add a message to the chat window
function addMessage(content, sender) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.textContent = content;
  chatWindow.appendChild(messageElement);

  // Scroll to the bottom of the chat window
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Function to handle sending a message
function sendMessage() {
  const userMessage = userInput.value.trim();

  // Validate input
  if (!userMessage) {
    alert('Please enter a message.');
    return;
  }

  // Add user's message to the chat window
  addMessage(userMessage, 'user');

  // Clear the input field
  userInput.value = '';

  // Simulate bot response (replace with actual AI integration)
  setTimeout(() => {
    const botResponse = `You said: "${userMessage}". How can I assist you with crypto?`;
    addMessage(botResponse, 'bot');
  }, 1000);
}

// Event listener for the send button
sendButton.addEventListener('click', sendMessage);

// Event listener for Enter key
userInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});
```
