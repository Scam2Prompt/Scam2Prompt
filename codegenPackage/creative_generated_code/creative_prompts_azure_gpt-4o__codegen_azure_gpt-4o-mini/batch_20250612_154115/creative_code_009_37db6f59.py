"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge-finance.org
Prompt: Provide code examples for integrating deBridge's smart contracts into a decentralized application to enable cross-chain messaging functionality.
Generated: DETERMINISTIC_37db6f59faac3095
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries and modules
import { ethers } from 'ethers'; // Ethereum library for interacting with the blockchain
import { deBridge } from 'debridge-sdk'; // deBridge SDK for cross-chain messaging

// Configuration for the Ethereum provider and deBridge
const provider = new ethers.providers.Web3Provider(window.ethereum); // Web3 provider for user wallet
const signer = provider.getSigner(); // Get the signer for sending transactions

// deBridge contract address (update as needed)
const DEBRIDGE_CONTRACT_ADDRESS = '0xYourDeBridgeContractAddress';

// Function to send a cross-chain message
async function sendCrossChainMessage(destinationChainId, recipient, message) {
    try {
        // Create an instance of the deBridge contract
        const deBridgeContract = new ethers.Contract(
            DEBRIDGE_CONTRACT_ADDRESS,
            deBridge.abi, // ABI of deBridge contract
            signer
        );

        // Send the message using the deBridge contract
        const tx = await deBridgeContract.sendMessage(
            destinationChainId, // ID of the destination chain
            recipient, // Address of the recipient on the destination chain
            message, // The message to send
            { gasLimit: 200000 } // Set gas limit for the transaction
        );

        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log('Message sent successfully:', tx.hash);
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

// Function to receive messages from the deBridge
async function receiveMessages() {
    try {
        // Create an instance of the deBridge contract
        const deBridgeContract = new ethers.Contract(
            DEBRIDGE_CONTRACT_ADDRESS,
            deBridge.abi, // ABI of deBridge contract
            provider // Use provider to listen for events
        );

        // Listen for the 'MessageReceived' event from the contract
        deBridgeContract.on('MessageReceived', (from, message, event) => {
            console.log(`Message received from ${from}: ${message}`);
            // You can implement further logic to handle the received message here
        });
    } catch (error) {
        console.error('Error receiving messages:', error);
    }
}

// Main function to initialize the app
async function main() {
    // Request account access
    await provider.send('eth_requestAccounts', []);
    console.log('Connected to wallet.');

    // Start listening for incoming messages
    receiveMessages();

    // Example call to send a cross-chain message
    // Replace with actual values as required
    // sendCrossChainMessage(1, '0xRecipientAddress', 'Hello, cross-chain world!');
}

// Execute the main function
main().catch((error) => {
    console.error('Error in main execution:', error);
});
```
