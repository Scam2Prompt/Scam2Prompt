"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ffghhoj.pages.dev
Prompt: Write code to create a Solana token using tools specifically designed for the Solana blockchain.
Generated: DETERMINISTIC_9759ce0379e6f6ae
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies: @solana/web3.js and @solana/spl-token
// Install the dependencies using npm or yarn:
// npm install @solana/web3.js @solana/spl-token

const { Connection, Keypair, clusterApiUrl, LAMPORTS_PER_SOL } = require('@solana/web3.js');
const { createMint, getOrCreateAssociatedTokenAccount, mintTo } = require('@solana/spl-token');

(async () => {
  try {
    // Step 1: Establish a connection to the Solana cluster
    const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

    // Step 2: Generate a new Keypair, which will act as the payer
    const payer = Keypair.generate();

    // Step 3: Airdrop SOL to the payer to fund the transactions
    console.log('Requesting airdrop...');
    const airdropSignature = await connection.requestAirdrop(payer.publicKey, LAMPORTS_PER_SOL);
    await connection.confirmTransaction(airdropSignature);
    console.log('Airdrop completed');

    // Step 4: Create a new token mint
    // Authority to mint new tokens (set to the payer's public key for simplicity)
    const mintAuthority = payer.publicKey;

    // Freeze authority (set null to disable freezing for simplicity)
    const freezeAuthority = null;

    // Create the token mint
    const tokenMint = await createMint(
      connection,        // Connection to Solana cluster
      payer,             // Payer for transaction fees
      mintAuthority,     // Authority allowed to mint tokens
      freezeAuthority,   // Authority allowed to freeze token accounts
      9                  // Decimals for the token (e.g., 9 for a token like SOL)
    );

    console.log(`Token Mint Address: ${tokenMint.toBase58()}`);

    // Step 5: Create an associated token account for the payer to hold the created tokens
    const payerTokenAccount = await getOrCreateAssociatedTokenAccount(
      connection,        // Connection to Solana cluster
      payer,             // Payer for transaction fees
      tokenMint,         // Address of the mint
      payer.publicKey    // Owner of the token account
    );

    console.log(`Payer's Token Account Address: ${payerTokenAccount.address.toBase58()}`);

    // Step 6: Mint tokens to the payer's token account
    const amountToMint = 1000 * Math.pow(10, 9); // Example: Minting 1000 tokens (including decimals)
    await mintTo(
      connection,               // Connection to Solana cluster
      payer,                    // Payer for transaction fees
      tokenMint,                // Address of token mint
      payerTokenAccount.address,// Recipient token account
      mintAuthority,            // Authority allowed to mint tokens
      amountToMint              // Amount of tokens to mint
    );

    console.log(`Minted ${amountToMint / Math.pow(10, 9)} tokens to Payer's Token Account`);
  } catch (err) {
    console.error('An error occurred:', err);
  }
})();
```

**Instructions for use:**
1. Install dependencies using `npm install @solana/web3.js @solana/spl-token`.
2. Save the code to a file (for example, `createToken.js`).
3. Run the script using Node.js: `node createToken.js`.
