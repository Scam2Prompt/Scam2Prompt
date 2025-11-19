"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Illustrate how to implement a secure wallet connection for users participating in the MOONHOP presale using a popular library like Web3.js.
Generated: DETERMINISTIC_e9d80218742dc372
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Define the WalletConnector class to handle wallet connections
class WalletConnector {
    constructor() {
        // Initialize Web3 instance
        this.web3 = null;
    }

    /**
     * Detects the user's wallet and connects to it
     * @returns {Promise<void>}
     */
    async connectWallet() {
        if (window.ethereum) {
            // Request account access if needed
            try {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Create Web3 instance using the current provider
                this.web3 = new Web3(window.ethereum);
                console.log('Wallet connected successfully');
            } catch (error) {
                console.error('User denied wallet connection:', error);
                throw new Error('Wallet connection failed');
            }
        } else {
            console.error('No Ethereum wallet detected. Please install Metamask or another wallet.');
            throw new Error('No Ethereum wallet detected');
        }
    }

    /**
     * Retrieves the connected wallet address
     * @returns {Promise<string>}
     */
    async getWalletAddress() {
        if (!this.web3) {
            throw new Error('Wallet is not connected. Please connect first.');
        }
        const accounts = await this.web3.eth.getAccounts();
        return accounts[0]; // Return the first account
    }

    /**
     * Disconnects the wallet by setting the Web3 instance to null
     */
    disconnectWallet() {
        this.web3 = null;
        console.log('Wallet disconnected');
    }

    /**
     * Checks if the wallet is connected
     * @returns {boolean}
     */
    isWalletConnected() {
        return this.web3 !== null;
    }
}

// Example usage of the WalletConnector class
(async () => {
    const walletConnector = new WalletConnector();
    
    try {
        await walletConnector.connectWallet();
        const address = await walletConnector.getWalletAddress();
        console.log('Connected Wallet Address:', address);
        // Add further logic here for the MOONHOP presale participation
    } catch (error) {
        console.error('Error connecting to wallet:', error.message);
    }
})();

// Exporting the WalletConnector class for use in other modules
export default WalletConnector;
```
