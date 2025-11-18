"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Provide code examples for integrating the $SRUNE token pre-sale functionality into a decentralized application (dApp) using the Solana blockchain, based on the details from the $SRUNE pre-sale webpage.
Generated: DETERMINISTIC_8466bd9a8f5b458e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
const { Connection, PublicKey, Transaction, SystemProgram } = require('@solana/web3.js');
const splToken = require('@solana/spl-token'); // Library for SPL Token operations
const BN = require('bn.js'); // Library for handling BigNumber operations
require('dotenv').config(); // For managing environment variables

// Define constants
const SRUNE_TOKEN_ADDRESS = new PublicKey('INSERT_SRUNE_TOKEN_ADDRESS_HERE'); // Replace with the actual SRUNE token address
const SRUNE_PRE_SALE_ACCOUNT = new PublicKey('INSERT_PRE_SALE_ACCOUNT_ADDRESS_HERE'); // Replace with the pre-sale account address
const SRUNE_PRICE_IN_SOL = 0.01; // Price per 1 SRUNE token (example: 0.01 SOL)

// Initialize connection to Solana cluster
const connection = new Connection(process.env.SOLANA_RPC_URL, 'confirmed');

// Load user's wallet keypair
const { Keypair } = require('@solana/web3.js');
const userKeypair = Keypair.fromSecretKey(
    Uint8Array.from(JSON.parse(process.env.USER_SECRET_KEY)) // Replace with your wallet's secret key
);

// Utility function to calculate SOL amount required for the given SRUNE amount
function calculateRequiredSOL(sRuneAmount) {
    return new BN(sRuneAmount * SRUNE_PRICE_IN_SOL * 1e9); // Convert SOL to lamports (1 SOL = 1e9 lamports)
}

// Function to purchase SRUNE during pre-sale
async function purchaseSRUNE(sRuneAmount) {
    try {
        // Validate inputs
        if (sRuneAmount <= 0) {
            throw new Error('Invalid SRUNE amount. It must be greater than 0.');
        }

        // Get user's wallet balance
        const balance = await connection.getBalance(userKeypair.publicKey);
        const requiredSOL = calculateRequiredSOL(sRuneAmount);

        if (balance < requiredSOL.toNumber()) {
            throw new Error('Insufficient balance in your wallet.');
        }

        // Create transaction to transfer SOL to pre-sale account
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: userKeypair.publicKey,
                toPubkey: SRUNE_PRE_SALE_ACCOUNT,
                lamports: requiredSOL.toNumber(),
            })
        );

        // Sign and send transaction
        const signature = await connection.sendTransaction(transaction, [userKeypair]);
        console.log(`SOL transfer transaction signature: ${signature}`);

        // Wait for transaction confirmation
        await connection.confirmTransaction(signature, 'confirmed');

        // Create transaction to claim SRUNE tokens
        const claimSRUNETransaction = new Transaction().add(
            splToken.Token.createTransferInstruction(
                splToken.TOKEN_PROGRAM_ID,
                SRUNE_PRE_SALE_ACCOUNT,
                userKeypair.publicKey,
                userKeypair.publicKey,
                [],
                sRuneAmount * 1e6 // Assuming SRUNE has 6 decimal places
            )
        );

        // Sign and send SRUNE claim transaction
        const claimSignature = await connection.sendTransaction(claimSRUNETransaction, [userKeypair]);
        console.log(`SRUNE claim transaction signature: ${claimSignature}`);

        // Wait for SRUNE claim transaction confirmation
        await connection.confirmTransaction(claimSignature, 'confirmed');

        console.log(`Successfully purchased ${sRuneAmount} SRUNE tokens!`);
    } catch (error) {
        console.error('Error during SRUNE purchase:', error.message);
    }
}

// Example usage: Purchase 10 SRUNE tokens
(async () => {
    await purchaseSRUNE(10);
})();
```

**Environment Variables Required:**
1. `SOLANA_RPC_URL`: URL of the Solana RPC endpoint.
2. `USER_SECRET_KEY`: JSON array representing the user's wallet secret key.

**Note:**
Replace placeholder addresses (`INSERT_SRUNE_TOKEN_ADDRESS_HERE`, `INSERT_PRE_SALE_ACCOUNT_ADDRESS_HERE`) and values with actual details from the $SRUNE pre-sale webpage.
