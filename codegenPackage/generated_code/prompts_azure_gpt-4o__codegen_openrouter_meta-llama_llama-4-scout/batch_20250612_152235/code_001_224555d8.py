"""
Generated Code Metadata:
========================
Original URL: https://sol-czk.pages.dev
Prompt: Recommend libraries or APIs mentioned on the Solana区块链创建服务工具 site for interacting with Solana blockchain and creating custom tokens.
Generated: DETERMINISTIC_224555d8e5f79e0e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Keypair, Connection, clusterApiUrl } = require('@solana/web3.js');
const { createMint, createTokenAccount, mintTo } = require('@solana/spl-token');

// Set up Solana connection and API URL
const connection = new Connection(clusterApiUrl('devnet'));

/**
 * Create a new Solana keypair for the token owner
 * @returns {Keypair} The generated keypair
 */
function createKeypair() {
  try {
    // Generate a new keypair
    const keypair = Keypair.generate();
    return keypair;
  } catch (error) {
    console.error('Error creating keypair:', error);
    throw error;
  }
}

/**
 * Create a custom token on the Solana blockchain
 * @param {Keypair} ownerKeypair The keypair of the token owner
 * @param {string} tokenName The name of the token
 * @param {string} tokenSymbol The symbol of the token
 * @param {number} tokenDecimals The number of decimals for the token
 * @returns {Promise<string>} The address of the created token
 */
async function createToken(ownerKeypair, tokenName, tokenSymbol, tokenDecimals) {
  try {
    // Create a new token mint
    const mint = await createMint(
      connection,
      ownerKeypair,
      ownerKeypair.publicKey,
      null,
      tokenDecimals
    );

    // Create a token account for the owner
    const tokenAccount = await createTokenAccount(
      connection,
      ownerKeypair,
      mint,
      ownerKeypair.publicKey
    );

    // Mint some tokens to the owner's account
    await mintTo(
      connection,
      ownerKeypair,
      mint,
      tokenAccount,
      ownerKeypair.publicKey,
      1000000 // Initial token supply
    );

    return mint.toString();
  } catch (error) {
    console.error('Error creating token:', error);
    throw error;
  }
}

// Example usage
async function main() {
  const ownerKeypair = createKeypair();
  const tokenName = 'My Token';
  const tokenSymbol = 'MTK';
  const tokenDecimals = 2;

  const tokenAddress = await createToken(
    ownerKeypair,
    tokenName,
    tokenSymbol,
    tokenDecimals
  );

  console.log(`Token created at address: ${tokenAddress}`);
}

main();
```
