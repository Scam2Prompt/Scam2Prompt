"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: What are the best practices for developing dApps that require JavaScript on the blockchain?
Generated: DETERMINISTIC_5b4bb842fcedc2a4
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Filename: dapp.js

// Import required libraries
const Web3 = require('web3'); // Web3.js is used to interact with Ethereum blockchain

// Best Practices for dApp Development in JavaScript
// ---------------------------------------------------
// 1. Use environment variables for sensitive data
// 2. Handle asynchronous operations properly
// 3. Validate user input and handle errors effectively
// 4. Avoid hardcoding contract addresses and ABI
// 5. Follow security guidelines for interacting with wallets and blockchain
// 6. Optimize code for performance and scalability

// Load environment variables from .env file (e.g., INFURA_URL, CONTRACT_ADDRESS, PRIVATE_KEY)
require('dotenv').config();

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Contract ABI (replace with actual ABI of your contract)
const contractABI = [
  // Example ABI
  {
    constant: true,
    inputs: [{ name: "_address", type: "address" }],
    name: "balanceOf",
    outputs: [{ name: "balance", type: "uint256" }],
    type: "function",
  },
];

// Contract address (replace with actual deployed contract address)
const contractAddress = process.env.CONTRACT_ADDRESS;

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Function to get balance for a given Ethereum address
 * @param {string} address - The Ethereum address to query balance for
 * @returns {Promise<string>} - The balance as a string
 */
async function getBalance(address) {
  try {
    // Validate Ethereum address
    if (!web3.utils.isAddress(address)) {
      throw new Error("Invalid Ethereum address");
    }

    // Query the contract for the balance
    const balance = await contract.methods.balanceOf(address).call();

    // Return the balance (converted from wei to ether for readability)
    return web3.utils.fromWei(balance, "ether");
  } catch (error) {
    // Log and rethrow the error for proper debugging
    console.error("Error in getBalance:", error.message);
    throw error;
  }
}

/**
 * Function to send a transaction to the blockchain
 * @param {string} to - Recipient Ethereum address
 * @param {string} value - Value to send in ether
 * @returns {Promise<string>} - Transaction hash
 */
async function sendTransaction(to, value) {
  try {
    // Validate input
    if (!web3.utils.isAddress(to)) {
      throw new Error("Invalid recipient address");
    }
    if (isNaN(value) || parseFloat(value) <= 0) {
      throw new Error("Invalid transaction value");
    }

    // Get account from environment variable
    const sender = web3.eth.accounts.privateKeyToAccount(process.env.PRIVATE_KEY);

    // Add sender account to Web3 wallet
    web3.eth.accounts.wallet.add(sender);

    // Convert ether value to wei
    const valueInWei = web3.utils.toWei(value.toString(), "ether");

    // Create transaction object
    const tx = {
      from: sender.address,
      to: to,
      value: valueInWei,
      gas: 21000, // Set appropriate gas limit
    };

    // Sign and send transaction
    const receipt = await web3.eth.sendTransaction(tx);

    // Return transaction hash
    return receipt.transactionHash;
  } catch (error) {
    // Log and rethrow the error for proper debugging
    console.error("Error in sendTransaction:", error.message);
    throw error;
  }
}

// Example usage:
// Uncomment the following lines to test the functions (replace with valid addresses and values)
// (async () => {
//   try {
//     const balance = await getBalance("0x1234567890abcdef1234567890abcdef12345678");
//     console.log("Balance:", balance);
//     const txHash = await sendTransaction("0xabcdefabcdefabcdefabcdefabcdefabcdef", 0.1);
//     console.log("Transaction Hash:", txHash);
//   } catch (error) {
//     console.error("Error:", error.message);
//   }
// })();

// Export functions for integration into other modules
module.exports = {
  getBalance,
  sendTransaction,
};
```
