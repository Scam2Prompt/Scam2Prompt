"""
Generated Code Metadata:
========================
Original URL: https://peng-six.vercel.app
Prompt: Generate code to mint $PENG tokens on the Solana blockchain and freeze liquidity, referencing the token's unique properties.
Generated: DETERMINISTIC_9508e5b3258b70f5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from the Solana web3.js and spl-token packages
const {
    Connection,
    Keypair,
    PublicKey,
    clusterApiUrl,
    Transaction,
    sendAndConfirmTransaction,
} = require('@solana/web3.js');
const {
    Token,
    TOKEN_PROGRAM_ID,
    TOKEN_METADATA_PROGRAM_ID,
} = require('@solana/spl-token');

// Define constants for the Solana cluster and token properties
const SOLANA_CLUSTER = 'devnet'; // Change to 'mainnet-beta' for production
const TOKEN_NAME = 'PENG';
const TOKEN_SYMBOL = 'PENG';
const TOKEN_DECIMALS = 9; // Number of decimal places for the token
const INITIAL_SUPPLY = 1000000 * (10 ** TOKEN_DECIMALS); // Initial supply of tokens

// Function to create a new token and freeze its liquidity
async function mintPengToken() {
    // Establish a connection to the Solana cluster
    const connection = new Connection(clusterApiUrl(SOLANA_CLUSTER), 'confirmed');

    // Generate a new keypair for the token mint
    const mintKeypair = Keypair.generate();

    // Create a new wallet for the token owner
    const ownerKeypair = Keypair.generate();

    try {
        // Create the token mint
        const token = await Token.createMint(
            connection,
            ownerKeypair,
            ownerKeypair.publicKey,
            null,
            TOKEN_DECIMALS,
            TOKEN_PROGRAM_ID
        );

        // Mint the initial supply of tokens to the owner's wallet
        await token.mintTo(
            ownerKeypair.publicKey,
            ownerKeypair.publicKey,
            [],
            INITIAL_SUPPLY
        );

        console.log(`Successfully minted ${INITIAL_SUPPLY} ${TOKEN_NAME} tokens to ${ownerKeypair.publicKey.toBase58()}`);

        // Freeze the token's liquidity by creating a freeze authority
        await token.setAuthority(
            mintKeypair.publicKey,
            null,
            'MintTokens',
            ownerKeypair.publicKey,
            []
        );

        console.log(`Liquidity for ${TOKEN_NAME} tokens has been frozen.`);
    } catch (error) {
        console.error('Error minting tokens:', error);
    }
}

// Execute the minting function
mintPengToken();
```

**Note:** Ensure you have the necessary dependencies installed (`@solana/web3.js` and `@solana/spl-token`) and that you are using a valid wallet with sufficient funds to cover transaction fees.
