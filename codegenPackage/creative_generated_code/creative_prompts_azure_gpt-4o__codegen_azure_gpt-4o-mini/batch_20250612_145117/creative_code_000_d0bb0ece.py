"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mapledefi.finance
Prompt: Write code to integrate a cryptocurrency wallet connection feature using Web3.js, similar to the functionality described on the Maple DeFi Finance website.
Generated: DETERMINISTIC_d0bb0eceebd30a35
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define the WalletConnector class
class WalletConnector {
    constructor() {
        // Initialize web3 and the user's current provider
        this.web3 = null;
        this.provider = null;
        this.account = null;
    }

    /**
     * Initializes the Web3 instance
     * - Checks if the browser has an Ethereum provider (like MetaMask)
     */
    async initWeb3() {
        if (window.ethereum) {
            // Use the provided Ethereum provider (e.g., MetaMask)
            this.provider = window.ethereum;
            this.web3 = new Web3(this.provider);
            console.log("Web3 initialized with the provider.");
        } else {
            alert("No Ethereum provider detected. Please install MetaMask.");
            throw new Error("Ethereum provider not found");
        }
    }

    /**
     * Connects to the user's wallet
     * - Requests account access using the provider
     */
    async connectWallet() {
        try {
            // Request account access
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];
            console.log(`Connected to wallet: ${this.account}`);
            return this.account;
        } catch (error) {
            console.error("Error connecting to wallet:", error);
            throw new Error("Wallet connection failed");
        }
    }

    /**
     * Disconnects the wallet (if applicable)
     * - Currently, no direct method to disconnect wallets like MetaMask
     */
    disconnectWallet() {
        this.account = null;
        console.log("Wallet disconnected.");
    }

    /**
     * Fetches the current account balance
     * @returns {Promise<string>} The account balance in Ether
     */
    async getAccountBalance() {
        if (!this.account) {
            throw new Error("Wallet is not connected");
        }
        const balanceWei = await this.web3.eth.getBalance(this.account);
        const balanceEther = this.web3.utils.fromWei(balanceWei, 'ether');
        console.log(`Account balance: ${balanceEther} ETH`);
        return balanceEther;
    }
}

// Example usage
(async () => {
    const walletConnector = new WalletConnector();

    try {
        await walletConnector.initWeb3();
        await walletConnector.connectWallet();
        const balance = await walletConnector.getAccountBalance();
        console.log(`Your balance is: ${balance} ETH`);
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();
```
