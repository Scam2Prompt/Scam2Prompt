"""
Generated Code Metadata:
========================
Original URL: https://fetch-alliance.com
Prompt: "Create a guide on getting started with Fetch Wallet for transactions on the Fetch.ai platform, including code examples for simple transactions."
Generated: DETERMINISTIC_6df9aed2d00210ca
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const fetch = require('node-fetch');
const { FetchWallet, DirectSecp256k1HdWallet } = require('@fetchai/wallet');

// Set up constants for the Fetch.ai network
const NETWORK = 'testnet'; // or 'mainnet'
const LEDGER = 'fetchai';
const COINS = [
  {
    denom: 'fet',
    decimals: 6,
  },
];

/**
 * Create a new Fetch Wallet instance
 * @param {string} mnemonic - The wallet mnemonic
 * @param {string} password - The wallet password
 * @returns {Promise<FetchWallet>}
 */
async function createWallet(mnemonic, password) {
  try {
    // Create a new DirectSecp256k1HdWallet instance
    const wallet = await DirectSecp256k1HdWallet.fromMnemonic(
      mnemonic,
      password,
      COINS,
      LEDGER,
      NETWORK,
    );

    // Return the Fetch Wallet instance
    return new FetchWallet(wallet);
  } catch (error) {
    console.error('Error creating wallet:', error);
    throw error;
  }
}

/**
 * Send a simple transaction using the Fetch Wallet
 * @param {FetchWallet} wallet - The Fetch Wallet instance
 * @param {string} recipientAddress - The recipient's address
 * @param {number} amount - The amount to send (in FET)
 * @returns {Promise<string>} The transaction hash
 */
async function sendTransaction(wallet, recipientAddress, amount) {
  try {
    // Get the wallet's account address
    const accountAddress = wallet.accountAddress;

    // Create a new transaction
    const transaction = {
      from: accountAddress,
      to: recipientAddress,
      value: `${amount * 1e6}`, // Convert FET to microFET (6 decimal places)
      memo: 'Simple transaction',
    };

    // Sign and broadcast the transaction
    const transactionHash = await wallet.sendTransaction(transaction);

    // Return the transaction hash
    return transactionHash;
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw error;
  }
}

// Example usage
async function main() {
  // Replace with your own mnemonic and password
  const mnemonic = 'your_mnemonic_here';
  const password = 'your_password_here';

  // Create a new Fetch Wallet instance
  const wallet = await createWallet(mnemonic, password);

  // Get the wallet's account address
  const accountAddress = wallet.accountAddress;
  console.log(`Account Address: ${accountAddress}`);

  // Replace with the recipient's address
  const recipientAddress = 'fetch1...';

  // Send a simple transaction
  const amount = 1; // 1 FET
  const transactionHash = await sendTransaction(wallet, recipientAddress, amount);
  console.log(`Transaction Hash: ${transactionHash}`);
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```
