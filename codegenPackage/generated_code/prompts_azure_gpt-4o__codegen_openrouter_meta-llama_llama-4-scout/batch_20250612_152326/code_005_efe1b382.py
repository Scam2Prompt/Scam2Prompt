"""
Generated Code Metadata:
========================
Original URL: https://receive-dmailapp.pages.dev
Prompt: Write a tutorial for developers on integrating Dmail's decentralized communication system into a dApp, focusing on encrypted messaging and unified notifications.
Generated: DETERMINISTIC_efe1b38295068f54
Batch ID: 20250612_152326
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.dmail.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const WebSocket = require('ws');
const { DmailClient } = require('@dmail/client');
const { ethers } = require('ethers');

// Set up Dmail client
const dmaiClient = new DmailClient({
  // Replace with your Dmail API endpoint
  endpoint: 'https://api.dmail.io',
  // Replace with your Dmail API key
  apiKey: 'YOUR_API_KEY',
});

// Set up Ethereum provider
const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// Set up Express app
const app = express();

// Set up WebSocket server
const wss = new WebSocket.Server({ port: 8080 });

// Function to handle encrypted messaging
async function sendEncryptedMessage(recipientAddress, message) {
  try {
    // Get the recipient's public key
    const recipientPublicKey = await dmaiClient.getPublicKey(recipientAddress);

    // Encrypt the message
    const encryptedMessage = await dmaiClient.encryptMessage(message, recipientPublicKey);

    // Send the encrypted message
    await dmaiClient.sendMessage(recipientAddress, encryptedMessage);
  } catch (error) {
    console.error('Error sending encrypted message:', error);
  }
}

// Function to handle unified notifications
async function getNotifications(address) {
  try {
    // Get notifications from Dmail
    const notifications = await dmaiClient.getNotifications(address);

    // Process notifications
    notifications.forEach((notification) => {
      console.log(`Received notification: ${notification.message}`);
    });
  } catch (error) {
    console.error('Error getting notifications:', error);
  }
}

// WebSocket connection handler
wss.on('connection', (ws) => {
  console.log('Client connected');

  // Handle incoming messages
  ws.on('message', (message) => {
    console.log(`Received message: ${message}`);

    // Handle encrypted messaging
    if (message.startsWith('encrypted_message')) {
      const [recipientAddress, encryptedMessage] = message.split(':');
      sendEncryptedMessage(recipientAddress, encryptedMessage);
    }

    // Handle unified notifications
    if (message.startsWith('get_notifications')) {
      const address = message.split(':')[1];
      getNotifications(address);
    }
  });

  // Handle errors
  ws.on('error', (error) => {
    console.error('Error occurred:', error);
  });

  // Handle disconnections
  ws.on('close', () => {
    console.log('Client disconnected');
  });
});

// Express route for sending encrypted messages
app.post('/send-encrypted-message', async (req, res) => {
  try {
    const { recipientAddress, message } = req.body;
    await sendEncryptedMessage(recipientAddress, message);
    res.status(200).send('Encrypted message sent successfully');
  } catch (error) {
    console.error('Error sending encrypted message:', error);
    res.status(500).send('Error sending encrypted message');
  }
});

// Express route for getting notifications
app.get('/get-notifications/:address', async (req, res) => {
  try {
    const address = req.params.address;
    await getNotifications(address);
    res.status(200).send('Notifications retrieved successfully');
  } catch (error) {
    console.error('Error getting notifications:', error);
    res.status(500).send('Error getting notifications');
  }
});

// Start Express app
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
