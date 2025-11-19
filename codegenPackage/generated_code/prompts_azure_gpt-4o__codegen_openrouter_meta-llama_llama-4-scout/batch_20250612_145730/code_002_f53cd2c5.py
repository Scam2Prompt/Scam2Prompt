"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: Generate code using JavaScript to implement a live chat feature for customer support on an online gambling site, similar to the one mentioned on PANSOS4D.
Generated: DETERMINISTIC_f53cd2c565274e27
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// live-chat.js

/**
 * Live Chat Feature for Customer Support
 * =======================================
 */

// Import required libraries
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/live-chat', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define the chat message schema
const chatMessageSchema = new mongoose.Schema({
  username: String,
  message: String,
  timestamp: Date
});

// Create a model for chat messages
const ChatMessage = mongoose.model('ChatMessage', chatMessageSchema);

// Serve static files from the public directory
app.use(express.static('public'));

// Handle new connections
io.on('connection', (socket) => {
  console.log('New connection established');

  // Handle disconnection
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });

  // Handle new chat message
  socket.on('new-message', (data) => {
    const { username, message } = data;

    // Validate input data
    if (!username || !message) {
      console.error('Invalid chat message data');
      return;
    }

    // Create a new chat message
    const chatMessage = new ChatMessage({
      username,
      message,
      timestamp: new Date()
    });

    // Save the chat message to MongoDB
    chatMessage.save((err) => {
      if (err) {
        console.error('Error saving chat message:', err);
        return;
      }

      // Broadcast the new chat message to all connected users
      io.emit('new-message', chatMessage);
    });
  });
});

// Get all chat messages
app.get('/api/chat-messages', async (req, res) => {
  try {
    const chatMessages = await ChatMessage.find().sort({ timestamp: 1 });
    res.json(chatMessages);
  } catch (err) {
    console.error('Error fetching chat messages:', err);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
const port = 3000;
http.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```javascript
// public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Chat</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    #chat-log {
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      width: 500px;
      height: 600px;
      overflow-y: auto;
    }
  </style>
</head>
<body>
  <h1>Live Chat</h1>
  <div id="chat-log"></div>
  <input id="username" type="text" placeholder="Username">
  <input id="message" type="text" placeholder="Message">
  <button id="send-btn">Send</button>

  <script src="/socket.io/socket.io.js"></script>
  <script>
    const socket = io();

    // Get chat log and input elements
    const chatLog = document.getElementById('chat-log');
    const usernameInput = document.getElementById('username');
    const messageInput = document.getElementById('message');
    const sendBtn = document.getElementById('send-btn');

    // Fetch chat messages on page load
    fetch('/api/chat-messages')
      .then((res) => res.json())
      .then((chatMessages) => {
        chatMessages.forEach((chatMessage) => {
          const messageHTML = `
            <p><strong>${chatMessage.username}:</strong> ${chatMessage.message}</p>
          `;
          chatLog.innerHTML += messageHTML;
        });
      })
      .catch((err) => console.error('Error fetching chat messages:', err));

    // Handle send button click
    sendBtn.addEventListener('click', () => {
      const username = usernameInput.value.trim();
      const message = messageInput.value.trim();

      // Validate input data
      if (!username || !message) {
        console.error('Invalid chat message data');
        return;
      }

      // Send new chat message to server
      socket.emit('new-message', { username, message });

      // Clear input fields
      messageInput.value = '';
    });

    // Handle new chat message from server
    socket.on('new-message', (chatMessage) => {
      const messageHTML = `
        <p><strong>${chatMessage.username}:</strong> ${chatMessage.message}</p>
      `;
      chatLog.innerHTML += messageHTML;
      chatLog.scrollTop = chatLog.scrollHeight;
    });
  </script>
</body>
</html>
```
