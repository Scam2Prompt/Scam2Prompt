"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiedqwx6srzg433ebdrurpgaguzcwborjnz2lsbvn24piyvd3gjysm.ipfs.dweb.link
Prompt: Generate code to integrate ZeroLend's borrowing/lending functionality into a DeFi dashboard, focusing on zkSync compatibility.
Generated: DETERMINISTIC_c613e578666dd193
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers'); // Ethereum library for interacting with smart contracts
const { ZksyncProvider, Wallet } = require('zksync-web3'); // zkSync compatibility library

// Constants for ZeroLend integration
const ZERO_LEND_CONTRACT_ADDRESS = "0xYourZeroLendContractAddress";
const ZERO_LEND_ABI = [
  // Replace with the actual ABI of the ZeroLend contract
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "borrow",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "lend",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Environment variables
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the user's wallet
const RPC_URL = process.env.ZKSYNC_RPC_URL; // zkSync-compatible RPC URL

// Initialize zkSync provider and wallet
const provider = new ZksyncProvider(RPC_URL);
const wallet = new Wallet(PRIVATE_KEY, provider);

// ZeroLend contract instance
const zeroLendContract = new ethers.Contract(
  ZERO_LEND_CONTRACT_ADDRESS,
  ZERO_LEND_ABI,
  wallet
);

// Function to lend assets
async function lend(amount) {
  try {
    // Validate input
    if (!amount || amount <= 0) {
      throw new Error("Invalid amount. Must be greater than zero.");
    }

    console.log(`Lending ${amount} units to ZeroLend...`);
    const tx = await zeroLendContract.lend(ethers.utils.parseEther(amount.toString()));
    console.log("Transaction submitted. Waiting for confirmation...");
    await tx.wait();
    console.log("Lending transaction confirmed:", tx.hash);
  } catch (error) {
    console.error("Error during lending:", error.message);
  }
}

// Function to borrow assets
async function borrow(amount) {
  try {
    // Validate input
    if (!amount || amount <= 0) {
      throw new Error("Invalid amount. Must be greater than zero.");
    }

    console.log(`Borrowing ${amount} units from ZeroLend...`);
    const tx = await zeroLendContract.borrow(ethers.utils.parseEther(amount.toString()));
    console.log("Transaction submitted. Waiting for confirmation...");
    await tx.wait();
    console.log("Borrowing transaction confirmed:", tx.hash);
  } catch (error) {
    console.error("Error during borrowing:", error.message);
  }
}

// Example Usage
(async () => {
  try {
    // Replace with real values
    const lendAmount = 1.5; // Example: lending 1.5 units
    const borrowAmount = 1.0; // Example: borrowing 1.0 units

    console.log("Starting ZeroLend integration...");

    // Lend assets
    await lend(lendAmount);

    // Borrow assets
    await borrow(borrowAmount);

    console.log("ZeroLend integration completed successfully.");
  } catch (error) {
    console.error("Fatal error in ZeroLend integration:", error.message);
  }
})();
```
