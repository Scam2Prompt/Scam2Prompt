"""
Generated Code Metadata:
========================
Original URL: https://dialect-c15.pages.dev
Prompt: Write a code example of how to use the Actions API to participate in governance on the Solana blockchain, and discuss the importance of signable transactions and messages.
Generated: DETERMINISTIC_eb8be413cf1ac4e6
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, clusterApiUrl } = require('@solana/web3.js');

// Set up a connection to the Solana blockchain
async function establishConnection() {
    try {
        // Establish a connection to the Solana blockchain
        const connection = new Connection(clusterApiUrl('devnet'));
        console.log('Connected to Solana blockchain');
        return connection;
    } catch (error) {
        console.error('Error establishing connection:', error);
        throw error;
    }
}

// Create a new program-derived address
async function createProgramDerivedAddress(programId, seeds) {
    try {
        // Create a new program-derived address
        const [derivedAddress, bump] = await PublicKey.findProgramAddress(seeds, programId);
        return { derivedAddress, bump };
    } catch (error) {
        console.error('Error creating program-derived address:', error);
        throw error;
    }
}

// Create a signable transaction
async function createSignableTransaction(connection, programId, account, instructions) {
    try {
        // Create a new transaction
        const transaction = new Transaction();

        // Add instructions to the transaction
        instructions.forEach(instruction => transaction.add(instruction));

        // Set the recent block hash
        transaction.recentBlockHash = await connection.getLatestBlockHash();

        // Set the fee payer
        transaction.feePayer = account.publicKey;

        return transaction;
    } catch (error) {
        console.error('Error creating signable transaction:', error);
        throw error;
    }
}

// Sign a transaction
async function signTransaction(transaction, account) {
    try {
        // Sign the transaction
        const signedTransaction = await account.signTransaction(transaction);
        return signedTransaction;
    } catch (error) {
        console.error('Error signing transaction:', error);
        throw error;
    }
}

// Send a transaction
async function sendTransaction(connection, transaction) {
    try {
        // Send the transaction
        const signature = await connection.sendTransaction(transaction);
        console.log('Transaction sent:', signature);
        return signature;
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw error;
    }
}

// Main function
async function main() {
    try {
        // Establish a connection to the Solana blockchain
        const connection = await establishConnection();

        // Set up a program ID
        const programId = new PublicKey('11111111111111111111111111111111');

        // Set up an account
        const account = {
            publicKey: new PublicKey('11111111111111111111111111111111'),
            signTransaction: async (transaction) => {
                // Sign the transaction with the account's secret key
                // NOTE: In a real application, use a secure method to store and retrieve the secret key
                const secretKey = new Uint8Array([/* secret key */]);
                const signedTransaction = transaction.sign(secretKey);
                return signedTransaction;
            }
        };

        // Create a new program-derived address
        const seeds = [Buffer.from('seed')];
        const { derivedAddress } = await createProgramDerivedAddress(programId, seeds);

        // Create instructions for the transaction
        const instructions = [
            // Example instruction
            {
                programId,
                data: Buffer.from('instruction data'),
                keys: [
                    {
                        pubkey: account.publicKey,
                        isSigner: true,
                        isWritable: true
                    },
                    {
                        pubkey: derivedAddress,
                        isSigner: false,
                        isWritable: true
                    }
                ]
            }
        ];

        // Create a signable transaction
        const transaction = await createSignableTransaction(connection, programId, account, instructions);

        // Sign the transaction
        const signedTransaction = await signTransaction(transaction, account);

        // Send the transaction
        await sendTransaction(connection, signedTransaction);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Run the main function
main();
```
