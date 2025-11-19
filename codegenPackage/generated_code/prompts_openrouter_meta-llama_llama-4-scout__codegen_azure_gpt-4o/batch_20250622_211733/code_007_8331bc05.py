"""
Generated Code Metadata:
========================
Original URL: https://tante4dx1.beauty
Prompt: Suggest a system architecture for a real-time live chat support feature, ensuring 24/7 availability for customer inquiries.
Generated: DETERMINISTIC_8331bc0527dd2e75
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a simplified implementation of a real-time live chat support feature using Node.js, Express, and WebSocket. This architecture ensures scalability and 24/7 availability by leveraging a stateless server and a Redis-based message broker for persistence and real-time communication.

```javascript
// server.js
// Import required modules
const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const redis = require('redis');

// Initialize Express app
const app = express();
const server = http.createServer(app);

// Initialize WebSocket server
const wss = new WebSocket.Server({ server });

// Initialize Redis client
const redisClient = redis.createClient();

// Middleware for parsing JSON requests
app.use(express.json());

// Endpoint for health check
app.get('/health', (req, res) => {
  res.status(200).send('Live Chat Support is running.');
});

// WebSocket connection handler
wss.on('connection', (ws) => {
  console.log('New client connected.');

  // Handle incoming messages from clients
  ws.on('message', (message) => {
    try {
      const parsedMessage = JSON.parse(message);

      // Example message structure: { type: 'message', userId: '123', text: 'Hello' }
      if (parsedMessage.type === 'message') {
        // Broadcast the message to all connected clients
        wss.clients.forEach((client) => {
          if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(parsedMessage));
          }
        });

        // Save the message to Redis for persistence
        redisClient.lpush(`chat:${parsedMessage.userId}`, JSON.stringify(parsedMessage), (err) => {
          if (err) {
            console.error('Error saving message to Redis:', err);
          }
        });
      }
    } catch (error) {
      console.error('Error processing message:', error);
      ws.send(JSON.stringify({ error: 'Invalid message format.' }));
    }
  });

  // Handle WebSocket connection close
  ws.on('close', () => {
    console.log('Client disconnected.');
  });
});

// Error handling middleware for Express
app.use((err, req, res, next) => {
  console.error('Server error:', err);
  res.status(500).send('Internal Server Error');
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Live Chat Support server is running on port ${PORT}`);
});

// Redis connection error handling
redisClient.on('error', (err) => {
  console.error('Redis error:', err);
});
```

### Key Features:
1. **WebSocket for Real-Time Communication**: Enables real-time messaging between clients and the server.
2. **Redis for Persistence**: Ensures messages are stored for retrieval in case of server restarts or crashes.
3. **Health Check Endpoint**: Provides a simple way to verify the server's availability.
4. **Error Handling**: Handles invalid message formats and Redis errors gracefully.
5. **Scalability**: Stateless architecture allows horizontal scaling by deploying multiple instances behind a load balancer.

### Deployment Considerations:
- Use a cloud provider (e.g., AWS, Azure, GCP) for 24/7 availability.
- Deploy Redis in a managed service or cluster for high availability.
- Use HTTPS for secure communication.
- Implement authentication and authorization for WebSocket connections.
