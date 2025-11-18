"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Recommend libraries or SDKs provided by MetaMask for integrating blockchain-based applications with Web3 functionality.
Generated: DETERMINISTIC_6003d203ccf22e5b
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries from MetaMask and Web3.js
import Web3 from 'web3';

// Define a class to handle MetaMask integration
class MetaMaskIntegration {
    constructor() {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            this.web3 = new Web3(window.ethereum);
        } else {
            throw new Error('MetaMask is not installed. Please install it to use this application.');
        }
    }

    // Request account access
    async requestAccount() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error('Error requesting account:', error);
            throw new Error('User denied account access');
        }
    }

    // Get the current user's account
    async getCurrentAccount() {
        const accounts = await this.web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please ensure MetaMask is connected.');
        }
        return accounts[0];
    }

    // Send a transaction
    async sendTransaction(transactionParams) {
        try {
            const transactionHash = await this.web3.eth.sendTransaction(transactionParams);
            return transactionHash;
        } catch (error) {
            console.error('Error sending transaction:', error);
            throw new Error('Transaction failed');
        }
    }

    // Get the balance of an account
    async getAccountBalance(account) {
        try {
            const balance = await this.web3.eth.getBalance(account);
            return this.web3.utils.fromWei(balance, 'ether'); // Convert balance from Wei to Ether
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw new Error('Failed to retrieve account balance');
        }
    }
}

// Example usage
(async () => {
    try {
        const metaMask = new MetaMaskIntegration();
        const account = await metaMask.requestAccount();
        console.log(`Connected account: ${account}`);

        const balance = await metaMask.getAccountBalance(account);
        console.log(`Account balance: ${balance} ETH`);

        // Example transaction parameters
        const transactionParams = {
            from: account,
            to: '0xRecipientAddress', // Replace with a valid recipient address
            value: metaMask.web3.utils.toWei('0.01', 'ether'),
        };

        const transactionHash = await metaMask.sendTransaction(transactionParams);
        console.log(`Transaction successful with hash: ${transactionHash}`);
    } catch (error) {
        console.error('Error in MetaMask integration:', error.message);
    }
})();
```
