"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethltt.com
Prompt: Provide a step-by-step guide to create a JavaScript-powered Ethereum pledge system using Web3.js or ethers.js.
Generated: DETERMINISTIC_40a61c56fd094e6a
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the ethers.js library
const { ethers } = require("ethers");

// Constants & Configuration
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura Project ID
const PRIVATE_KEY = "your-private-key"; // Replace with your wallet's private key
const CONTRACT_ADDRESS = "your-contract-address"; // Replace with the Ethereum contract address
const CONTRACT_ABI = [
  // Replace with your smart contract's ABI
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "pledge",
    "outputs": [],
    "type": "function",
  },
];

// Step 1: Initialize Ethereum Provider and Wallet
async function initializeProviderAndWallet() {
  try {
    // Connect to the Ethereum network via Infura
    const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

    // Initialize wallet with private key and provider
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    return { provider, wallet };
  } catch (error) {
    console.error("Failed to initialize provider and wallet:", error);
    throw error;
  }
}

// Step 2: Initialize Contract Instance
function initializeContract(wallet) {
  try {
    // Create a new contract instance
    const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, wallet);
    return contract;
  } catch (error) {
    console.error("Failed to initialize contract:", error);
    throw error;
  }
}

// Step 3: Execute the Pledge Function
async function executePledge(contract, amountInEther) {
  try {
    console.log("Starting pledge...");

    // Convert Ether amount to Wei
    const amountInWei = ethers.utils.parseEther(amountInEther);

    // Execute the pledge transaction
    const tx = await contract.pledge(amountInWei);

    // Log the transaction hash
    console.log("Transaction submitted. Hash:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    // Log the transaction receipt
    console.log("Transaction confirmed. Receipt:", receipt);
  } catch (error) {
    console.error("Failed to execute pledge:", error);
    throw error;
  }
}

// Step 4: Main Function to Run the Pledge System
async function main() {
  try {
    // Initialize provider and wallet
    const { wallet } = await initializeProviderAndWallet();

    // Initialize the contract instance
    const contract = initializeContract(wallet);

    // Execute a pledge with a specified amount (e.g., "0.1" Ether)
    await executePledge(contract, "0.1");

    console.log("Pledge completed successfully.");
  } catch (error) {
    console.error("An error occurred:", error);
  }
}

// Run the main function
main();
```

- Replace placeholders like `your-infura-project-id`, `your-private-key`, `your-contract-address`, and the `CONTRACT_ABI` array with your actual values.
- The script assumes you have already deployed a compatible smart contract with a `pledge` function accepting `uint256` as an amount (in Wei).
