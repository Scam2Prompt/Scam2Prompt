"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-illuvium.com
Prompt: Generate code to integrate Solana blockchain functionality into a dapp using the latest MetaMask extension version.
Generated: DETERMINISTIC_511ba9426fbc2a20
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// solana-dapp.js

// Import necessary modules
// Note: MetaMask does not directly integrate with Solana; Solana wallets like Phantom are used instead.
// We'll use the Solana Web3.js library for blockchain interactions and assume Phantom Wallet extension.

import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';

// Constants
const SOLANA_NETWORK = "mainnet-beta"; // Use "devnet", "testnet", or "mainnet-beta"
const CONNECTION_URL = clusterApiUrl(SOLANA_NETWORK); // Cluster URL based on the selected network
const connection = new Connection(CONNECTION_URL, "confirmed");

// Helper function to connect to Phantom Wallet
async function connectWallet() {
  try {
    // Check if the Phantom wallet is installed
    const provider = window.solana;
    if (!provider || !provider.isPhantom) {
      throw new Error("Phantom Wallet is not installed. Please install it to continue.");
    }

    // Connect to the wallet
    const response = await provider.connect();
    console.log("Wallet connected successfully:", response.publicKey.toString());
    return response.publicKey;
  } catch (error) {
    console.error("Failed to connect wallet:", error.message);
    throw error;
  }
}

// Function to fetch the balance of a connected wallet
async function getWalletBalance(publicKey) {
  try {
    // Fetch balance in lamports (smallest unit in Solana)
    const balance = await connection.getBalance(publicKey);
    // Convert lamports to SOL (1 SOL = 1,000,000,000 lamports)
    const solBalance = balance / 1_000_000_000;
    console.log(`Wallet Balance: ${solBalance} SOL`);
    return solBalance;
  } catch (error) {
    console.error("Error fetching wallet balance:", error.message);
    throw error;
  }
}

// Example: Send SOL from one wallet to another
async function sendSol(fromWallet, toWalletAddress, amountInSol) {
  try {
    // Validate inputs
    if (!fromWallet || !toWalletAddress || amountInSol <= 0) {
      throw new Error("Invalid transaction parameters.");
    }

    const toWallet = new PublicKey(toWalletAddress);
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: fromWallet.publicKey,
        toPubkey: toWallet,
        lamports: amountInSol * 1_000_000_000, // Convert SOL to lamports
      })
    );

    // Sign and send the transaction
    const signature = await connection.sendTransaction(transaction, [fromWallet], {
      skipPreflight: false,
      preflightCommitment: "confirmed",
    });

    console.log("Transaction successful. Signature:", signature);
    return signature;
  } catch (error) {
    console.error("Transaction failed:", error.message);
    throw error;
  }
}

// Main function to demonstrate functionality
async function main() {
  try {
    console.log("Connecting to Phantom Wallet...");
    const publicKey = await connectWallet();

    console.log("Fetching wallet balance...");
    await getWalletBalance(publicKey);

    // Example: Sending SOL (uncomment and edit with valid values to test)
    // const recipient = "<Recipient Wallet Address>";
    // await sendSol(publicKey, recipient, 0.01); // Send 0.01 SOL
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

// Execute the main function
main();
```

**Dependencies:**
Install `@solana/web3.js`:
```bash
npm install @solana/web3.js
```

**Note:**
MetaMask is primarily for Ethereum-based applications, and Phantom Wallet is the recommended extension for Solana-based dApps. This code assumes you're using Phantom.
