"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Generate code in JavaScript to automate the process of connecting a wallet (e.g., MetaMask) and purchasing $BTFD tokens using ETH or BNB during the presale.
Generated: DETERMINISTIC_75caf6165fba78e2
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define the presale contract address and ABI
const PRESALE_CONTRACT_ADDRESS = 'YOUR_PRESALE_CONTRACT_ADDRESS';
const PRESALE_ABI = [
  // Add the ABI for the presale contract here
];

// Initialize the Web3 provider
const web3 = new Web3(window.ethereum);

// Connect to MetaMask
async function connectWallet() {
  if (typeof window.ethereum !== 'undefined') {
    try {
      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      console.log('Wallet connected:', window.ethereum.selectedAddress);
      return window.ethereum.selectedAddress;
    } catch (error) {
      console.error('User denied wallet connection:', error);
      throw new Error('Connection failed');
    }
  } else {
    console.error('MetaMask is not installed');
    throw new Error('MetaMask is not installed');
  }
}

// Purchase $BTFD tokens
async function purchaseTokens(amountInEther) {
  try {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Create a contract instance
    const presaleContract = new web3.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);
    
    // Convert amount to Wei
    const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

    // Call the purchase function on the presale contract
    const transaction = await presaleContract.methods.purchase().send({
      from: account,
      value: amountInWei,
      gas: 3000000 // Set an appropriate gas limit
    });

    console.log('Transaction successful:', transaction);
  } catch (error) {
    console.error('Error during token purchase:', error);
    throw new Error('Token purchase failed');
  }
}

// Main function to handle wallet connection and token purchase
async function main() {
  try {
    await connectWallet();
    const amountToPurchase = 0.1; // Amount of ETH/BNB to spend on $BTFD tokens
    await purchaseTokens(amountToPurchase);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Execute the main function
main();
```
