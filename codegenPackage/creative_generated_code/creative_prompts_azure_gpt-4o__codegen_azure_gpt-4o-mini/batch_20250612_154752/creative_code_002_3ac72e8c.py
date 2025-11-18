"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao1.pro
Prompt: Create a script that checks if a user’s wallet is connected to a dApp, inspired by the wallet connection functionality on DAO1.
Generated: DETERMINISTIC_3ac72e8c8294318b
Batch ID: 20250612_154752
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

// Define the WalletConnector class
class WalletConnector {
    constructor() {
        // Initialize web3 instance
        this.web3 = null;
        this.isConnected = false;
    }

    /**
     * Initializes the web3 instance and checks for wallet connection.
     */
    async init() {
        try {
            // Check if the browser has an Ethereum provider (like MetaMask)
            if (window.ethereum) {
                // Create web3 instance with the Ethereum provider
                this.web3 = new Web3(window.ethereum);
                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                this.isConnected = true;
                console.log('Wallet is connected.');
            } else {
                throw new Error('No Ethereum provider detected. Please install MetaMask or another wallet.');
            }
        } catch (error) {
            // Handle errors during wallet connection
            console.error('Error connecting to wallet:', error.message);
        }
    }

    /**
     * Checks if the wallet is connected to the dApp.
     * @returns {boolean} True if connected, false otherwise.
     */
    checkConnection() {
        return this.isConnected;
    }

    /**
     * Get the connected wallet accounts.
     * @returns {Promise<string[]>} List of wallet addresses if connected, otherwise an empty array.
     */
    async getAccounts() {
        if (!this.isConnected) {
            console.warn('Wallet is not connected. Unable to retrieve accounts.');
            return [];
        }

        try {
            const accounts = await this.web3.eth.getAccounts();
            return accounts;
        } catch (error) {
            console.error('Error fetching accounts:', error.message);
            return [];
        }
    }
}

// Example usage of the WalletConnector class
(async () => {
    const walletConnector = new WalletConnector();
    await walletConnector.init();

    if (walletConnector.checkConnection()) {
        const accounts = await walletConnector.getAccounts();
        console.log('Connected accounts:', accounts);
    } else {
        console.log('Wallet is not connected.');
    }
})();
```
