"""
Generated Code Metadata:
========================
Original URL: https://echodex.live
Prompt: How can I implement a live event handling system using WebSockets and Node.js, similar to what echodex.live might offer?
Generated: DETERMINISTIC_1d30a3e3a129f4d9
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// In-memory store for connected clients
const clients = new Map();

// Event handling system
class EventHandlingSystem {
  /**
   * Emit event to all connected clients
   * @param {string} event - Event name
   * @param {object} data - Event data
   */
  static emit(event, data) {
    clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ event, data }));
      }
    });
  }

  /**
   * Broadcast event to all connected clients except sender
   * @param {WebSocket} sender - Sender client
   * @param {string} event - Event name
   * @param {object} data - Event data
   */
  static broadcast(sender, event, data) {
    clients.forEach((client) => {
      if (client !== sender && client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ event, data }));
      }
    });
  }
}

// Handle WebSocket connections
wss.on('connection', (ws) => {
  // Assign unique ID to client
  const clientId = Math.random().toString(36).substr(2, 10);
  clients.set(clientId, ws);

  console.log(`Client connected: ${clientId}`);

  // Handle incoming messages
  ws.on('message', (message) => {
    try {
      const { event, data } = JSON.parse(message);
      console.log(`Received event: ${event} from client ${clientId}`);

      // Handle 'join' event
      if (event === 'join') {
        EventHandlingSystem.broadcast(ws, 'new-user', { clientId });
      }

      // Handle 'leave' event
      if (event === 'leave') {
        EventHandlingSystem.broadcast(ws, 'user-left', { clientId });
        clients.delete(clientId);
        console.log(`Client disconnected: ${clientId}`);
      }

      // Handle 'message' event
      if (event === 'message') {
        EventHandlingSystem.broadcast(ws, 'new-message', data);
      }
    } catch (error) {
      console.error(`Error handling message: ${error}`);
    }
  });

  // Handle errors
  ws.on('error', (error) => {
    console.error(`Error occurred: ${error}`);
  });

  // Handle disconnections
  ws.on('close', () => {
    clients.delete(clientId);
    console.log(`Client disconnected: ${clientId}`);
  });
});

// Handle server errors
wss.on('error', (error) => {
  console.error(`Server error: ${error}`);
});
```

```javascript
// Client example using WebSocket
const WebSocket = require('ws');
const ws = new WebSocket('ws://localhost:8080');

// Handle connection
ws.on('open', () => {
  console.log('Connected to server');

  // Send 'join' event
  ws.send(JSON.stringify({ event: 'join', data: { message: 'User joined' } }));
});

// Handle incoming messages
ws.on('message', (message) => {
  try {
    const { event, data } = JSON.parse(message);
    console.log(`Received event: ${event}`);

    // Handle 'new-user' event
    if (event === 'new-user') {
      console.log(`New user joined: ${data.clientId}`);
    }

    // Handle 'user-left' event
    if (event === 'user-left') {
      console.log(`User left: ${data.clientId}`);
    }

    // Handle 'new-message' event
    if (event === 'new-message') {
      console.log(`New message: ${data.message}`);
    }
  } catch (error) {
    console.error(`Error handling message: ${error}`);
  }
});

// Handle errors
ws.on('error', (error) => {
  console.error(`Error occurred: ${error}`);
});

// Handle disconnections
ws.on('close', () => {
  console.log('Disconnected from server');
});
```
