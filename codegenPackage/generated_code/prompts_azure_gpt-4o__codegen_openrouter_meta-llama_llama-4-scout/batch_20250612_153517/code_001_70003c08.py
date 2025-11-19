"""
Generated Code Metadata:
========================
Original URL: https://solinu-org.pages.dev
Prompt: Generate code to check the balance of $SOLINU tokens in a connected wallet and calculate the reward distribution based on the airdrop rules provided (e.g., $300 or 10% of the balance).
Generated: DETERMINISTIC_70003c0819a4391a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const axios = require('axios');

/**
 * Airdrop reward distribution rules
 * @typedef {Object} AirdropRules
 * @property {number} fixedReward - Fixed reward amount in USD (e.g., $300)
 * @property {number} percentageReward - Percentage of the balance to reward (e.g., 10%)
 */

/**
 * Connected wallet and token balance
 * @typedef {Object} WalletBalance
 * @property {PublicKey} wallet - Connected wallet public key
 * @property {number} balance - $SOLINU token balance
 */

/**
 * Calculates reward distribution based on airdrop rules
 * @param {WalletBalance} walletBalance - Connected wallet and token balance
 * @param {AirdropRules} airdropRules - Airdrop reward distribution rules
 * @returns {number} Reward amount in $SOLINU tokens
 */
function calculateReward(walletBalance, airdropRules) {
  // Calculate reward amount in USD
  const fixedRewardUsd = airdropRules.fixedReward;
  const percentageRewardUsd = walletBalance.balance * airdropRules.percentageReward / 100;

  // Choose maximum reward amount
  const rewardUsd = Math.min(fixedRewardUsd, percentageRewardUsd);

  // Assume $SOLINU token price is $1 (replace with actual token price)
  const solinuTokenPrice = 1;
  const rewardSolinu = rewardUsd / solinuTokenPrice;

  return rewardSolinu;
}

// Airdrop rules example
const airdropRules = {
  fixedReward: 300, // $300
  percentageReward: 10, // 10% of balance
};

// Solana cluster connection
const connection = new Connection(clusterApiUrl('devnet'));

// Connected wallet public key
const connectedWallet = new PublicKey('your_connected_wallet_public_key');

// $SOLINU token public key
const solinuTokenPublicKey = new PublicKey('your_solinu_token_public_key');

// Fetch $SOLINU token balance
async function getTokenBalance(wallet) {
  try {
    const balance = await connection.getTokenAccountBalance(
      new PublicKey('your_solinu_token_account_public_key')
    );
    return parseInt(balance.uiAmount);
  } catch (error) {
    console.error('Error fetching token balance:', error);
    throw error;
  }
}

// Main function
async function main() {
  try {
    // Fetch $SOLINU token balance
    const balance = await getTokenBalance(connectedWallet);

    // Create wallet balance object
    const walletBalance = {
      wallet: connectedWallet,
      balance,
    };

    // Calculate reward distribution
    const rewardSolinu = calculateReward(walletBalance, airdropRules);

    console.log(`$SOLINU token balance: ${balance}`);
    console.log(`Reward distribution: ${rewardSolinu} $SOLINU tokens`);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Run main function
main();
```
