"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detto.finance
Prompt: Generate a step-by-step guide for implementing wallet connection in a decentralized application using Web3Modal, referencing the functionality of Detto Finance.
Generated: DETERMINISTIC_af721229ea2af1fd
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import Web3 from 'web3';
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

/**
 * WalletConnector class to handle wallet connection.
 */
class WalletConnector {
    constructor() {
        // Create a web3 modal instance
        this.web3Modal = new Web3Modal({
            cacheProvider: false, // Set to true to cache provider on page reload
            providerOptions: {} // Pass provider options if needed
        });
        this.provider = null; // Wallet provider
        this.web3 = null; // Web3 instance
        this.signer = null; // Signer for transactions
    }

    /**
     * Connect to the wallet.
     * @returns {Promise<void>} - A promise that resolves when the wallet is connected.
     * @throws {Error} - Throws an error if connection fails.
     */
    async connectWallet() {
        try {
            // Open modal to select wallet
            this.provider = await this.web3Modal.connect();
            // Create a web3 instance with the provider
            this.web3 = new Web3(this.provider);
            // Get the signer from the provider
            this.signer = new ethers.providers.Web3Provider(this.provider).getSigner();

            console.log('Wallet connected successfully');
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            throw new Error('Failed to connect wallet');
        }

        // Optionally, you can add event listeners for provider updates
        this.provider.on("accountsChanged", (accounts) => {
            console.log('Accounts changed:', accounts);
            // Handle account change
        });

        this.provider.on("chainChanged", (chainId) => {
            console.log('Chain changed:', chainId);
            // Handle chain change
        });

        this.provider.on("disconnect", async (error) => {
            console.log('Disconnected:', error);
            // Handle disconnection
        });
    }

    /**
     * Get the connected account.
     * @returns {Promise<string>} - The connected account address.
     * @throws {Error} - Throws an error if no account is connected.
     */
    async getAccount() {
        if (!this.signer) {
            throw new Error('No wallet connected');
        }

        const account = await this.signer.getAddress();
        return account;
    }
}

// Usage Example
(async () => {
    const walletConnector = new WalletConnector();
    try {
        await walletConnector.connectWallet();
        const account = await walletConnector.getAccount();
        console.log('Connected account:', account);
    } catch (error) {
        console.error('Error during wallet connection:', error);
    }
})();
```
