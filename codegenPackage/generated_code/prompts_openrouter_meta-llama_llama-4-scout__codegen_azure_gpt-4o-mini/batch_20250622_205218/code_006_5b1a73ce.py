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
// Import necessary libraries
const { Wormhole, Chain, Message } = require('@wormhole-foundation/wormhole-connect-sdk');

// Define the supported chains
const supportedChains = {
    ETH: Chain.ETH,
    SOL: Chain.SOL,
    BSC: Chain.BSC,
    POLYGON: Chain.POLYGON,
};

// Initialize the Wormhole SDK
const wormhole = new Wormhole({
    chains: Object.values(supportedChains),
});

// Function to send a message across chains
async function sendMessage(sourceChain, targetChain, messageContent) {
    try {
        // Validate the source and target chains
        if (!supportedChains[sourceChain] || !supportedChains[targetChain]) {
            throw new Error('Unsupported chain specified.');
        }

        // Create a message object
        const message = new Message({
            content: messageContent,
            sourceChain: supportedChains[sourceChain],
            targetChain: supportedChains[targetChain],
        });

        // Send the message
        const txHash = await wormhole.sendMessage(message);
        console.log(`Message sent successfully! Transaction Hash: ${txHash}`);
    } catch (error) {
        console.error('Error sending message:', error.message);
    }
}

// Function to receive a message from a specific chain
async function receiveMessage(targetChain) {
    try {
        // Validate the target chain
        if (!supportedChains[targetChain]) {
            throw new Error('Unsupported chain specified.');
        }

        // Listen for incoming messages
        wormhole.onMessage(targetChain, (message) => {
            console.log(`Received message on ${targetChain}:`, message.content);
        });
    } catch (error) {
        console.error('Error receiving message:', error.message);
    }
}

// Example usage
(async () => {
    // Send a message from Ethereum to Solana
    await sendMessage('ETH', 'SOL', 'Hello from Ethereum!');

    // Start listening for messages on Solana
    await receiveMessage('SOL');
})();
```
