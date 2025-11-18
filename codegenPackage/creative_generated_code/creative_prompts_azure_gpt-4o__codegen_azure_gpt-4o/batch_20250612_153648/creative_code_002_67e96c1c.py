"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dust-21.web.app
Prompt: Provide an example of how to integrate Solflare wallet connection into a web application to claim DUST tokens.
Generated: DETERMINISTIC_67e96c1c0f87206d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { Connection, PublicKey, Transaction, clusterApiUrl } from '@solana/web3.js';
import { Solflare } from '@solflare-wallet/sdk';

// Constants
const SOLANA_NETWORK = 'mainnet-beta'; // Use 'mainnet-beta' for production
const DUST_TOKEN_MINT = new PublicKey('DUST_TOKEN_MINT_ADDRESS'); // Replace with the actual DUST token mint address
const CLAIM_PROGRAM_ID = new PublicKey('CLAIM_PROGRAM_ID'); // Replace with the actual claim program ID

// Initialize Solflare wallet instance
const solflare = new Solflare();

// Function to connect Solflare wallet
async function connectWallet() {
  try {
    // Detect if Solflare is available in the browser
    if (!solflare.isConnected) {
      await solflare.connect(); // Prompt user to connect the wallet
    }
    console.log('Wallet connected:', solflare.publicKey.toString());
  } catch (error) {
    console.error('Failed to connect wallet:', error);
  }
}

// Function to claim DUST tokens
async function claimDustTokens() {
  try {
    // Ensure wallet is connected
    if (!solflare.isConnected) {
      throw new Error('Wallet not connected.');
    }

    // Establish connection to Solana blockchain
    const connection = new Connection(clusterApiUrl(SOLANA_NETWORK));

    // Public key of the wallet
    const walletPublicKey = solflare.publicKey;

    // Build the transaction to claim DUST tokens
    const transaction = new Transaction().add({
      // Instruction to the claim program
      keys: [
        { pubkey: walletPublicKey, isSigner: true, isWritable: true }, // Wallet public key
        { pubkey: DUST_TOKEN_MINT, isSigner: false, isWritable: false }, // DUST token mint address
      ],
      programId: CLAIM_PROGRAM_ID, // Program ID handling DUST claims
    });

    // Set the recent blockhash and fee payer
    const { blockhash } = await connection.getLatestBlockhash();
    transaction.recentBlockhash = blockhash;
    transaction.feePayer = walletPublicKey;

    // Request wallet to sign the transaction
    const signedTransaction = await solflare.signTransaction(transaction);

    // Send the signed transaction to the blockchain
    const txId = await connection.sendRawTransaction(signedTransaction.serialize());
    console.log('Transaction sent. Tx ID:', txId);

    // Confirm the transaction
    await connection.confirmTransaction(txId, 'finalized');
    console.log('Transaction confirmed. DUST tokens claimed.');
  } catch (error) {
    console.error('Failed to claim DUST tokens:', error);
  }
}

// Example usage
// Call connectWallet() when user clicks "Connect Wallet" button
// Call claimDustTokens() when user clicks "Claim DUST Tokens" button
```

Replace the `DUST_TOKEN_MINT_ADDRESS` and `CLAIM_PROGRAM_ID` with actual values corresponding to the DUST token mint and the program ID responsible for handling the token claim process on the Solana blockchain.
