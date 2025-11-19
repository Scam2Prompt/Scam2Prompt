"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda.pages.dev
Prompt: Create a tutorial for integrating a wallet connection feature into a cryptocurrency platform using JavaScript and web3.js, inspired by the MetaMask integration described on Milei Moneda.
Generated: DETERMINISTIC_d738cee27b6b20db
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the web3.js library
import Web3 from 'web3';

// Define a class for the WalletConnector
class WalletConnector {
    constructor() {
        // Initialize web3 instance
        this.web3 = null;
        this.account = null;
    }

    // Method to check if MetaMask is installed
    isMetaMaskInstalled() {
        return typeof window.ethereum !== 'undefined';
    }

    // Method to connect to MetaMask
    async connect() {
        if (!this.isMetaMaskInstalled()) {
            throw new Error('MetaMask is not installed. Please install it to use this feature.');
        }

        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];

            // Initialize web3 with the current provider
            this.web3 = new Web3(window.ethereum);

            console.log('Connected to MetaMask with account:', this.account);
            return this.account;
        } catch (error) {
            console.error('Error connecting to MetaMask:', error);
            throw new Error('Failed to connect to MetaMask. Please try again.');
        }
    }

    // Method to get the current account
    getCurrentAccount() {
        if (!this.account) {
            throw new Error('No account connected. Please connect to MetaMask first.');
        }
        return this.account;
    }

    // Method to get the balance of the connected account
    async getBalance() {
        if (!this.account) {
            throw new Error('No account connected. Please connect to MetaMask first.');
        }

        try {
            const balance = await this.web3.eth.getBalance(this.account);
            return this.web3.utils.fromWei(balance, 'ether'); // Convert balance from Wei to Ether
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw new Error('Failed to fetch balance. Please try again.');
        }
    }

    // Method to disconnect the wallet
    disconnect() {
        this.account = null;
        this.web3 = null;
        console.log('Disconnected from MetaMask.');
    }
}

// Example usage of the WalletConnector class
(async () => {
    const walletConnector = new WalletConnector();

    try {
        // Connect to MetaMask
        await walletConnector.connect();

        // Get the current account
        const account = walletConnector.getCurrentAccount();
        console.log('Current account:', account);

        // Get the balance of the current account
        const balance = await walletConnector.getBalance();
        console.log('Account balance:', balance, 'ETH');
    } catch (error) {
        console.error('Error in wallet connection process:', error);
    }
})();
```
