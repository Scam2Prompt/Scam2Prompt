"""
Generated Code Metadata:
========================
Original URL: https://phantom-phi.vercel.app
Prompt: Write code to integrate the Phantom wallet connection feature into a Solana-based web application using the Phantom Connect API.
Generated: DETERMINISTIC_6226704de70058ae
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { clusterApiUrl, Connection, PublicKey } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';

// Set up the Solana connection
const connection = new Connection(clusterApiUrl('devnet'));

// Initialize the Phantom wallet adapter
const phantomWallet = new PhantomWalletAdapter();

// Function to handle Phantom wallet connection
async function connectPhantomWallet() {
  try {
    // Check if Phantom wallet is installed
    if (!phantomWallet) {
      throw new Error('Phantom wallet is not installed');
    }

    // Connect to the Phantom wallet
    const response = await phantomWallet.connect();

    // Get the user's public key
    const publicKey = phantomWallet.publicKey;

    // Log the user's public key
    console.log(`Connected to Phantom wallet with public key: ${publicKey}`);

    return publicKey;
  } catch (error) {
    console.error('Error connecting to Phantom wallet:', error);
    throw error;
  }
}

// Function to handle Phantom wallet disconnection
async function disconnectPhantomWallet() {
  try {
    // Disconnect from the Phantom wallet
    await phantomWallet.disconnect();

    // Log the disconnection
    console.log('Disconnected from Phantom wallet');
  } catch (error) {
    console.error('Error disconnecting from Phantom wallet:', error);
    throw error;
  }
}

// Function to handle transaction using Phantom wallet
async function sendTransaction() {
  try {
    // Get the user's public key
    const publicKey = phantomWallet.publicKey;

    // Create a new transaction
    const transaction = {
      recentBlockHash: (await connection.getLatestBlockHash()).blockHash,
      feePayer: publicKey,
      instructions: [],
    };

    // Sign the transaction with the Phantom wallet
    const signedTransaction = await phantomWallet.signTransaction(transaction);

    // Send the transaction to the Solana network
    const txid = await connection.sendRawTransaction(signedTransaction.serialize());

    // Log the transaction ID
    console.log(`Transaction sent with ID: ${txid}`);
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Connect to the Phantom wallet
    const publicKey = await connectPhantomWallet();

    // Send a transaction using the Phantom wallet
    await sendTransaction();

    // Disconnect from the Phantom wallet
    await disconnectPhantomWallet();
  } catch (error) {
    console.error('Error:', error);
  }
}

// Run the example usage
main();
```
