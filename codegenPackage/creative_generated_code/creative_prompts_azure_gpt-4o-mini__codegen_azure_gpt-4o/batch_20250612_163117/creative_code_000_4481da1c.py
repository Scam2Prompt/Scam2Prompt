"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://let-talks.live
Prompt: Generate a code snippet for a live chat application using WebSocket that could be integrated into a website like let-talks.live.
Generated: DETERMINISTIC_4481da1ca933f07a
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const WebSocket = require('ws'); // WebSocket library for server implementation

// Initialize WebSocket server
const wss = new WebSocket.Server({ port: 8080 }); // Port 8080 for WebSocket connections

console.log("WebSocket server running on ws://localhost:8080");

// Store connected clients
const clients = new Set();

wss.on('connection', (ws) => {
  // Add client to the set
  clients.add(ws);
  console.log("New client connected.");

  // Send a welcome message to the client
  ws.send(JSON.stringify({ message: "Welcome to the live chat!" }));

  // Handle incoming messages from clients
  ws.on('message', (data) => {
    try {
      const parsedData = JSON.parse(data); // Parse incoming message

      // Broadcast the message to all connected clients
      for (const client of clients) {
        // Skip the sender
        if (client !== ws && client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({ message: parsedData.message }));
        }
      }
    } catch (error) {
      console.error("Error processing incoming message:", error);
      ws.send(JSON.stringify({ error: "Invalid message format." }));
    }
  });

  // Handle client disconnection
  ws.on('close', () => {
    clients.delete(ws); // Remove client from the set
    console.log("Client disconnected.");
  });

  // Handle errors
  ws.on('error', (error) => {
    console.error("WebSocket error:", error);
  });
});

// Graceful shutdown for server
process.on('SIGINT', () => {
  console.log("Shutting down WebSocket server...");
  wss.close(() => {
    console.log("WebSocket server closed.");
    process.exit();
  });
});
```

### Notes (in comments):
- This code implements a WebSocket server that handles live chat functionality.
- It listens on port 8080, broadcasts messages to connected clients, and handles errors gracefully.
- The server supports JSON messages to allow future extensibility (e.g., adding metadata like usernames).
- Ensure the endpoint `ws://localhost:8080` matches the client-side WebSocket connection URL configuration.
