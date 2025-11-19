"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-test-wallet.pages.dev
Prompt: How does WalletConnect Test Wallet facilitate testing of WalletConnect integrations?
Generated: DETERMINISTIC_b28129960a91f0c9
Batch ID: 20250622_205158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
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
/**
 * WalletConnect Test Wallet
 * =======================
 * 
 * This application facilitates testing of WalletConnect integrations.
 * 
 * @author [Your Name]
 */

// Import required libraries
const express = require('express');
const WebSocket = require('ws');
const { WalletConnect } = require('@walletconnect/node');

// Initialize WalletConnect
const walletConnect = new WalletConnect({
  // Bridge URL
  bridge: 'https://bridge.walletconnect.org',
});

// Create an Express app
const app = express();

// Create a WebSocket server
const wss = new WebSocket.Server({ port: 8080 });

// Store connected clients
const clients = [];

// Handle WebSocket connections
wss.on('connection', (ws) => {
  // Add client to the list
  clients.push(ws);

  // Handle incoming messages
  ws.on('message', (message) => {
    try {
      // Parse incoming message
      const data = JSON.parse(message);

      // Handle WalletConnect requests
      if (data.type === 'wc_pairing') {
        // Handle pairing request
        handlePairingRequest(ws, data);
      } else if (data.type === 'wc_request') {
        // Handle request
        handleRequest(ws, data);
      }
    } catch (error) {
      console.error('Error handling message:', error);
      ws.send(JSON.stringify({ error: 'Invalid message' }));
    }
  });

  // Handle client disconnection
  ws.on('close', () => {
    // Remove client from the list
    clients.splice(clients.indexOf(ws), 1);
  });
});

// Handle pairing requests
async function handlePairingRequest(ws, data) {
  try {
    // Approve pairing request
    const approval = await walletConnect.approvePairing(data);

    // Send approval response
    ws.send(JSON.stringify({ type: 'wc_pairing_approved', approval }));
  } catch (error) {
    console.error('Error handling pairing request:', error);
    ws.send(JSON.stringify({ error: 'Failed to approve pairing' }));
  }
}

// Handle requests
async function handleRequest(ws, data) {
  try {
    // Handle request
    const response = await walletConnect.handleRequest(data);

    // Send response
    ws.send(JSON.stringify({ type: 'wc_response', response }));
  } catch (error) {
    console.error('Error handling request:', error);
    ws.send(JSON.stringify({ error: 'Failed to handle request' }));
  }
}

// Start the Express app
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Define a simple API endpoint to test WalletConnect
app.get('/test', (req, res) => {
  res.send('WalletConnect Test Wallet is running');
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).send('Internal Server Error');
});
```
