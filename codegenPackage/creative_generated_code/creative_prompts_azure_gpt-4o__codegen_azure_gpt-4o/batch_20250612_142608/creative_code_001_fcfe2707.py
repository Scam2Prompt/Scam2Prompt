"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Generate code to interact with the MetaMask wallet API for importing wallet tokens and executing secure transactions, as outlined in the "MetaMask导入钱包代币全面指南" section.
Generated: DETERMINISTIC_fcfe27071e81c87a
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Function to connect to MetaMask and import wallet tokens
async function importWalletTokensAndExecuteTransaction() {
  try {
    // Check if MetaMask is available
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask first.");
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const account = accounts[0]; // Get the first connected account

    console.log(`Connected account: ${account}`);

    // Create a provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Create a signer to authorize transactions
    const signer = provider.getSigner();

    // Example token contract data (replace these values with your token's information)
    const tokenAddress = "0xYourTokenAddressHere"; // Replace with your token's smart contract address
    const tokenABI = [
      // Minimal ERC20 ABI
      "function balanceOf(address owner) view returns (uint256)",
      "function transfer(address to, uint256 amount) returns (bool)"
    ];

    // Connect to the token contract
    const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);

    // Import wallet tokens (fetch balance from contract)
    const balance = await tokenContract.balanceOf(account);

    console.log(`Token balance: ${ethers.utils.formatUnits(balance, 18)} tokens`);

    // Example transaction: Transfer tokens (replace with recipient details)
    const recipientAddress = "0xRecipientAddressHere"; // Replace with recipient's wallet address
    const transferAmount = ethers.utils.parseUnits("10", 18); // Replace with desired amount (e.g., 10 tokens)

    console.log(`Preparing to transfer ${ethers.utils.formatUnits(transferAmount, 18)} tokens to ${recipientAddress}...`);

    // Execute the token transfer securely
    const tx = await tokenContract.transfer(recipientAddress, transferAmount);

    console.log("Transaction sent! Waiting for confirmation...");

    // Wait for confirmation
    const receipt = await tx.wait();

    console.log("Transaction confirmed!", receipt);
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred:", error.message || error);
  }
}

// Execute the function when needed (ensure the user has MetaMask installed and connected)
importWalletTokensAndExecuteTransaction();
```

This code snippet handles connecting to MetaMask, importing wallet tokens, and executing secure transactions with proper ERC20 contract interaction. Make sure to replace placeholder values (like token address and recipient address) with actual data specific to your use case.
