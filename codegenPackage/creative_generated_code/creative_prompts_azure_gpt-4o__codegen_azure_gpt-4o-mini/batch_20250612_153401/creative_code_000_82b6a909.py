"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-drain.vercel.app
Prompt: Write a Solana blockchain-based script to mint a custom token named "$NET" with a total supply of 100,000,000, as described on the website. Include wallet connection functionality.
Generated: DETERMINISTIC_82b6a90919325aea
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and modules
import { Connection, Keypair, PublicKey, clusterApiUrl } from '@solana/web3.js';
import {
    Token,
    TOKEN_PROGRAM_ID,
    AccountLayout,
    createMint,
    createAccount,
    mintTo,
} from '@solana/spl-token';

// Define constants
const TOTAL_SUPPLY = 100_000_000; // Total supply of the token
const TOKEN_NAME = "$NET"; // Token name
const DECIMALS = 9; // Number of decimals for the token
const NETWORK = clusterApiUrl('devnet'); // Change to 'mainnet-beta' for production

// Connect to the Solana blockchain
const connection = new Connection(NETWORK, 'confirmed');

// Function to create a new token mint
async function createTokenMint(userKeypair) {
    try {
        // Create a new mint
        const mint = await createMint(
            connection,
            userKeypair,
            userKeypair.publicKey,
            null,
            DECIMALS,
            TOKEN_PROGRAM_ID
        );

        // Create an associated token account for the user
        const userTokenAccount = await createAccount(
            connection,
            userKeypair,
            mint,
            userKeypair.publicKey
        );

        // Mint tokens to the user's token account
        await mintTo(
            connection,
            userKeypair,
            mint,
            userTokenAccount,
            userKeypair.publicKey,
            TOTAL_SUPPLY * Math.pow(10, DECIMALS) // Total supply adjusted for decimals
        );

        console.log(`Token Minted: ${mint.toBase58()}`);
        console.log(`User Token Account: ${userTokenAccount.toBase58()}`);
    } catch (error) {
        console.error("Error creating token mint:", error);
    }
}

// Main function to execute the minting process
(async () => {
    // Generate a random user keypair
    const userKeypair = Keypair.generate();
    
    // Display user wallet address
    console.log(`User Wallet Address: ${userKeypair.publicKey.toBase58()}`);

    // Create the token mint
    await createTokenMint(userKeypair);
})();
```
