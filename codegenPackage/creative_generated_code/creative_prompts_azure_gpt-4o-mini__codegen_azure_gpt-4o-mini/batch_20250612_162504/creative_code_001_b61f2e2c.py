"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-09.web.app
Prompt: Write a code snippet that demonstrates how to interact with the DustLabs SPL token using Solana's web3.js library.
Generated: DETERMINISTIC_b61f2e2c9ff4500c
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const {
    Connection,
    clusterApiUrl,
    Keypair,
    PublicKey,
    SystemProgram,
    Transaction,
    sendAndConfirmTransaction,
} = require('@solana/web3.js');
const {
    Token,
    TOKEN_PROGRAM_ID,
    TOKEN_METADATA_PROGRAM_ID,
} = require('@solana/spl-token');

// Constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production use
const CONNECTION = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Function to create and mint an SPL token
async function createAndMintSPLToken(ownerKeypair) {
    try {
        // Create a new token
        const mint = await Token.createMint(
            CONNECTION,
            ownerKeypair,
            ownerKeypair.publicKey,
            null,
            9, // Decimals
            TOKEN_PROGRAM_ID
        );

        console.log(`Token Mint Address: ${mint.publicKey.toBase58()}`);

        // Create a token account for the owner
        const tokenAccount = await mint.getOrCreateAssociatedAccountInfo(ownerKeypair.publicKey);

        // Mint 1000 tokens to the token account
        const mintAmount = 1000 * 10 ** mint.decimals;
        await mint.mintTo(tokenAccount.address, ownerKeypair.publicKey, [], mintAmount);

        console.log(`Minted ${mintAmount} tokens to ${tokenAccount.address.toBase58()}`);
        
        return { mint: mint.publicKey, tokenAccount: tokenAccount.address };
    } catch (error) {
        console.error("Error creating or minting SPL Token:", error);
        throw error; // Rethrow error for further handling if needed
    }
}

// Main function to execute the token creation
(async () => {
    // Generate a new keypair for the owner (In production, securely manage your keys)
    const ownerKeypair = Keypair.generate();

    // Fund the owner wallet if needed (for devnet)
    const airdropSignature = await CONNECTION.requestAirdrop(
        ownerKeypair.publicKey,
        2 * 1e9 // 2 SOL
    );
    
    // Confirm the airdrop
    await CONNECTION.confirmTransaction(airdropSignature);

    console.log(`Owner Wallet Public Key: ${ownerKeypair.publicKey.toBase58()}`);

    // Create and mint SPL token
    const { mint, tokenAccount } = await createAndMintSPLToken(ownerKeypair);
    
    console.log(`Token Account Address: ${tokenAccount.toBase58()}`);
})().catch(err => {
    console.error("Error in main function:", err);
});
```
