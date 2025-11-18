"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Generate a basic configuration script for integrating a Solana wallet using the Web3Modal framework.
Generated: DETERMINISTIC_203bc2a23e20fa9d
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3Modal from 'web3modal';
import { providers } from 'ethers';

// Configuration for the Web3Modal
const providerOptions = {
    // Add any wallet providers you want to support
    injected: {
        display: {
            name: 'MetaMask',
            description: 'Connect with the provider in your Browser',
        },
        package: null, // no package needed for injected
    },
    walletconnect: {
        package: require('@walletconnect/web3-provider'), // Required
        options: {
            infuraId: 'YOUR_INFURA_ID', // Required
        },
    },
    // You can add other wallet providers here, e.g., Coinbase, Fortmatic, etc.
};

// Create a new instance of Web3Modal
const web3Modal = new Web3Modal({
    network: 'mainnet', // Can be 'mainnet', 'testnet', etc.
    cacheProvider: true, // Set to true to cache provider
    providerOptions, // Pass the provider options
});

// Function to connect the wallet
async function connectWallet() {
    try {
        // Open the modal to select a wallet provider
        const provider = await web3Modal.connect();
        
        // Create a new ethers provider
        const ethersProvider = new providers.Web3Provider(provider);
        
        // Get the signer for transactions
        const signer = ethersProvider.getSigner();
        
        // Get the user's address
        const userAddress = await signer.getAddress();
        
        console.log('Connected wallet address:', userAddress);
        
        return { ethersProvider, signer, userAddress };
    } catch (error) {
        console.error('Could not connect to wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to disconnect the wallet
async function disconnectWallet() {
    try {
        await web3Modal.clearCachedProvider(); // Clear cached provider
        console.log('Wallet disconnected');
    } catch (error) {
        console.error('Error disconnecting wallet:', error);
    }
}

// Export the functions for use in other modules
export { connectWallet, disconnectWallet };
```
