"""
Generated Code Metadata:
========================
Original URL: https://wormhole.pw
Prompt: Outline the steps to implement multichain applications using Wormhole's SDK, including native token transfers, queries, and messaging, and discuss the benefits of using Wormhole's permissionless tooling.
Generated: DETERMINISTIC_80353b9b1a940810
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from Wormhole SDK
const { Wormhole, TokenBridge, Message } = require('@wormhole/sdk');

// Initialize the Wormhole SDK
const wormhole = new Wormhole({
    // Configuration options for the Wormhole SDK
    network: 'mainnet', // or 'testnet' for testing purposes
    // Add other necessary configurations here
});

// Function to transfer native tokens across chains
async function transferNativeToken(sourceChain, targetChain, amount, recipientAddress) {
    try {
        // Create a token bridge instance
        const tokenBridge = new TokenBridge(wormhole, sourceChain);

        // Initiate the transfer
        const transferResult = await tokenBridge.transfer({
            amount,
            recipient: recipientAddress,
            targetChain,
        });

        console.log('Transfer successful:', transferResult);
    } catch (error) {
        console.error('Error during token transfer:', error);
    }
}

// Function to query token balance on a specific chain
async function queryTokenBalance(chain, address) {
    try {
        const balance = await wormhole.getTokenBalance(chain, address);
        console.log(`Token balance for ${address} on ${chain}:`, balance);
        return balance;
    } catch (error) {
        console.error('Error querying token balance:', error);
    }
}

// Function to send a message across chains
async function sendMessage(sourceChain, targetChain, messageContent) {
    try {
        const message = new Message({
            content: messageContent,
            targetChain,
        });

        const sendResult = await wormhole.sendMessage(sourceChain, message);
        console.log('Message sent successfully:', sendResult);
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

// Example usage
(async () => {
    const sourceChain = 'Ethereum';
    const targetChain = 'Solana';
    const amount = 100; // Amount of tokens to transfer
    const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const messageContent = 'Hello from Ethereum!';

    // Transfer native tokens
    await transferNativeToken(sourceChain, targetChain, amount, recipientAddress);

    // Query token balance
    await queryTokenBalance(sourceChain, recipientAddress);

    // Send a message
    await sendMessage(sourceChain, targetChain, messageContent);
})();
```
