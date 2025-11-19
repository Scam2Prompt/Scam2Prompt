"""
Generated Code Metadata:
========================
Original URL: https://agodarentacar.com
Prompt: Develop a Node.js script to integrate a 24/7 online chat support feature similar to Agoda RentACar's red chat bubble functionality.
Generated: DETERMINISTIC_5358864d48de0ef1
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// chat-support.js

/**
 * 24/7 Online Chat Support Feature
 * 
 * This script integrates a basic online chat support feature similar to Agoda RentACar's red chat bubble functionality.
 * 
 * @author [Your Name]
 */

// Import required modules
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/chat-support', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define chat message schema
const chatMessageSchema = new mongoose.Schema({
    username: String,
    message: String,
    timestamp: Date
});

// Create chat message model
const ChatMessage = mongoose.model('ChatMessage', chatMessageSchema);

// Serve static files
app.use(express.static('public'));

// Handle socket connections
io.on('connection', (socket) => {
    console.log('Client connected');

    // Handle new chat message
    socket.on('new-message', (data) => {
        const chatMessage = new ChatMessage({
            username: data.username,
            message: data.message,
            timestamp: new Date()
        });

        // Save chat message to database
        chatMessage.save((err) => {
            if (err) {
                console.error('Error saving chat message:', err);
                socket.emit('error', 'Failed to send message');
            } else {
                // Broadcast new chat message to all connected clients
                io.emit('new-message', data);
            }
        });
    });

    // Handle client disconnection
    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

// Handle HTTP requests
app.get('/chat-history', async (req, res) => {
    try {
        const chatHistory = await ChatMessage.find().sort({ timestamp: 1 });
        res.json(chatHistory);
    } catch (err) {
        console.error('Error retrieving chat history:', err);
        res.status(500).json({ error: 'Failed to retrieve chat history' });
    }
});

// Start server
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
    <title>24/7 Online Chat Support</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #chat-container {
            width: 300px;
            height: 400px;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-y: auto;
        }
        #chat-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div id="chat-container"></div>
    <input id="chat-input" type="text" placeholder="Type a message...">
    <button id="send-btn">Send</button>

    <script src="/socket.io/socket.io.js"></script>
    <script>
        const socket = io();

        // Get chat history on page load
        fetch('/chat-history')
            .then((res) => res.json())
            .then((chatHistory) => {
                const chatContainer = document.getElementById('chat-container');
                chatHistory.forEach((message) => {
                    const messageElement = document.createElement('div');
                    messageElement.textContent = `${message.username}: ${message.message}`;
                    chatContainer.appendChild(messageElement);
                });
            })
            .catch((err) => console.error('Error retrieving chat history:', err));

        // Handle send button click
        document.getElementById('send-btn').addEventListener('click', () => {
            const chatInput = document.getElementById('chat-input');
            const message = chatInput.value.trim();
            if (message) {
                const data = {
                    username: 'You',
                    message: message
                };
                socket.emit('new-message', data);
                chatInput.value = '';
            }
        });

        // Handle new chat message
        socket.on('new-message', (data) => {
            const chatContainer = document.getElementById('chat-container');
            const messageElement = document.createElement('div');
            messageElement.textContent = `${data.username}: ${data.message}`;
            chatContainer.appendChild(messageElement);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        });

        // Handle error
        socket.on('error', (error) => {
            console.error('Error:', error);
        });
    </script>
</body>
</html>
```
