"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Generate a code snippet in JavaScript to implement a live chat feature, similar to the one offered by Pelangi189, using WebSockets or a similar technology.
Generated: DETERMINISTIC_a1bb7ae69f5e460c
Batch ID: 20250622_210703
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
 * Live Chat Implementation using WebSockets
 */

// Import required modules
const WebSocket = require('ws');
const http = require('http');

// Create HTTP server
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Live Chat Server\n');
});

// Create WebSocket server
const wss = new WebSocket.Server({ server });

// Store connected clients
const clients = new Set();

wss.on('connection', (ws) => {
  // Add client to set
  clients.add(ws);

  // Handle incoming message
  ws.on('message', (message) => {
    console.log(`Received message => ${message}`);

    // Broadcast message to all connected clients
    clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  // Handle client disconnection
  ws.on('close', () => {
    clients.delete(ws);
  });

  // Handle client error
  ws.on('error', (error) => {
    console.error('Client error:', error);
    clients.delete(ws);
  });
});

// Handle server error
server.on('error', (error) => {
  console.error('Server error:', error);
});

// Start server
const port = 8080;
server.listen(port, () => {
  console.log(`Live Chat Server listening on port ${port}`);
});

// live-chat-client.js

/**
 * Live Chat Client Implementation
 */

// Import required modules
const WebSocket = require('ws');

// Establish WebSocket connection
const ws = new WebSocket('ws://localhost:8080');

// Handle connection open
ws.on('open', () => {
  console.log('Connected to Live Chat Server');

  // Send message to server
  const sendMessage = (message) => {
    ws.send(message);
  };

  // Example usage
  sendMessage('Hello from client!');
});

// Handle incoming message
ws.on('message', (message) => {
  console.log(`Received message => ${message}`);
});

// Handle connection close
ws.on('close', () => {
  console.log('Disconnected from Live Chat Server');
});

// Handle client error
ws.on('error', (error) => {
  console.error('Client error:', error);
});

// index.html

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
  <input id="message-input" type="text" placeholder="Type a message...">
  <button id="send-button">Send</button>

  <script>
    const chatLog = document.getElementById('chat-log');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    const ws = new WebSocket('ws://localhost:8080');

    ws.onmessage = (event) => {
      const message = event.data;
      const messageElement = document.createElement('div');
      messageElement.textContent = message;
      chatLog.appendChild(messageElement);
      chatLog.scrollTop = chatLog.scrollHeight;
    };

    sendButton.onclick = () => {
      const message = messageInput.value.trim();
      if (message) {
        ws.send(message);
        messageInput.value = '';
      }
    };
  </script>
</body>
</html>
```
