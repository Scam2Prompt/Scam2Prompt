"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-tx.pages.dev
Prompt: Provide a code example for implementing buy/sell functionality in a DApp connected to mobile wallets.
Generated: DETERMINISTIC_40997eb2231c43d2
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3'); // Web3.js for interacting with Ethereum blockchain
const ABI = require('./contractABI.json'); // Replace with your smart contract's ABI file
const CONTRACT_ADDRESS = "0xYourContractAddress"; // Replace with your deployed contract address

// Initialize Web3 instance
let web3;
if (window.ethereum) {
  web3 = new Web3(window.ethereum); // Uses MetaMask or other injected wallet
} else {
  throw new Error("Ethereum-compatible browser or wallet not detected.");
}

// Contract instance
const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

// Function to connect to wallet
async function connectWallet() {
  try {
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    return accounts[0]; // Return the connected wallet address
  } catch (error) {
    throw new Error("Failed to connect wallet: " + error.message);
  }
}

// Function to buy tokens
async function buyTokens(amountInEther) {
  try {
    const buyerAddress = await connectWallet(); // Connect and get user's wallet
    const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether'); // Convert Ether to Wei

    // Send transaction to buy tokens
    const transaction = await contract.methods.buyTokens().send({
      from: buyerAddress,
      value: amountInWei, // Amount of Ether to send
    });

    console.log("Transaction successful:", transaction);
    return transaction; // Returns transaction receipt
  } catch (error) {
    console.error("Error buying tokens:", error.message);
    throw new Error("Failed to buy tokens: " + error.message);
  }
}

// Function to sell tokens
async function sellTokens(tokenAmount) {
  try {
    const sellerAddress = await connectWallet(); // Connect and get user's wallet

    // Send transaction to sell tokens
    const transaction = await contract.methods.sellTokens(tokenAmount).send({
      from: sellerAddress,
    });

    console.log("Transaction successful:", transaction);
    return transaction; // Returns transaction receipt
  } catch (error) {
    console.error("Error selling tokens:", error.message);
    throw new Error("Failed to sell tokens: " + error.message);
  }
}

// Example Usage
// Initiate buying tokens (2 Ether)
// buyTokens(2).catch(console.error);

// Initiate selling tokens (100 Tokens)
// sellTokens(100).catch(console.error);

// Note:
// - Ensure "buyTokens" and "sellTokens" methods exist in your smart contract.
// - Replace "contractABI.json" and "0xYourContractAddress" with your actual ABI and contract address.
// - Include additional validations and checks as needed to improve security.
```
