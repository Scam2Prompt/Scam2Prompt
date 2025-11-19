"""
Generated Code Metadata:
========================
Original URL: https://boxesxsol.web.app
Prompt: Develop code to manage Solana wallets, including depositing funds from the main wallet to the trading wallet and withdrawing funds back, as outlined on the webpage.
Generated: DETERMINISTIC_6881e0c8bd2eed77
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, clusterApiUrl, sendAndConfirmTransaction } = require('@solana/web3.js');

// Set up constants
const MAIN_WALLET_ADDRESS = 'MAIN_WALLET_ADDRESS_HERE';
const TRADING_WALLET_ADDRESS = 'TRADING_WALLET_ADDRESS_HERE';
const SOLANA_NETWORK = clusterApiUrl('devnet'); // Change to 'mainnet-beta' for production

// Set up wallet connection
const connection = new Connection(SOLANA_NETWORK);

/**
 * Deposit funds from main wallet to trading wallet
 * @param {number} amount - Amount of SOL to deposit
 */
async function depositFunds(amount) {
    try {
        // Get main and trading wallet public keys
        const mainWalletPublicKey = new PublicKey(MAIN_WALLET_ADDRESS);
        const tradingWalletPublicKey = new PublicKey(TRADING_WALLET_ADDRESS);

        // Create transaction
        const transaction = new Transaction();
        transaction.recentBlockHash = await connection.getLatestBlockHash();

        // Add instruction to transfer SOL
        transaction.add(
            require('@solana/web3.js').SystemProgram.transfer({
                fromPubkey: mainWalletPublicKey,
                toPubkey: tradingWalletPublicKey,
                lamports: amount * 1e9, // Convert SOL to lamports
            })
        );

        // Sign transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, [mainWalletPublicKey]);

        console.log(`Deposited ${amount} SOL into trading wallet. Transaction signature: ${signature}`);
    } catch (error) {
        console.error('Error depositing funds:', error);
    }
}

/**
 * Withdraw funds from trading wallet to main wallet
 * @param {number} amount - Amount of SOL to withdraw
 */
async function withdrawFunds(amount) {
    try {
        // Get main and trading wallet public keys
        const mainWalletPublicKey = new PublicKey(MAIN_WALLET_ADDRESS);
        const tradingWalletPublicKey = new PublicKey(TRADING_WALLET_ADDRESS);

        // Create transaction
        const transaction = new Transaction();
        transaction.recentBlockHash = await connection.getLatestBlockHash();

        // Add instruction to transfer SOL
        transaction.add(
            require('@solana/web3.js').SystemProgram.transfer({
                fromPubkey: tradingWalletPublicKey,
                toPubkey: mainWalletPublicKey,
                lamports: amount * 1e9, // Convert SOL to lamports
            })
        );

        // Sign transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, [tradingWalletPublicKey]);

        console.log(`Withdrew ${amount} SOL from trading wallet. Transaction signature: ${signature}`);
    } catch (error) {
        console.error('Error withdrawing funds:', error);
    }
}

// Example usage
async function main() {
    // Deposit 1 SOL into trading wallet
    await depositFunds(1);

    // Withdraw 0.5 SOL from trading wallet
    await withdrawFunds(0.5);
}

main();
```
