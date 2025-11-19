"""
Generated Code Metadata:
========================
Original URL: https://soulmagic.live
Prompt: Create a code example for a simple live streaming service using Node.js and WebSockets.
Generated: DETERMINISTIC_ae1ef095572189dd
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js
const express = require('express');
const WebSocket = require('ws');
const http = require('http');

// Initialize Express app
const app = express();

// Serve static files from public directory
app.use(express.static('public'));

// Create HTTP server
const server = http.createServer(app);

// Initialize WebSocket server
const wss = new WebSocket.Server({ server });

// Store connected clients
const clients = new Set();

// WebSocket connection handler
wss.on('connection', (ws) => {
  console.log('New client connected');
  clients.add(ws);

  // Message handler
  ws.on('message', (message) => {
    console.log(`Received: ${message}`);
    // Broadcast message to all clients
    clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  // Close handler
  ws.on('close', () => {
    console.log('Client disconnected');
    clients.delete(ws);
  });

  // Error handler
  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Streaming Demo</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }
    #stream-container {
      margin-top: 20px;
    }
    #message-input {
      margin-top: 20px;
      width: 300px;
      padding: 8px;
    }
    button {
      padding: 8px 16px;
      margin-left: 10px;
    }
  </style>
</head>
<body>
  <h1>Live Streaming Demo</h1>
  <div id="stream-container"></div>
  <input type="text" id="message-input" placeholder="Enter message to stream">
  <button id="send-button">Send</button>

  <script>
    // Connect to WebSocket server
    const ws = new WebSocket(`ws://${window.location.host}`);

    // Handle incoming messages
    ws.onmessage = (event) => {
      const streamContainer = document.getElementById('stream-container');
      const messageElement = document.createElement('div');
      messageElement.textContent = event.data;
      streamContainer.appendChild(messageElement);
    };

    // Handle connection open
    ws.onopen = () => {
      console.log('Connected to WebSocket server');
    };

    // Handle errors
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    // Handle connection close
    ws.onclose = () => {
      console.log('Disconnected from WebSocket server');
    };

    // Send message when button is clicked
    document.getElementById('send-button').addEventListener('click', () => {
      const messageInput = document.getElementById('message-input');
      const message = messageInput.value.trim();
      if (message) {
        ws.send(message);
        messageInput.value = '';
      }
    });

    // Send message when Enter key is pressed
    document.getElementById('message-input').addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        document.getElementById('send-button').click();
      }
    });
  </script>
</body>
</html>
```

```json
// package.json
{
  "name": "live-streaming-demo",
  "version": "1.0.0",
  "description": "Simple live streaming service using WebSockets",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "ws": "^8.16.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.2"
  }
}
```
