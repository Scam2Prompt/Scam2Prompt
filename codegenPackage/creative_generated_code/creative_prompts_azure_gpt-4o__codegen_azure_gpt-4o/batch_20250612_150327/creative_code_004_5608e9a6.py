"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallett.creatorlink.net
Prompt: Create a step-by-step guide in code for importing a MetaMask wallet using a recovery seed phrase, ensuring secure handling of the seed phrase.
Generated: DETERMINISTIC_5608e9a66a18921d
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-step guide to import a MetaMask wallet using a recovery seed phrase.
 * This code demonstrates secure handling of the seed phrase and wallet recovery.
 *
 * Requirements:
 * - Node.js environment
 * - Install `ethers` library: `npm install ethers`
 */

// Import necessary dependencies from ethers.js
const { ethers } = require('ethers');

// Securely store environment variables (including the recovery seed phrase) in a `.env` file.
// Install dotenv for environment variable management: `npm install dotenv`
require('dotenv').config();

try {
  // Step 1: Retrieve the seed phrase securely from environment variables
  const seedPhrase = process.env.SEED_PHRASE;

  // Validate that the seed phrase exists
  if (!seedPhrase) {
    throw new Error('Seed phrase not found! Please set SEED_PHRASE in your .env file.');
  }

  // Step 2: Create a wallet instance using the recovery seed phrase
  const wallet = ethers.Wallet.fromMnemonic(seedPhrase);

  // Step 3: Log essential wallet details securely
  console.log('Wallet successfully imported!');
  console.log('Address:', wallet.address);

  /**
   * Best practice: Do NOT log the private key or seed phrase in production environments.
   * If you must display sensitive information during development, ensure it is removed prior to deployment.
   */

  // Step 4: Demonstrate secure handling of the wallet
  // Example: Connect wallet to a provider (e.g., Infura or Alchemy)
  const provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_RPC_URL); // Replace with your RPC URL
  const connectedWallet = wallet.connect(provider);

  // Verify connection and balance retrieval
  connectedWallet.getBalance()
    .then(balance => {
      console.log('Wallet Balance:', ethers.utils.formatEther(balance), 'ETH');
    })
    .catch(error => {
      console.error('Failed to retrieve wallet balance:', error.message);
    });

} catch (error) {
  // Step 5: Handle errors gracefully
  console.error('Error importing wallet:', error.message);
}

/**
 * NOTE:
 * - Store the seed phrase securely (e.g., use environment variables or encrypted storage).
 * - Never hardcode sensitive information like seed phrases or private keys in your code.
 * - Use secure deployment practices to protect your secrets.
 */
```
