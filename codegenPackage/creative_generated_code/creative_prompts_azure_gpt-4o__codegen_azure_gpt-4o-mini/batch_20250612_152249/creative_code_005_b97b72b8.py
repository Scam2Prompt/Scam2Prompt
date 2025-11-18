"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudconnect.tistory.com
Prompt: What are the best practices for implementing a secure wallet connection feature in a dApp? Include code examples using Web3.js or ethers.js.
Generated: DETERMINISTIC_b97b72b88fe7ee57
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Define a class to handle the wallet connection
class WalletConnector {
    constructor() {
        // Initialize provider and signer
        this.provider = null;
        this.signer = null;
    }

    // Method to connect to the user's wallet
    async connectWallet() {
        try {
            // Check if the window object has Ethereum provider (e.g., MetaMask)
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                
                // Set up the provider and signer
                this.provider = new ethers.providers.Web3Provider(window.ethereum);
                this.signer = this.provider.getSigner();

                console.log("Wallet connected:", accounts[0]);
                return accounts[0];
            } else {
                throw new Error("Ethereum provider is not available. Please install a wallet like MetaMask.");
            }
        } catch (error) {
            console.error("Error connecting to wallet:", error);
            throw error; // Rethrow the error for further handling if needed
        }
    }

    // Method to fetch the user's account balance
    async getAccountBalance() {
        try {
            if (!this.signer) throw new Error("Wallet is not connected.");

            const address = await this.signer.getAddress();
            const balance = await this.provider.getBalance(address);
            const balanceInEth = ethers.utils.formatEther(balance); // Convert balance from Wei to Ether

            console.log(`Account balance for ${address}: ${balanceInEth} ETH`);
            return balanceInEth;
        } catch (error) {
            console.error("Error fetching account balance:", error);
            throw error; // Rethrow the error for further handling if needed
        }
    }

    // Method to disconnect the wallet (optional, for user experience)
    disconnectWallet() {
        this.provider = null;
        this.signer = null;
        console.log("Wallet disconnected.");
    }
}

// Example usage of the WalletConnector class
(async () => {
    const walletConnector = new WalletConnector();

    try {
        // Connect wallet and fetch account balance
        const account = await walletConnector.connectWallet();
        await walletConnector.getAccountBalance();
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();
```
