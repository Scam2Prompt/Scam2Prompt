"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.sbs
Prompt: Provide a step-by-step guide to enable JavaScript functionality for interacting with USDC smart contracts on Ethereum.
Generated: DETERMINISTIC_4dc8ed2f93b8e83e
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Import required libraries
// Importing ethers.js - a popular library for interacting with Ethereum blockchain
const { ethers } = require("ethers");

// Step 2: Define the USDC Contract ABI (Application Binary Interface)
/*
  The ABI is required to interact with the USDC smart contract.
  Below is a simplified ABI with common ERC20 functions.
*/
const USDC_ABI = [
  // Query Balance
  "function balanceOf(address owner) view returns (uint256)",
  // Transfer Tokens
  "function transfer(address to, uint256 amount) returns (bool)",
];

// Step 3: Define Ethereum network and USDC contract address
/*
  Use the correct USDC contract address for the Ethereum network.
  For example, the mainnet USDC contract address is used below.
*/
const ETHEREUM_NETWORK = "mainnet"; // Choose between 'mainnet', 'goerli', etc.
const USDC_CONTRACT_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606EB48"; // Mainnet USDC contract address

// Step 4: Connect to Ethereum using ethers.js
async function setupProviderAndContract() {
  try {
    // Create a provider (for interacting with the blockchain)
    const provider = ethers.getDefaultProvider(ETHEREUM_NETWORK);

    // Create a signer (used for signing transactions)
    // This example assumes you have a private key (NEVER SHARE YOUR PRIVATE KEY)
    const privateKey = "YOUR_PRIVATE_KEY"; // Replace with the actual private key
    const signer = new ethers.Wallet(privateKey, provider);

    // Initialize the USDC contract instance
    const usdcContract = new ethers.Contract(USDC_CONTRACT_ADDRESS, USDC_ABI, signer);

    return { provider, signer, usdcContract };
  } catch (error) {
    console.error("Error setting up provider or contract:", error);
    throw new Error("Failed to initialize provider or contract.");
  }
}

// Step 5: Function to check USDC balance
async function checkBalance(address) {
  try {
    // Ensure setup is correctly initialized
    const { usdcContract } = await setupProviderAndContract();

    // Query the balance of the given address
    const balance = await usdcContract.balanceOf(address);

    // Convert the balance from Wei to a human-readable format
    return ethers.utils.formatUnits(balance, 6); // USDC has 6 decimal places
  } catch (error) {
    console.error("Error querying balance:", error);
    throw new Error("Failed to query balance.");
  }
}

// Step 6: Function to transfer USDC tokens
async function transferUSDC(to, amount) {
  try {
    const { usdcContract } = await setupProviderAndContract();

    // Convert the amount to Wei (smallest unit of USDC)
    const amountInWei = ethers.utils.parseUnits(amount.toString(), 6);

    // Execute the transfer operation
    const tx = await usdcContract.transfer(to, amountInWei);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log("Transaction successful! Receipt:", receipt);
  } catch (error) {
    console.error("Error transferring USDC:", error);
    throw new Error("Failed to transfer USDC.");
  }
}

// Step 7: Example usage
(async function main() {
  try {
    const testAddress = "0xYourEthereumAddressHere"; // Replace with a valid Ethereum address
    const recipientAddress = "0xRecipientAddressHere"; // Replace with recipient Ethereum address

    // Check balance
    const balance = await checkBalance(testAddress);
    console.log(`USDC Balance for ${testAddress}: ${balance}`);

    // Transfer USDC
    const transferAmount = 10; // Transfer 10 USDC
    await transferUSDC(recipientAddress, transferAmount);
  } catch (error) {
    console.error("Error in main function:", error);
  }
})();
```
