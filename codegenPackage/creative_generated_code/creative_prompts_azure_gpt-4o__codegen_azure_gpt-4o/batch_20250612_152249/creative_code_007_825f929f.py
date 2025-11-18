"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testauikg-8uv.pages.dev
Prompt: Provide an example of how to build a mobile-friendly Web3 messaging app that supports connecting any wallet and receiving notifications, inspired by Web3Inbox.
Generated: DETERMINISTIC_825f929f4d6bd574
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
// Using Node.js and Express for the backend server
// Using ethers.js for wallet interaction
// Using WebSocket for real-time notifications

const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const bodyParser = require('body-parser');
const { ethers } = require('ethers');

// Create an Express application
const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Set up an in-memory datastore for simplicity
// In production, use a database like PostgreSQL or MongoDB
const users = {}; // { walletAddress: { messages: [], connections: [] } }

// Wallet connection endpoint
app.post('/connect-wallet', async (req, res) => {
  try {
    const { walletAddress } = req.body;

    // Validate wallet address
    if (!ethers.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Register the wallet if not already registered
    if (!users[walletAddress]) {
      users[walletAddress] = { messages: [], connections: [] };
    }

    res.status(200).json({ message: 'Wallet connected successfully' });
  } catch (error) {
    console.error('Error connecting wallet:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Messaging endpoint
app.post('/send-message', async (req, res) => {
  try {
    const { senderWallet, receiverWallet, message } = req.body;

    // Validate input
    if (!ethers.utils.isAddress(senderWallet) || !ethers.utils.isAddress(receiverWallet)) {
      return res.status(400).json({ error: 'Invalid wallet address(es)' });
    }
    if (!message || typeof message !== 'string') {
      return res.status(400).json({ error: 'Message must be a non-empty string' });
    }

    // Ensure receiver is registered
    if (!users[receiverWallet]) {
      return res.status(404).json({ error: 'Receiver wallet not found' });
    }

    // Save message to the receiver's inbox
    users[receiverWallet].messages.push({ senderWallet, message, timestamp: new Date() });

    // Send notification via WebSocket if the receiver is connected
    users[receiverWallet].connections.forEach((ws) => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: 'message', senderWallet, message }));
      }
    });

    res.status(200).json({ message: 'Message sent successfully' });
  } catch (error) {
    console.error('Error sending message:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Fetch messages endpoint
app.get('/messages/:walletAddress', async (req, res) => {
  try {
    const { walletAddress } = req.params;

    // Validate wallet address
    if (!ethers.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Ensure the wallet is registered
    if (!users[walletAddress]) {
      return res.status(404).json({ error: 'Wallet not found' });
    }

    res.status(200).json({ messages: users[walletAddress].messages });
  } catch (error) {
    console.error('Error fetching messages:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// WebSocket connection handler for notifications
wss.on('connection', (ws, req) => {
  // Extract wallet address from query parameters (e.g., ws://server?walletAddress=...)
  const walletAddress = req.url.split('?walletAddress=')[1];

  if (!walletAddress || !ethers.utils.isAddress(walletAddress)) {
    ws.close();
    return;
  }

  // Register WebSocket connection
  if (!users[walletAddress]) {
    users[walletAddress] = { messages: [], connections: [] };
  }
  users[walletAddress].connections.push(ws);

  // Clean up when the connection is closed
  ws.on('close', () => {
    users[walletAddress].connections = users[walletAddress].connections.filter((conn) => conn !== ws);
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- This code provides a basic Web3 messaging app backend with wallet connection, message sending, message retrieval, and real-time notifications.
- In production, you should use a secure database and implement authentication/authorization for better security.
