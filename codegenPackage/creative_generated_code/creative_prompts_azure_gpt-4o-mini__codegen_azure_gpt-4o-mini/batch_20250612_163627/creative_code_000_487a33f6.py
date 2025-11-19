"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duracorefixxdap.pages.dev
Prompt: How can I connect my wallet to decentralized applications (DApps) using the MultiChain Protocol?
Generated: DETERMINISTIC_487a33f6ec0da4f6
Batch ID: 20250612_163627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3'; // Web3.js for interacting with Ethereum
import { providers } from '@metamask/providers'; // MetaMask provider for wallet connection

// Define a class to handle wallet connection to DApps using MultiChain Protocol
class WalletConnector {
    constructor() {
        // Initialize Web3 instance
        this.web3 = null;
        this.provider = null;
    }

    // Method to initialize the wallet connection
    async init() {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                this.provider = window.ethereum;
                this.web3 = new Web3(this.provider);

                // Request account access
                await this.provider.request({ method: 'eth_requestAccounts' });
                console.log('Wallet connected successfully.');

                // Set up event listener for account changes
                this.provider.on('accountsChanged', (accounts) => {
                    console.log('Accounts changed:', accounts);
                });

                // Set up event listener for network changes
                this.provider.on('chainChanged', (chainId) => {
                    console.log('Network changed:', chainId);
                });
            } else {
                throw new Error('MetaMask is not installed. Please install it to use this DApp.');
            }
        } catch (error) {
            console.error('Failed to connect wallet:', error.message);
            alert(error.message); // Display error message to user
        }
    }

    // Method to get the currently connected account
    async getCurrentAccount() {
        try {
            const accounts = await this.web3.eth.getAccounts();
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error('Failed to retrieve accounts:', error.message);
            throw new Error('Unable to retrieve account information.');
        }
    }

    // Method to get the current network ID
    async getNetworkId() {
        try {
            return await this.web3.eth.net.getId(); // Get the network ID
        } catch (error) {
            console.error('Failed to retrieve network ID:', error.message);
            throw new Error('Unable to retrieve network information.');
        }
    }
}

// Example usage of WalletConnector class
(async () => {
    const walletConnector = new WalletConnector();
    await walletConnector.init(); // Initialize wallet connection

    try {
        const account = await walletConnector.getCurrentAccount();
        console.log('Connected account:', account);

        const networkId = await walletConnector.getNetworkId();
        console.log('Current network ID:', networkId);
    } catch (error) {
        console.error('Error during usage:', error.message);
    }
})();
```
