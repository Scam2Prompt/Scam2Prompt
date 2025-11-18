"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-launcher-sol.web.app
Prompt: Generate JavaScript code to enable token creation and deployment on Solana, ensuring compatibility with tools like Token Launcher.
Generated: DETERMINISTIC_a7181c448d92de36
Batch ID: 20250612_152109
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
  LAMPORTS_PER_SOL,
  Transaction,
  SystemProgram,
} = require('@solana/web3.js');
const {
  createMint,
  getOrCreateAssociatedTokenAccount,
  mintTo,
  transfer,
} = require('@solana/spl-token');

// Constants for configuration
const NETWORK = 'mainnet-beta'; // Change to 'devnet' or 'testnet' for testing
const DECIMALS = 9; // Number of decimals for the token
const INITIAL_SUPPLY = 1000000; // Initial supply of tokens
const TOKEN_NAME = 'MyToken'; // Replace with your token name

async function createAndDeployToken() {
  try {
    // Step 1: Establish a connection with Solana blockchain
    const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

    // Step 2: Generate a new Keypair for the token owner
    const payer = Keypair.generate();

    // Airdrop SOL to the token owner's account (needed for fees, only in testnet/devnet)
    const airdropSignature = await connection.requestAirdrop(
      payer.publicKey,
      LAMPORTS_PER_SOL // 1 SOL
    );
    await connection.confirmTransaction(airdropSignature);

    console.log(`Airdropped 1 SOL to token owner's account: ${payer.publicKey.toBase58()}`);

    // Step 3: Create a new Mint (Token)
    const mint = await createMint(
      connection, // Connection object
      payer, // Payer for transaction fees
      payer.publicKey, // Mint authority (can mint new tokens)
      payer.publicKey, // Freeze authority (optional, can freeze accounts)
      DECIMALS // Number of decimals
    );

    console.log(`Token Minted. Mint Address: ${mint.toBase58()}`);

    // Step 4: Create an associated token account for the payer
    const tokenAccount = await getOrCreateAssociatedTokenAccount(
      connection,
      payer,
      mint,
      payer.publicKey // Account holder's public key
    );

    console.log(`Associated Token Account created: ${tokenAccount.address.toBase58()}`);

    // Step 5: Mint tokens to the associated token account
    await mintTo(
      connection,
      payer,
      mint,
      tokenAccount.address,
      payer.publicKey, // Mint authority
      INITIAL_SUPPLY * Math.pow(10, DECIMALS) // Amount to mint, scaled to decimals
    );

    console.log(`${INITIAL_SUPPLY} tokens minted to ${tokenAccount.address.toBase58()}`);
  } catch (error) {
    console.error('Error creating and deploying token:', error);
  }
}

// Execute the function
createAndDeployToken();
```
