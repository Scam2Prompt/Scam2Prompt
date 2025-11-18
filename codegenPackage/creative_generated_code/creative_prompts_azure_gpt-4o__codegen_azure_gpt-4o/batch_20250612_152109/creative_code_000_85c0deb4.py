"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-launcher-sol.web.app
Prompt: Write code to create and launch a custom token on the Solana blockchain using JavaScript, referencing tools similar to the Token Launcher app.
Generated: DETERMINISTIC_85c0deb46252dea3
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to create and launch a custom token on the Solana blockchain.
 * This uses the Solana Web3.js library and spl-token package.
 * 
 * Before running the script:
 * - Ensure you have a Solana wallet private key to fund the transaction.
 * - Install dependencies: `npm install @solana/web3.js @solana/spl-token bs58`
 */

const { Connection, Keypair, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { createMint, getOrCreateAssociatedTokenAccount, mintTo } = require('@solana/spl-token');
const bs58 = require('bs58');

// Configuration variables
const NETWORK = 'mainnet-beta'; // Change to 'devnet' for testing
const CONNECTION_URL = clusterApiUrl(NETWORK); // Solana cluster URL
const PRIVATE_KEY = '<YOUR_PRIVATE_KEY>'; // Replace with your wallet's private key (base58-encoded)
const TOKEN_DECIMALS = 9; // Number of decimals for the token
const INITIAL_SUPPLY = 1000000; // Initial token supply

// Error handling wrapper
(async function createCustomToken() {
  try {
    // Step 1: Set up connection to the Solana blockchain
    const connection = new Connection(CONNECTION_URL, 'confirmed');

    // Step 2: Load the wallet keypair from the private key
    const ownerKeypair = Keypair.fromSecretKey(bs58.decode(PRIVATE_KEY));

    // Step 3: Create a new mint (token)
    const mint = await createMint(
      connection,               // Blockchain connection
      ownerKeypair,             // Payer of the transaction
      ownerKeypair.publicKey,   // Authority to mint new tokens
      null,                     // Authority to freeze tokens (optional)
      TOKEN_DECIMALS            // Number of decimals for the token
    );
    console.log(`Token created with Mint Address: ${mint.toBase58()}`);

    // Step 4: Create an associated token account for the owner
    const tokenAccount = await getOrCreateAssociatedTokenAccount(
      connection,
      ownerKeypair,             // Payer of the transaction
      mint,                     // Mint address
      ownerKeypair.publicKey    // Owner of the token account
    );
    console.log(`Associated Token Account Address: ${tokenAccount.address.toBase58()}`);

    // Step 5: Mint initial supply of tokens to the owner's account
    const signature = await mintTo(
      connection,
      ownerKeypair,             // Payer of the transaction
      mint,                     // Mint address
      tokenAccount.address,     // Recipient account
      ownerKeypair,             // Authority to mint tokens
      INITIAL_SUPPLY * 10 ** TOKEN_DECIMALS // Amount of tokens to mint (adjusted for decimals)
    );
    console.log(`Tokens minted successfully. Transaction Signature: ${signature}`);

    console.log('Custom token successfully created and launched!');
  } catch (error) {
    console.error('Error creating custom token:', error.message);
  }
})();
```

> **Note:** Don't forget to replace `<YOUR_PRIVATE_KEY>` with the actual private key of your wallet in base58 format. Use this script responsibly, and always test on the Solana devnet before deploying tokens on the mainnet.
