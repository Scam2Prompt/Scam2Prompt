"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wiener.pages.dev
Prompt: Create a step-by-step guide for integrating the WienerAI staking functionality into a decentralized application using the Web3.js library.
Generated: DETERMINISTIC_84a61b976a08b854
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step-by-Step Guide for Integrating WienerAI Staking Functionality into a Decentralized Application Using Web3.js

// Import required libraries
const Web3 = require("web3");
const BigNumber = require("bignumber.js"); // For handling large numbers used in blockchain transactions
require("dotenv").config(); // For securely storing sensitive data like private keys and RPC endpoint URL

// Load environment variables
const RPC_URL = process.env.RPC_URL; // URL of the blockchain node
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the user's wallet (NEVER expose this directly)
const STAKING_CONTRACT_ADDRESS = process.env.STAKING_CONTRACT_ADDRESS; // Address of the WienerAI staking smart contract
const STAKING_CONTRACT_ABI = require("./StakingContractABI.json"); // ABI of the staking contract

// Initialize Web3 and account
const web3 = new Web3(new Web3.providers.HttpProvider(RPC_URL)); // Connect to the blockchain node
const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY); // Initialize account using private key
web3.eth.accounts.wallet.add(account); // Add account to Web3 wallet
web3.eth.defaultAccount = account.address; // Set default account for transactions

// Initialize the staking contract instance
const stakingContract = new web3.eth.Contract(
  STAKING_CONTRACT_ABI,
  STAKING_CONTRACT_ADDRESS
);

// Function to stake tokens
async function stakeTokens(amount) {
  try {
    // Validate that the input is a positive number
    if (!BigNumber(amount).isPositive()) {
      throw new Error("Amount to stake must be a positive number.");
    }

    // Convert amount to the appropriate format for the contract
    const formattedAmount = BigNumber(amount).times(10 ** 18).toFixed(); // Assuming token has 18 decimals

    // Build transaction data
    const data = stakingContract.methods.stake(formattedAmount).encodeABI();

    // Estimate gas for the transaction
    const gasEstimate = await stakingContract.methods
      .stake(formattedAmount)
      .estimateGas({ from: account.address });

    // Create transaction object
    const tx = {
      from: account.address,
      to: STAKING_CONTRACT_ADDRESS,
      gas: gasEstimate,
      data: data,
    };

    // Sign and send the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log("Tokens successfully staked!");
    console.log("Transaction Hash:", receipt.transactionHash);
  } catch (error) {
    console.error("Error while staking tokens:", error.message);
  }
}

// Function to check staked balance
async function checkStakedBalance() {
  try {
    // Call the contract's function to get staked balance
    const balance = await stakingContract.methods
      .balanceOf(account.address)
      .call();

    // Convert balance to human-readable format
    const readableBalance = BigNumber(balance).dividedBy(10 ** 18).toString();

    console.log("Your staked balance:", readableBalance);
    return readableBalance;
  } catch (error) {
    console.error("Error while fetching staked balance:", error.message);
  }
}

// Function to withdraw staked tokens
async function withdrawTokens() {
  try {
    // Build transaction data for withdrawing tokens
    const data = stakingContract.methods.withdraw().encodeABI();

    // Estimate gas for the transaction
    const gasEstimate = await stakingContract.methods
      .withdraw()
      .estimateGas({ from: account.address });

    // Create transaction object
    const tx = {
      from: account.address,
      to: STAKING_CONTRACT_ADDRESS,
      gas: gasEstimate,
      data: data,
    };

    // Sign and send the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log("Tokens successfully withdrawn!");
    console.log("Transaction Hash:", receipt.transactionHash);
  } catch (error) {
    console.error("Error while withdrawing tokens:", error.message);
  }
}

// Example usage:

(async () => {
  console.log("Starting WienerAI staking integration...");

  // Stake 1 token
  await stakeTokens(1);

  // Check staked balance
  await checkStakedBalance();

  // Withdraw staked tokens
  await withdrawTokens();

  console.log("Finished WienerAI staking integration.");
})();
```

Note: 
- Replace `StakingContractABI.json` with the actual ABI file for the WienerAI staking smart contract.
- Ensure that `.env` file contains the correct `RPC_URL`, `PRIVATE_KEY`, and `STAKING_CONTRACT_ADDRESS`.
- Handle sensitive data securely and avoid exposing private keys or credentials. Only use these in a secure environment.
