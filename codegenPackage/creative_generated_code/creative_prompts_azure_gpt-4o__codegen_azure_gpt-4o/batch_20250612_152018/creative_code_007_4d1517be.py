"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://analogone.pages.dev
Prompt: Provide code examples for implementing cross-chain communication using Analog's GMP SDK and describe its advantages for omnichain DApp development.
Generated: DETERMINISTIC_4d1517be01f4a68b
Batch ID: 20250612_152018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://destination-chain-rpc.endpoint": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://source-chain-rpc.endpoint": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Analog GMP SDK
const AnalogGMP = require('@analog-foundation/gmp-sdk');
const ethers = require('ethers');

// Configuration for Analog SDK (replace with your own details)
const analogConfig = {
  apiKey: 'YOUR_ANALOG_API_KEY', // Replace with your Analog API key
  rpcUrls: {
    source: 'https://source-chain-rpc.endpoint', // Replace with source chain RPC URL
    destination: 'https://destination-chain-rpc.endpoint', // Replace with destination chain RPC URL
  },
};

// Initialize Analog GMP SDK
const analogSDK = new AnalogGMP(analogConfig);

// Function to execute cross-chain message passing
async function sendCrossChainMessage(data, destinationChain, senderPrivateKey) {
  try {
    // Initialize the sender's wallet
    const wallet = new ethers.Wallet(senderPrivateKey);
    const signer = wallet.connect(new ethers.providers.JsonRpcProvider(analogConfig.rpcUrls.source));

    // Create a cross-chain message
    const messagePayload = {
      data: data, // Data to be sent across chains
      destinationChain: destinationChain, // Target chain
    };

    // Send the cross-chain message
    const tx = await analogSDK.sendMessage(signer, messagePayload);
    console.log('Cross-chain message sent successfully:', tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction mined:', receipt);
    return receipt;
  } catch (error) {
    console.error('Error sending cross-chain message:', error);
    throw new Error('Failed to send cross-chain message.');
  }
}

// Function to receive and handle cross-chain messages on the destination chain
async function handleCrossChainMessage(destinationPrivateKey) {
  try {
    // Initialize the destination wallet
    const wallet = new ethers.Wallet(destinationPrivateKey);
    const signer = wallet.connect(new ethers.providers.JsonRpcProvider(analogConfig.rpcUrls.destination));

    // Listen for incoming messages on the destination chain
    analogSDK.onMessageReceived(signer, async (message) => {
      console.log('Cross-chain message received:', message);

      // Handle the incoming message
      const { data, sender } = message;
      console.log('Message data:', data);
      console.log('Sender address:', sender);

      // Perform any business logic or state updates based on the message
      // (Example: Update a contract state or trigger an event)
    });
  } catch (error) {
    console.error('Error handling cross-chain message:', error);
    throw new Error('Failed to handle cross-chain message.');
  }
}

// Example usage
(async () => {
  const senderPrivateKey = 'YOUR_SOURCE_CHAIN_PRIVATE_KEY'; // Replace with sender's private key
  const destinationPrivateKey = 'YOUR_DESTINATION_CHAIN_PRIVATE_KEY'; // Replace with receiver's private key
  const destinationChain = 'destination-chain-id'; // Replace with destination chain ID
  const data = { value: 'Hello, cross-chain world!' }; // Example payload data

  try {
    // Send a cross-chain message
    const receipt = await sendCrossChainMessage(data, destinationChain, senderPrivateKey);
    console.log('Message sent successfully, transaction receipt:', receipt);

    // Handle incoming messages on the destination chain
    await handleCrossChainMessage(destinationPrivateKey);
  } catch (error) {
    console.error('Error executing cross-chain communication:', error);
  }
})();
```
