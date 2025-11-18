"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3wallets.pages.dev
Prompt: Provide an example of integrating WalletConnect Protocol to send and receive notifications on EVM-compatible chains via Web3Inbox.
Generated: DETERMINISTIC_1bc678bbcda22b1e
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { Web3Modal } = require('web3modal'); // Web3Modal for WalletConnect integration
const WalletConnectProvider = require('@walletconnect/web3-provider'); // WalletConnect Provider
const { ethers } = require('ethers'); // Ethers.js for interacting with EVM-compatible chains
const Web3Inbox = require('web3-inbox'); // Web3Inbox for notifications

// Set up WalletConnect provider options
const providerOptions = {
    walletconnect: {
        package: WalletConnectProvider, // Required
        options: {
            infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
        },
    },
};

// Initialize Web3Modal
const web3Modal = new Web3Modal({
    cacheProvider: true, // Optional, cache provider for auto-reconnection
    providerOptions, // Required
});

// Global variables
let provider;
let signer;

// Connect to WalletConnect
async function connectWallet() {
    try {
        // Open Web3Modal and connect to wallet
        provider = await web3Modal.connect();
        provider.on('disconnect', () => {
            console.log('Wallet disconnected');
        });

        // Wrap the provider with ethers.js
        const web3Provider = new ethers.providers.Web3Provider(provider);
        signer = web3Provider.getSigner();

        console.log('Wallet connected');
    } catch (error) {
        console.error('Wallet connection failed:', error);
    }
}

// Initialize Web3Inbox for sending and receiving notifications
async function initializeWeb3Inbox() {
    try {
        if (!signer) {
            throw new Error('Wallet not connected. Please connect your wallet first.');
        }

        // Initialize Web3Inbox with the connected wallet
        const web3Inbox = new Web3Inbox(signer);

        // Subscribe to inbox notifications
        web3Inbox.on('notification', (notification) => {
            console.log('New notification received:', notification);
        });

        console.log('Web3Inbox initialized successfully');
    } catch (error) {
        console.error('Failed to initialize Web3Inbox:', error);
    }
}

// Send a notification using Web3Inbox
async function sendNotification(receiverAddress, message) {
    try {
        if (!signer) {
            throw new Error('Wallet not connected. Please connect your wallet first.');
        }

        if (!receiverAddress || !message) {
            throw new Error('Receiver address and message are required to send a notification.');
        }

        // Create and send a notification
        const web3Inbox = new Web3Inbox(signer);
        await web3Inbox.sendNotification(receiverAddress, message);

        console.log(`Notification sent to ${receiverAddress}: ${message}`);
    } catch (error) {
        console.error('Failed to send notification:', error);
    }
}

// Example usage
(async () => {
    try {
        await connectWallet(); // Connect to wallet
        await initializeWeb3Inbox(); // Initialize Web3Inbox

        // Send a sample notification
        const receiverAddress = '0xReceiverAddress'; // Replace with the recipient's EVM-compatible address
        const message = 'Hello, this is a test notification!';
        await sendNotification(receiverAddress, message);
    } catch (error) {
        console.error('Error in example usage:', error);
    }
})();
```

- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID.
- Replace `0xReceiverAddress` with the recipient's EVM-compatible wallet address.
- Ensure you install all dependencies (`web3modal`, `@walletconnect/web3-provider`, `ethers`, `web3-inbox`) via npm.
