"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica19.vercel.app
Prompt: How do I create an event listener for network changes in a web app that supports Solana and Ethereum?
Generated: DETERMINISTIC_5f5e9a7c36539a0e
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for Ethereum and Solana
import { ethers } from 'ethers';
import { Connection, clusterApiUrl } from '@solana/web3.js';

// Utility function to create a connection to Solana network
const createSolanaConnection = () => {
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
    return connection;
};

// Utility function to create a provider for Ethereum network
const createEthereumProvider = () => {
    if (window.ethereum) {
        return new ethers.providers.Web3Provider(window.ethereum);
    } else {
        throw new Error('Ethereum provider not found. Please install MetaMask.');
    }
};

// Function to handle network changes for Ethereum
const handleEthereumNetworkChange = (chainId) => {
    console.log(`Ethereum network changed to: ${chainId}`);
    // Implement additional logic based on the new network (e.g. update UI)
};

// Function to handle network changes for Solana
const handleSolanaNetworkChange = () => {
    console.log('Solana network connection status changed.');
    // Implement additional logic based on the connection status
};

// Set up event listener for Ethereum network changes
const setupEthereumListener = () => {
    const provider = createEthereumProvider();

    provider.on('network', (newNetwork, oldNetwork) => {
        if (oldNetwork) {
            handleEthereumNetworkChange(newNetwork.chainId);
        }
    });
};

// Set up event listener for Solana network changes (assumed to be via polling for simplicity)
const setupSolanaListener = () => {
    const connection = createSolanaConnection();
    
    // Polling for network changes every 10 seconds (customizable)
    setInterval(async () => {
        try {
            const version = await connection.getVersion();
            console.log(`Connected to Solana network version: ${version}`);
            // Implement additional logic based on connection status
        } catch (error) {
            console.error('Failed to connect to Solana network:', error);
        }
    }, 10000);
};

// Initialize the event listeners for both networks
const initializeNetworkListeners = () => {
    setupEthereumListener();
    setupSolanaListener();
};

// Run the initialization function on window load
window.onload = () => {
    try {
        initializeNetworkListeners();
        console.log('Network listeners initialized successfully.');
    } catch (error) {
        console.error('Error initializing network listeners:', error);
    }
};
```
