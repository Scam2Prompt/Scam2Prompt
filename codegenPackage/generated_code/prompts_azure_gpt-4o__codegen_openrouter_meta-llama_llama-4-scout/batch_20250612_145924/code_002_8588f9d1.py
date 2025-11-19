"""
Generated Code Metadata:
========================
Original URL: https://slothanacoin.pages.dev
Prompt: Generate code to interact with the Solana blockchain to connect a wallet, send SOL to a specific address, and retrieve transaction details for the $SLOTH presale.
Generated: DETERMINISTIC_8588f9d13068b2c0
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, clusterApiUrl, Keypair, Transaction, SystemProgram, PublicKey } = require('@solana/web3.js');
const bs58 = require('bs58');

// Set up the Solana connection
const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

/**
 * Connects to a Solana wallet.
 * @param {string} mnemonic - The wallet's mnemonic phrase.
 * @returns {Keypair} The wallet's keypair.
 */
function connectWallet(mnemonic) {
    try {
        // Derive the keypair from the mnemonic phrase
        const seed = mnemonic.split(' ').map(word => Buffer.from(word, 'utf8'));
        const keypair = Keypair.fromSeed(Buffer.concat(seed));

        return keypair;
    } catch (error) {
        console.error('Error connecting wallet:', error);
        throw error;
    }
}

/**
 * Sends SOL to a specific address.
 * @param {Keypair} senderKeypair - The sender's wallet keypair.
 * @param {string} recipientAddress - The recipient's address.
 * @param {number} amount - The amount of SOL to send.
 * @returns {string} The transaction ID.
 */
async function sendSol(senderKeypair, recipientAddress, amount) {
    try {
        // Get the current blockhash
        const { blockhash } = await connection.getLatestBlockHash();

        // Create a new transaction
        const transaction = new Transaction({ feePayer: senderKeypair.publicKey, recentBlockHash: blockhash });

        // Add the transfer instruction
        transaction.add(SystemProgram.transfer({
            fromPubkey: senderKeypair.publicKey,
            toPubkey: new PublicKey(recipientAddress),
            lamports: amount * 1e9, // Convert SOL to lamports
        }));

        // Sign the transaction
        transaction.sign(senderKeypair);

        // Send the transaction
        const txid = await connection.sendTransaction(transaction);

        return txid.toString();
    } catch (error) {
        console.error('Error sending SOL:', error);
        throw error;
    }
}

/**
 * Retrieves transaction details for the $SLOTH presale.
 * @param {string} address - The address of the presale.
 * @param {number} [limit=10] - The number of transactions to retrieve.
 * @returns {object[]} An array of transaction details.
 */
async function getTransactionDetails(address, limit = 10) {
    try {
        // Get the transaction signatures
        const signatures = await connection.getSignaturesForAddress(new PublicKey(address), { limit });

        // Get the transaction details
        const transactions = await Promise.all(signatures.map(async signature => {
            const transaction = await connection.getTransaction(signature.signature);
            return transaction;
        }));

        return transactions;
    } catch (error) {
        console.error('Error retrieving transaction details:', error);
        throw error;
    }
}

// Example usage
async function main() {
    // Connect to a wallet
    const mnemonic = 'your mnemonic phrase here';
    const wallet = connectWallet(mnemonic);
    console.log('Wallet address:', wallet.publicKey.toString());

    // Send SOL to a specific address
    const recipientAddress = 'recipient address here';
    const amount = 1; // SOL
    const txid = await sendSol(wallet, recipientAddress, amount);
    console.log('Transaction ID:', txid);

    // Retrieve transaction details for the $SLOTH presale
    const slothPresaleAddress = 'sloth presale address here';
    const transactionDetails = await getTransactionDetails(slothPresaleAddress);
    console.log('Transaction details:', transactionDetails);
}

main().catch(error => {
    console.error('Error:', error);
    process.exit(1);
});
```
