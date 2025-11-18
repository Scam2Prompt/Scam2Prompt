"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pre-sales-kelexo.web.app
Prompt: Suggest best practices for integrating blockchain wallet connections into a web application, inspired by the Kelexo platform.
Generated: DETERMINISTIC_52802b2aa9e6fcc3
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define a class for handling blockchain wallet connections
class WalletConnector {
    constructor() {
        // Initialize web3 instance
        this.web3 = null;
        this.account = null;
    }

    /**
     * Initialize the wallet connection
     * Checks if the user has a wallet installed (e.g., MetaMask)
     */
    async init() {
        if (window.ethereum) {
            // Set up web3 with the current provider
            this.web3 = new Web3(window.ethereum);
            try {
                // Request account access if needed
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Set the user's account
                this.account = await this.getAccount();
                console.log("Wallet connected:", this.account);
            } catch (error) {
                console.error("User denied wallet connection:", error);
            }
        } else {
            console.error("No wallet found! Please install MetaMask.");
            alert("No wallet found! Please install MetaMask.");
        }
    }

    /**
     * Get the current connected account
     * @returns {string} - The connected account address
     */
    async getAccount() {
        const accounts = await this.web3.eth.getAccounts();
        return accounts[0]; // Returning the first account
    }

    /**
     * Listen for account changes
     * Updates the account variable and notifies the user
     */
    listenForAccountChange() {
        window.ethereum.on('accountsChanged', async (accounts) => {
            if (accounts.length === 0) {
                console.log("Please connect to MetaMask.");
                alert("Please connect to MetaMask.");
            } else {
                this.account = accounts[0];
                console.log("Account changed:", this.account);
            }
        });
    }

    /**
     * Listen for network changes
     * Notifies the user if the network is changed
     */
    listenForNetworkChange() {
        window.ethereum.on('chainChanged', (chainId) => {
            console.log("Network changed:", chainId);
            alert("Network changed. Please refresh the page.");
        });
    }
}

// Usage example
const walletConnector = new WalletConnector();
walletConnector.init();
walletConnector.listenForAccountChange();
walletConnector.listenForNetworkChange();
```
