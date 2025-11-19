"""
Generated Code Metadata:
========================
Original URL: https://kraken.vip
Prompt: Design a basic live chat system using a library or API that can be integrated into a website, similar to the "Chat with a Live Person" feature mentioned on the webpage.
Generated: DETERMINISTIC_e41ff441952ba49a
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Live Chat System using Node.js and Socket.IO**
====================================================

**Server-side Code (Node.js)**
-----------------------------

```javascript
// Import required libraries
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

// Store online users
let onlineUsers = {};

// Store chat history
let chatHistory = [];

// Serve static files
app.use(express.static('public'));

// Handle new connections
io.on('connection', (socket) => {
  console.log('New connection established');

  // Handle user join
  socket.on('join', (username) => {
    onlineUsers[username] = socket.id;
    console.log(`${username} joined the chat`);

    // Send chat history to new user
    socket.emit('chatHistory', chatHistory);

    // Broadcast new user to all connected clients
    io.emit('newUser', username);
  });

  // Handle new message
  socket.on('newMessage', (message) => {
    const { username, text } = message;
    console.log(`${username}: ${text}`);

    // Store message in chat history
    chatHistory.push({ username, text });

    // Broadcast new message to all connected clients
    io.emit('newMessage', message);
  });

  // Handle user disconnection
  socket.on('disconnect', () => {
    console.log('User disconnected');

    // Find and remove disconnected user
    for (const username in onlineUsers) {
      if (onlineUsers[username] === socket.id) {
        delete onlineUsers[username];
        console.log(`${username} left the chat`);

        // Broadcast user left to all connected clients
        io.emit('userLeft', username);
        break;
      }
    }
  });
});

// Handle errors
process.on('uncaughtException', (err) => {
  console.error('Uncaught exception:', err);
});

// Start server
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
```

**Client-side Code (JavaScript)**
---------------------------------

```javascript
// Establish connection to server
const socket = io();

// Get DOM elements
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatLog = document.getElementById('chat-log');
const usernameInput = document.getElementById('username-input');
const joinButton = document.getElementById('join-button');

// Handle join button click
joinButton.addEventListener('click', () => {
  const username = usernameInput.value.trim();
  if (username) {
    socket.emit('join', username);
    usernameInput.style.display = 'none';
    joinButton.style.display = 'none';
    chatForm.style.display = 'block';
  }
});

// Handle form submission
chatForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const text = chatInput.value.trim();
  if (text) {
    const message = { username: document.getElementById('username').textContent, text };
    socket.emit('newMessage', message);
    chatInput.value = '';
  }
});

// Handle new message
socket.on('newMessage', (message) => {
  const { username, text } = message;
  const messageElement = document.createElement('div');
  messageElement.textContent = `${username}: ${text}`;
  chatLog.appendChild(messageElement);
});

// Handle chat history
socket.on('chatHistory', (chatHistory) => {
  chatHistory.forEach((message) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${message.username}: ${message.text}`;
    chatLog.appendChild(messageElement);
  });
});

// Handle new user
socket.on('newUser', (username) => {
  const messageElement = document.createElement('div');
  messageElement.textContent = `${username} joined the chat`;
  chatLog.appendChild(messageElement);
});

// Handle user left
socket.on('userLeft', (username) => {
  const messageElement = document.createElement('div');
  messageElement.textContent = `${username} left the chat`;
  chatLog.appendChild(messageElement);
});
```

**HTML**
--------

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Chat</title>
  <style>
    #chat-log {
      padding: 10px;
      border: 1px solid #ccc;
      height: 500px;
      overflow-y: auto;
    }
  </style>
</head>
<body>
  <input id="username-input" type="text" placeholder="Enter username">
  <button id="join-button">Join Chat</button>
  <form id="chat-form" style="display: none;">
    <input id="chat-input" type="text" placeholder="Type a message...">
    <button type="submit">Send</button>
  </form>
  <div id="chat-log"></div>
  <script src="/socket.io/socket.io.js"></script>
  <script>
    // Client-side code here
  </script>
</body>
</html>
```

**package.json**
----------------

```json
{
  "name": "live-chat",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "socket.io": "^4.1.2"
  }
}
```
