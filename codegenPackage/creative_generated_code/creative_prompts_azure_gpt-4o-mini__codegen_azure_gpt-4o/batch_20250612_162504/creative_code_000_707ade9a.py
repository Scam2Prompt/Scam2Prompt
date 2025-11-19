"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-sale1.vercel.app
Prompt: How can I implement a token sale feature that allows users to select a wallet and specify the amount of BeyBlade (BBD) tokens to purchase at a price of 0.0500 SOL?
Generated: DETERMINISTIC_707ade9adaff67d1
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and libraries
const Web3 = require('@solana/web3.js'); // Solana Web3 library
const BN = require('bn.js'); // Library for handling big numbers

// Constants for token sale
const TOKEN_PRICE_SOL = 0.0500; // Price of one BeyBlade token in SOL
const TOKEN_DECIMALS = 9; // BeyBlade token decimals
const SELLER_PUBLIC_KEY = 'SELLER_PUBLIC_KEY_HERE'; // Replace with the token seller's public key

/**
 * Function to handle token sale
 * @param {string} buyerWallet - Public key of the buyer's wallet
 * @param {number} tokenAmount - Amount of tokens the buyer wants to purchase
 */
async function processTokenSale(buyerWallet, tokenAmount) {
    // Validate buyer wallet address
    if (!Web3.PublicKey.isOnCurve(buyerWallet)) {
        throw new Error('Invalid wallet address');
    }

    // Validate token amount
    if (tokenAmount <= 0 || !Number.isInteger(tokenAmount)) {
        throw new Error('Invalid token amount');
    }

    // Calculate total cost in SOL
    const totalCostSol = new BN(TOKEN_PRICE_SOL * tokenAmount * Math.pow(10, TOKEN_DECIMALS));

    try {
        // Connect to the Solana cluster
        const connection = new Web3.Connection(Web3.clusterApiUrl('mainnet-beta'), 'confirmed');

        // Create a transaction to transfer SOL from buyer to seller
        const transaction = new Web3.Transaction();
        transaction.add(
            Web3.SystemProgram.transfer({
                fromPubkey: new Web3.PublicKey(buyerWallet),
                toPubkey: new Web3.PublicKey(SELLER_PUBLIC_KEY),
                lamports: totalCostSol.toNumber(),
            })
        );

        // Sign and send the transaction
        const buyerAccount = Web3.Keypair.fromSecretKey(/* Insert buyer's secret key here */);
        await Web3.sendAndConfirmTransaction(connection, transaction, [buyerAccount]);

        console.log(`Transaction successful! ${tokenAmount} BeyBlade tokens purchased for ${totalCostSol.toNumber()} lamports.`);
    } catch (error) {
        // Handle errors that may occur during the transaction
        console.error('Error processing token sale:', error.message);
        throw new Error('Token sale failed. Please try again later.');
    }
}

// Example usage
(async () => {
    try {
        const buyerWallet = 'BUYER_PUBLIC_KEY_HERE'; // Replace with buyer's public key
        const tokenAmount = 10; // Example: Buyer wants to purchase 10 tokens

        await processTokenSale(buyerWallet, tokenAmount);
    } catch (error) {
        console.error(error.message);
    }
})();
```
