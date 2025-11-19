"""
Generated Code Metadata:
========================
Original URL: https://sh-haweng12s-projects.vercel.app
Prompt: Provide a code example for initializing a Solana wallet connection and handling transactions, inspired by the "TES tes Connect Wallet" feature.
Generated: DETERMINISTIC_003bf6a72c0acf02
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from Solana Web3.js
import {
    Connection,
    PublicKey,
    clusterApiUrl,
    Keypair,
    Transaction,
    SystemProgram,
    sendAndConfirmTransaction,
} from '@solana/web3.js';

// Define the Solana network to connect to
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Function to create a new wallet
const createWallet = () => {
    // Generate a new keypair
    const wallet = Keypair.generate();
    console.log('New wallet created:', wallet.publicKey.toString());
    return wallet;
};

// Function to get the balance of a wallet
const getWalletBalance = async (publicKey) => {
    try {
        const balance = await connection.getBalance(new PublicKey(publicKey));
        console.log(`Wallet balance: ${balance / 1e9} SOL`); // Convert lamports to SOL
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
};

// Function to send SOL from one wallet to another
const sendSol = async (fromWallet, toPublicKey, amount) => {
    try {
        // Create a transaction
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: fromWallet.publicKey,
                toPubkey: new PublicKey(toPublicKey),
                lamports: amount * 1e9, // Convert SOL to lamports
            })
        );

        // Send and confirm the transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, [fromWallet]);
        console.log('Transaction successful with signature:', signature);
    } catch (error) {
        console.error('Error sending SOL:', error);
    }
};

// Example usage
(async () => {
    // Create a new wallet
    const myWallet = createWallet();

    // Get balance of the new wallet
    await getWalletBalance(myWallet.publicKey);

    // Example recipient wallet (replace with a valid public key)
    const recipientWallet = 'RecipientPublicKeyHere';

    // Send 0.01 SOL to the recipient
    await sendSol(myWallet, recipientWallet, 0.01);
})();
```
