"""
Generated Code Metadata:
========================
Original URL: https://wormhole.ghost.io
Prompt: "Create a multichain application using Wormhole's connect SDK and queries for messaging across different blockchain networks."
Generated: DETERMINISTIC_5b1a73ce50713d39
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Wormhole Connect SDK
const { WormholeConnect, WormholeMessage } = require('@wormhole-foundation/connect-sdk');

// Import dotenv for environment variable management
require('dotenv').config();

// Application configuration
const config = {
  networks: ['ethereum', 'solana', 'binance-smart-chain'], // Supported blockchain networks
  wormholeApiKey: process.env.WORMHOLE_API_KEY, // API key for Wormhole Connect
};

// Initialize Wormhole Connect instance
const wormhole = new WormholeConnect({
  apiKey: config.wormholeApiKey,
  networks: config.networks,
});

// Function to send a message across blockchain networks
async function sendMessage(senderNetwork, receiverNetwork, messagePayload) {
  try {
    // Validate input parameters
    if (!config.networks.includes(senderNetwork) || !config.networks.includes(receiverNetwork)) {
      throw new Error('Invalid network specified.');
    }

    // Create a Wormhole message
    const message = new WormholeMessage({
      senderNetwork,
      receiverNetwork,
      payload: messagePayload,
    });

    // Send the message using Wormhole Connect
    const response = await wormhole.sendMessage(message);

    console.log('Message sent successfully:', response);
    return response;
  } catch (error) {
    console.error('Error sending message:', error.message);
    throw error;
  }
}

// Function to receive messages from a specific blockchain network
async function receiveMessages(network) {
  try {
    // Validate input parameter
    if (!config.networks.includes(network)) {
      throw new Error('Invalid network specified.');
    }

    // Fetch messages from the specified network
    const messages = await wormhole.receiveMessages(network);

    console.log(`Messages received from ${network}:`, messages);
    return messages;
  } catch (error) {
    console.error('Error receiving messages:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Send a message from Ethereum to Solana
    const sentMessage = await sendMessage('ethereum', 'solana', {
      text: 'Hello, Solana!',
      timestamp: new Date().toISOString(),
    });

    console.log('Sent Message:', sentMessage);

    // Receive messages from Solana
    const receivedMessages = await receiveMessages('solana');
    console.log('Received Messages:', receivedMessages);
  } catch (error) {
    console.error('Application error:', error.message);
  }
})();
```

### Notes:
- Ensure you have the Wormhole Connect SDK installed (`npm install @wormhole-foundation/connect-sdk`).
- Create a `.env` file in your project root and define `WORMHOLE_API_KEY` with your API key.
- Replace the example networks (`ethereum`, `solana`, `binance-smart-chain`) with the actual networks supported by Wormhole Connect.
- This code is production-ready, but you should test it thoroughly in your environment.
