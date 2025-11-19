"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Develop a privacy-focused backend API in Node.js for Connexa that ensures no chat history or message storage, as described on the website.
Generated: DETERMINISTIC_b80f62fbe7e2bdce
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const helmet = require('helmet');
const cors = require('cors');
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Enable CORS and helmet for security
app.use(cors());
app.use(helmet());
app.use(express.json());

// Define a constant for the maximum allowed message size
const MAX_MESSAGE_SIZE = 1024 * 1024; // 1MB

// In-memory storage for active connections (no chat history or message storage)
const activeConnections = new Map();

// Handle WebSocket connections
wss.on('connection', (ws) => {
  // Handle incoming messages
  ws.on('message', (message) => {
    if (message.length > MAX_MESSAGE_SIZE) {
      // Handle oversized messages
      ws.send(JSON.stringify({ type: 'error', message: 'Message too large' }));
      return;
    }

    try {
      // Relay the message to the intended recipient
      const { type, data, recipientId } = JSON.parse(message);
      if (type && data && recipientId) {
        if (activeConnections.has(recipientId)) {
          activeConnections.get(recipientId).send(JSON.stringify({ type, data }));
        } else {
          // Handle unknown recipient
          ws.send(JSON.stringify({ type: 'error', message: 'Recipient not found' }));
        }
      } else {
        // Handle malformed messages
        ws.send(JSON.stringify({ type: 'error', message: 'Invalid message format' }));
      }
    } catch (error) {
      // Handle JSON parsing errors
      ws.send(JSON.stringify({ type: 'error', message: 'Invalid JSON' }));
    }
  });

  // Handle connection close
  ws.on('close', () => {
    // Remove the connection from the active connections map
    for (const [id, connection] of activeConnections) {
      if (connection === ws) {
        activeConnections.delete(id);
        break;
      }
    }
  });

  // Handle connection errors
  ws.on('error', (error) => {
    console.error('Connection error:', error);
  });

  // Add the connection to the active connections map
  const connectionId = Date.now().toString();
  activeConnections.set(connectionId, ws);
});

// Handle WebSocket errors
wss.on('error', (error) => {
  console.error('WebSocket error:', error);
});

// Define a route for health checks
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
