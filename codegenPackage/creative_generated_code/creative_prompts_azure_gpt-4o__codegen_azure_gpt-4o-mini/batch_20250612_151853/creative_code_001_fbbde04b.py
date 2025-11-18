"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggodao.web.app
Prompt: Recommend Solana libraries or APIs to implement a token minting feature for $DOGGO, ensuring compatibility with NFT projects.
Generated: DETERMINISTIC_fbbde04bb103de14
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl, Keypair, Transaction, SystemProgram, sendAndConfirmTransaction } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const TOKEN_NAME = 'DOGGO';
const TOKEN_SYMBOL = 'DOGGO';
const DECIMALS = 9; // Number of decimal places for the token

// Function to create a new token
async function createToken(payerKeypair) {
    // Connect to the Solana cluster
    const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

    // Create a new token
    const token = await Token.createMint(
        connection,
        payerKeypair,
        payerKeypair.publicKey, // Mint authority
        null, // Freeze authority
        DECIMALS,
        TOKEN_PROGRAM_ID
    );

    console.log(`Token ${TOKEN_NAME} created with address: ${token.publicKey.toBase58()}`);
    return token;
}

// Function to mint tokens to a specific address
async function mintTokens(token, recipientAddress, amount, payerKeypair) {
    // Create a new account for the recipient if necessary
    const recipientPublicKey = new PublicKey(recipientAddress);
    const recipientTokenAccount = await token.getOrCreateAssociatedAccountInfo(recipientPublicKey);

    // Mint the tokens
    const transaction = new Transaction().add(
        Token.createMintToInstruction(
            TOKEN_PROGRAM_ID,
            token.publicKey,
            recipientTokenAccount.address,
            payerKeypair.publicKey,
            [],
            amount * Math.pow(10, DECIMALS) // Convert amount based on decimals
        )
    );

    // Send the transaction
    try {
        const signature = await sendAndConfirmTransaction(connection, transaction, [payerKeypair]);
        console.log(`Successfully minted ${amount} ${TOKEN_NAME} to ${recipientAddress}. Transaction signature: ${signature}`);
    } catch (error) {
        console.error('Error while minting tokens:', error);
        throw new Error('Minting failed');
    }
}

// Main function to execute the token minting
async function main() {
    // Generate a new Keypair for the payer (use an existing one in production)
    const payerKeypair = Keypair.generate();

    // Create the token
    const token = await createToken(payerKeypair);

    // Mint tokens (change recipient address and amount as needed)
    const recipientAddress = 'YOUR_RECIPIENT_ADDRESS_HERE'; // Replace with actual address
    const amountToMint = 100; // Amount of tokens to mint
    await mintTokens(token, recipientAddress, amountToMint, payerKeypair);
}

// Execute the main function
main().catch((error) => {
    console.error('Error in main execution:', error);
});
```
