"""
Generated Code Metadata:
========================
Original URL: https://soljack.com
Prompt: Develop a JavaScript function to handle Solana transactions for betting and payouts in a crypto gambling app like SolJack.
Generated: DETERMINISTIC_febbc3b861bab0e3
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { Connection, PublicKey, Transaction, SystemProgram, Keypair, sendAndConfirmTransaction } = require('@solana/web3.js');

/**
 * Handles placing a bet on Solana blockchain
 * @param {string} rpcUrl - Solana RPC endpoint URL
 * @param {Keypair} userKeypair - User's keypair for signing transaction
 * @param {string} houseWallet - House wallet public key
 * @param {number} amount - Amount to bet in lamports
 * @param {string} memo - Optional memo for the transaction
 * @returns {Promise<string>} Transaction signature
 */
async function placeBet(rpcUrl, userKeypair, houseWallet, amount, memo = '') {
    try {
        const connection = new Connection(rpcUrl, 'confirmed');
        const housePublicKey = new PublicKey(houseWallet);
        
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: userKeypair.publicKey,
                toPubkey: housePublicKey,
                lamports: amount,
            }),
            ...(memo ? [new TransactionInstruction({
                keys: [],
                programId: new PublicKey('MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr'),
                data: Buffer.from(memo, 'utf-8'),
            })] : [])
        );

        const signature = await sendAndConfirmTransaction(
            connection,
            transaction,
            [userKeypair]
        );

        return signature;
    } catch (error) {
        console.error('Error placing bet:', error);
        throw new Error('Failed to place bet');
    }
}

/**
 * Handles payout to winner on Solana blockchain
 * @param {string} rpcUrl - Solana RPC endpoint URL
 * @param {Keypair} houseKeypair - House keypair for signing transaction
 * @param {string} winnerWallet - Winner's wallet public key
 * @param {number} amount - Amount to payout in lamports
 * @param {string} memo - Optional memo for the transaction
 * @returns {Promise<string>} Transaction signature
 */
async function payoutWinner(rpcUrl, houseKeypair, winnerWallet, amount, memo = '') {
    try {
        const connection = new Connection(rpcUrl, 'confirmed');
        const winnerPublicKey = new PublicKey(winnerWallet);
        
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: houseKeypair.publicKey,
                toPubkey: winnerPublicKey,
                lamports: amount,
            }),
            ...(memo ? [new TransactionInstruction({
                keys: [],
                programId: new PublicKey('MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr'),
                data: Buffer.from(memo, 'utf-8'),
            })] : [])
        );

        const signature = await sendAndConfirmTransaction(
            connection,
            transaction,
            [houseKeypair]
        );

        return signature;
    } catch (error) {
        console.error('Error processing payout:', error);
        throw new Error('Failed to process payout');
    }
}

/**
 * Verifies a transaction on Solana blockchain
 * @param {string} rpcUrl - Solana RPC endpoint URL
 * @param {string} txSignature - Transaction signature to verify
 * @returns {Promise<boolean>} True if transaction is confirmed and valid
 */
async function verifyTransaction(rpcUrl, txSignature) {
    try {
        const connection = new Connection(rpcUrl, 'confirmed');
        const tx = await connection.getTransaction(txSignature);
        return tx !== null && tx.meta?.err === null;
    } catch (error) {
        console.error('Error verifying transaction:', error);
        throw new Error('Failed to verify transaction');
    }
}

module.exports = {
    placeBet,
    payoutWinner,
    verifyTransaction
};
```
