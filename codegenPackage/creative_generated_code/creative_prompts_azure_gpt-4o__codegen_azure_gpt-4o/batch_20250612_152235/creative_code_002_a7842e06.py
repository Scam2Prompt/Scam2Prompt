"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-czk.pages.dev
Prompt: Generate a JavaScript script to interact with the Solana blockchain, specifically using the methods described on the Solana区块链创建服务工具 webpage for token creation.
Generated: DETERMINISTIC_a7842e06f649a453
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from @solana/web3.js
const {
  Connection,
  PublicKey,
  Keypair,
  clusterApiUrl,
  SystemProgram,
  LAMPORTS_PER_SOL,
  Transaction,
} = require('@solana/web3.js');

// Import SPL token utilities from @solana/spl-token
const {
  createMint,
  getOrCreateAssociatedTokenAccount,
  mintTo,
  transfer,
} = require('@solana/spl-token');

// Define constants
const SOLANA_NETWORK = 'devnet'; // Cluster to connect to (devnet, testnet, or mainnet-beta)
const connection = new Connection(clusterApiUrl(SOLANA_NETWORK));

// Generate a new keypair for the payer (wallet that will pay for transactions)
const payer = Keypair.generate();

// Function to request an airdrop for the payer account (only works on devnet/testnet)
async function requestAirdrop() {
  try {
    const airdropSignature = await connection.requestAirdrop(
      payer.publicKey,
      2 * LAMPORTS_PER_SOL // Request 2 SOL for the payer account
    );
    await connection.confirmTransaction(airdropSignature);
    console.log('Airdrop successful!');
  } catch (error) {
    console.error('Airdrop failed:', error);
  }
}

// Function to create a new token mint
async function createTokenMint() {
  try {
    // Generate a new keypair for the mint authority
    const mintAuthority = payer.publicKey;

    // Generate a freeze authority keypair (optional, can be null)
    const freezeAuthority = null;

    // Create the mint and set decimals to 9 (default for tokens on Solana)
    const tokenMint = await createMint(
      connection, // Connection to Solana network
      payer, // Payer account
      mintAuthority, // Address that can mint tokens
      freezeAuthority, // Address that can freeze token accounts
      9 // Decimal places for the token
    );

    console.log('Token Mint Created:', tokenMint.toBase58());
    return tokenMint;
  } catch (error) {
    console.error('Failed to create token mint:', error);
  }
}

// Function to create an associated token account for a user
async function createTokenAccount(tokenMint, owner) {
  try {
    const tokenAccount = await getOrCreateAssociatedTokenAccount(
      connection, // Connection to Solana network
      payer, // Payer account
      tokenMint, // Token mint address
      owner // Owner of the token account
    );

    console.log('Token Account Created:', tokenAccount.address.toBase58());
    return tokenAccount;
  } catch (error) {
    console.error('Failed to create token account:', error);
  }
}

// Function to mint tokens to a specific account
async function mintTokens(tokenMint, destination, amount) {
  try {
    await mintTo(
      connection, // Connection to Solana network
      payer, // Payer account
      tokenMint, // Token mint address
      destination, // Destination token account
      payer, // Authority that can mint tokens
      amount * Math.pow(10, 9) // Convert amount to smallest unit (e.g., 10 => 10 * 10^9 lamports)
    );

    console.log(`Minted ${amount} tokens to account: ${destination.toBase58()}`);
  } catch (error) {
    console.error('Failed to mint tokens:', error);
  }
}

// Function to transfer tokens between accounts
async function transferTokens(tokenMint, source, destination, owner, amount) {
  try {
    await transfer(
      connection, // Connection to Solana network
      payer, // Payer account
      source, // Source token account
      destination, // Destination token account
      owner, // Owner of the source account
      amount * Math.pow(10, 9) // Convert amount to smallest unit
    );

    console.log(`Transferred ${amount} tokens from ${source.toBase58()} to ${destination.toBase58()}`);
  } catch (error) {
    console.error('Failed to transfer tokens:', error);
  }
}

// Main function to execute the script
(async () => {
  console.log('Starting Solana Token Interaction Script');

  // Step 1: Request Airdrop for Payer Account
  await requestAirdrop();

  // Step 2: Create a new Token Mint
  const tokenMint = await createTokenMint();

  // Step 3: Create a token account for the payer
  const payerTokenAccount = await createTokenAccount(tokenMint, payer.publicKey);

  // Step 4: Mint tokens to the payer's token account
  await mintTokens(tokenMint, payerTokenAccount.address, 100); // Mint 100 tokens

  // Step 5: Transfer tokens to another user (example user receiving tokens)
  const recipient = Keypair.generate(); // Generate a recipient keypair
  const recipientTokenAccount = await createTokenAccount(tokenMint, recipient.publicKey);

  await transferTokens(tokenMint, payerTokenAccount.address, recipientTokenAccount.address, payer, 50); // Transfer 50 tokens

  console.log('Script execution completed!');
})();
```
