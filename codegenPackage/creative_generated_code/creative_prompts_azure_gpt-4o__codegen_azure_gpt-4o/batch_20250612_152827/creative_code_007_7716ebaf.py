"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.pages.dev
Prompt: Develop a web3.js script to automate claiming NFTs and referral bonuses from the God Candle platform.
Generated: DETERMINISTIC_7716ebaf65ad1078
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const Web3 = require('web3');
require('dotenv').config();

// Load environment variables for security
const INFURA_URL = process.env.INFURA_URL; // Infura endpoint for Ethereum node
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key
const GOD_CANDLE_CONTRACT_ADDRESS = process.env.GOD_CANDLE_CONTRACT_ADDRESS; // God Candle platform contract address
const GOD_CANDLE_ABI = require('./GodCandleABI.json'); // ABI file for the God Candle contract

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Create account instance from the private key
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.eth.defaultAccount = account.address;

// Create contract instance
const godCandleContract = new web3.eth.Contract(GOD_CANDLE_ABI, GOD_CANDLE_CONTRACT_ADDRESS);

/**
 * Automates claiming NFTs from the God Candle platform.
 * @returns {Promise<string>} Transaction hash of the NFT claim.
 */
async function claimNFT() {
  try {
    console.log('Attempting to claim NFT...');

    // Prepare the transaction data
    const tx = godCandleContract.methods.claimNFT();
    const gas = await tx.estimateGas({ from: account.address });

    // Send the transaction
    const receipt = await tx.send({
      from: account.address,
      gas,
    });

    console.log('NFT claimed successfully!', receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error('Failed to claim NFT:', error.message);
    throw error; // Rethrow error for external handling
  }
}

/**
 * Automates claiming referral bonuses from the God Candle platform.
 * @returns {Promise<string>} Transaction hash of the referral bonus claim.
 */
async function claimReferralBonus() {
  try {
    console.log('Attempting to claim referral bonus...');

    // Prepare the transaction data
    const tx = godCandleContract.methods.claimReferralBonus();
    const gas = await tx.estimateGas({ from: account.address });

    // Send the transaction
    const receipt = await tx.send({
      from: account.address,
      gas,
    });

    console.log('Referral bonus claimed successfully!', receipt.transactionHash);
    return receipt.transactionHash;
  } catch (error) {
    console.error('Failed to claim referral bonus:', error.message);
    throw error; // Rethrow error for external handling
  }
}

/**
 * Main function to execute the script.
 */
async function main() {
  try {
    console.log('Starting automation script...');

    // Claim NFT
    await claimNFT();

    // Claim referral bonus
    await claimReferralBonus();

    console.log('Automation script completed successfully!');
  } catch (error) {
    console.error('Error occurred during automation:', error.message);
    process.exit(1); // Exit script with error code
  }
}

// Execute the script
main();
```

### Instructions:
1. Save the God Candle contract ABI in a separate file named `GodCandleABI.json`.
2. Populate `.env` file with the following variables:  
   - `INFURA_URL`: Your Infura endpoint URL  
   - `PRIVATE_KEY`: Your wallet's private key  
   - `GOD_CANDLE_CONTRACT_ADDRESS`: The address of the God Candle contract  
3. Install necessary dependencies using `npm install web3 dotenv`.
4. Run the script using `node script.js`.
