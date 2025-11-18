"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-fork-marekhauzr-main-419labs.vercel.app
Prompt: Generate code to integrate a StarkNet wallet into a GameFi application, using the StarkNet ecosystem's wallet tools.
Generated: DETERMINISTIC_cb1920c5c9859bbf
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from StarkNet ecosystem
import { Wallet, Provider, utils } from 'starknet';

// Initialize the StarkNet wallet
class StarkNetWallet {
    constructor() {
        this.wallet = null; // Wallet instance
        this.provider = new Provider(); // Initialize provider
    }

    /**
     * Connect to the StarkNet wallet.
     * Throws an error if the wallet connection fails.
     */
    async connect() {
        try {
            // Check if a wallet is available
            if (!window.starknet) {
                throw new Error('StarkNet wallet not found. Please install one.');
            }

            // Connect to the wallet
            this.wallet = await window.starknet.request({ method: 'wallet_requestAccounts' });
            console.log('Connected to StarkNet wallet:', this.wallet);
        } catch (error) {
            console.error('Failed to connect to StarkNet wallet:', error);
            throw new Error('Wallet connection error: ' + error.message);
        }
    }

    /**
     * Get the connected wallet address.
     * Returns the address of the connected wallet or null if not connected.
     * 
     * @returns {string|null} The wallet address or null.
     */
    getWalletAddress() {
        return this.wallet ? this.wallet[0] : null;
    }

    /**
     * Sign a transaction with the connected wallet.
     * 
     * @param {string} transaction - The transaction data to sign.
     * @returns {Promise<string>} The signed transaction.
     */
    async signTransaction(transaction) {
        if (!this.wallet) {
            throw new Error('Wallet is not connected. Please connect first.');
        }

        try {
            const signedTransaction = await window.starknet.request({
                method: 'wallet_signTransaction',
                params: { transaction }
            });
            return signedTransaction;
        } catch (error) {
            console.error('Failed to sign transaction:', error);
            throw new Error('Transaction signing error: ' + error.message);
        }
    }

    /**
     * Disconnect the wallet.
     * Resets the wallet instance and logs out the user.
     */
    disconnect() {
        this.wallet = null;
        console.log('Disconnected from StarkNet wallet');
    }
}

// Usage example
(async () => {
    const starkNetWallet = new StarkNetWallet();

    try {
        // Connect to the wallet
        await starkNetWallet.connect();

        // Get connected wallet address
        const address = starkNetWallet.getWalletAddress();
        console.log('Wallet address:', address);

        // Example transaction (replace with actual transaction data)
        const transaction = {
            from: address,
            to: '0xrecipientAddress',
            value: utils.toHex(1), // Sending 1 unit
        };

        // Sign the transaction
        const signedTx = await starkNetWallet.signTransaction(transaction);
        console.log('Signed transaction:', signedTx);

        // Disconnect from the wallet after operations are complete
        starkNetWallet.disconnect();
    } catch (error) {
        console.error('Error in StarkNet wallet operations:', error);
    }
})();
```
