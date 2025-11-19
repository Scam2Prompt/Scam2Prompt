"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockappsnode.com
Prompt: What are the best practices for implementing self-custodial features in a Web3 application?
Generated: DETERMINISTIC_f19f61907033db07
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Self-Custodial Wallet Implementation for a Web3 Application
 * This module provides features for creating, managing, and using a self-custodial wallet.
 * It leverages ethers.js library for Ethereum blockchain interactions.
 */

const { ethers } = require('ethers');

/**
 * WalletManager class to handle self-custodial wallet operations.
 */
class WalletManager {
    constructor() {
        this.wallet = null;
    }

    /**
     * Create a new wallet
     * @returns {string} - The wallet's mnemonic phrase
     */
    createWallet() {
        // Generate a random wallet
        const randomWallet = ethers.Wallet.createRandom();
        this.wallet = randomWallet;
        return randomWallet.mnemonic.phrase;
    }

    /**
     * Restore a wallet from a mnemonic phrase
     * @param {string} mnemonic - The mnemonic phrase to restore
     * @throws {Error} - Throws an error if the mnemonic is invalid
     */
    restoreWallet(mnemonic) {
        if (!ethers.utils.HDNode.isValidMnemonic(mnemonic)) {
            throw new Error('Invalid mnemonic phrase provided');
        }
        this.wallet = ethers.Wallet.fromMnemonic(mnemonic);
    }

    /**
     * Get the wallet address
     * @returns {string|null} - The wallet address or null if wallet is not created/restored
     */
    getAddress() {
        return this.wallet ? this.wallet.address : null;
    }

    /**
     * Send Ether from the wallet to another address
     * @param {string} to - The recipient's address
     * @param {number} amount - Amount of Ether to send (in Ether)
     * @throws {Error} - Throws an error if transaction fails
     */
    async sendEther(to, amount) {
        if (!this.wallet) {
            throw new Error('Wallet is not created or restored');
        }

        // Connect to a provider (e.g., Infura, Alchemy, or your own node)
        const provider = ethers.getDefaultProvider('mainnet');
        const walletWithProvider = this.wallet.connect(provider);

        // Convert Ether amount to Wei
        const weiAmount = ethers.utils.parseEther(amount.toString());

        try {
            const transaction = await walletWithProvider.sendTransaction({
                to: to,
                value: weiAmount,
            });
            await transaction.wait(); // Wait for the transaction to be mined
            return transaction;
        } catch (error) {
            throw new Error(`Transaction failed: ${error.message}`);
        }
    }

    /**
     * Get the balance of the wallet
     * @returns {Promise<string>} - The balance in Ether
     */
    async getBalance() {
        if (!this.wallet) {
            throw new Error('Wallet is not created or restored');
        }

        // Connect to a provider
        const provider = ethers.getDefaultProvider('mainnet');
        const balance = await provider.getBalance(this.wallet.address);
        return ethers.utils.formatEther(balance);
    }
}

// Example usage
(async () => {
    try {
        const walletManager = new WalletManager();
        
        // Create a new wallet
        const mnemonic = walletManager.createWallet();
        console.log('Mnemonic:', mnemonic);
        console.log('Wallet Address:', walletManager.getAddress());

        // Get balance
        const balance = await walletManager.getBalance();
        console.log('Balance:', balance, 'ETH');

        // Send Ether (replace with an actual address and amount)
        // const transaction = await walletManager.sendEther('recipient_address', 0.01);
        // console.log('Transaction:', transaction);
        
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
```
