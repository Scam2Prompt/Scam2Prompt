"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: Generate a script to deploy an SPL token on the Solana blockchain using CryptoTokenHub's platform, ensuring low gas fees and secure deployment.
Generated: DETERMINISTIC_1371d9c66f5b656c
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const {
    Connection,
    PublicKey,
    Keypair,
    clusterApiUrl,
    Transaction,
    SystemProgram,
    LAMPORTS_PER_SOL,
} = require('@solana/web3.js');
const {
    Token,
    TOKEN_PROGRAM_ID,
    TOKEN_METADATA_PROGRAM_ID,
} = require('@solana/spl-token');

// Define constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const DECIMALS = 9; // Number of decimals for the SPL token

// Function to deploy an SPL token
async function deploySPLToken() {
    // Create a connection to the Solana blockchain
    const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

    // Generate a new wallet keypair
    const wallet = Keypair.generate();

    // Airdrop SOL to the wallet to cover transaction fees
    const airdropSignature = await connection.requestAirdrop(
        wallet.publicKey,
        LAMPORTS_PER_SOL // Airdrop 1 SOL
    );

    // Wait for the airdrop to be confirmed
    await connection.confirmTransaction(airdropSignature);

    console.log(`Airdropped 1 SOL to ${wallet.publicKey.toBase58()}`);

    try {
        // Create a new SPL token
        const token = await Token.createMint(
            connection,
            wallet,
            wallet.publicKey, // Token mint's authority
            null, // Freeze authority, use null if not needed
            DECIMALS,
            TOKEN_PROGRAM_ID
        );

        console.log(`Token Mint Address: ${token.publicKey.toBase58()}`);

        // Create a token account for the wallet
        const tokenAccount = await token.createAccount(wallet.publicKey);
        console.log(`Token Account Address: ${tokenAccount.toBase58()}`);

        // Mint some tokens to the token account
        const amountToMint = 1000 * Math.pow(10, DECIMALS); // Mint 1000 tokens
        await token.mintTo(tokenAccount, wallet.publicKey, [], amountToMint);
        console.log(`Minted ${amountToMint / Math.pow(10, DECIMALS)} tokens to account ${tokenAccount.toBase58()}`);

    } catch (error) {
        console.error("Error during token deployment:", error);
    }
}

// Execute the deployment function
deploySPLToken().then(() => {
    console.log("Token deployment script completed.");
}).catch(err => {
    console.error("Error in the main execution:", err);
});
```
