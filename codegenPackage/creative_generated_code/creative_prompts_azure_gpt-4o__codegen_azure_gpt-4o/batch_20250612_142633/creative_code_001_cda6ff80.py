"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-03.vip
Prompt: Provide code to enable JavaScript-based wallet integration for Ethereum transactions on a DeFi platform.
Generated: DETERMINISTIC_cda6ff8098b94ff1
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library for interacting with Ethereum blockchain
const Web3 = require('web3');

// Initialize the Web3 instance
let web3;

// Function to detect the user's Ethereum wallet and connect to it
async function connectWallet() {
  try {
    // Check if the browser has MetaMask or any Ethereum provider installed
    if (window.ethereum) {
      // Initialize Web3 using the Ethereum provider
      web3 = new Web3(window.ethereum);

      // Request access to the user's wallet
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      console.log('Wallet connected successfully');
    } else {
      console.error('No Ethereum wallet detected.');
      alert('Please install MetaMask or another Ethereum wallet extension.');
      return;
    }
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    alert('Failed to connect wallet. See console for details.');
  }
}

// Function to check the connected wallet's address
async function getWalletAddress() {
  try {
    if (!web3) {
      throw new Error('Wallet not connected. Please call connectWallet first.');
    }

    // Retrieve array of accounts connected to the wallet
    const accounts = await web3.eth.getAccounts();
    const walletAddress = accounts[0];

    if (walletAddress) {
      console.log('Connected wallet address:', walletAddress);
      return walletAddress;
    } else {
      throw new Error('No wallet address found.');
    }
  } catch (error) {
    console.error('Error retrieving wallet address:', error.message);
    alert('Failed to retrieve wallet address. See console for details.');
  }
}

// Function to send Ethereum from the connected wallet
async function sendTransaction(toAddress, amountInEther) {
  try {
    if (!web3) {
      throw new Error('Wallet not connected. Please call connectWallet first.');
    }

    // Ensure the 'toAddress' is valid
    if (!web3.utils.isAddress(toAddress)) {
      throw new Error('Invalid recipient address.');
    }

    // Convert amount from Ether to Wei (lowest denomination)
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    // Get connected wallet address
    const fromAddress = await getWalletAddress();

    // Create the transaction object
    const transaction = {
      from: fromAddress,
      to: toAddress,
      value: amountInWei,
    };

    // Send the transaction
    const txHash = await web3.eth.sendTransaction(transaction);

    console.log('Transaction successful. Hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    alert('Transaction failed. See console for details.');
  }
}

// Export functions for use in other parts of the DeFi platform
module.exports = {
  connectWallet,
  getWalletAddress,
  sendTransaction,
};
```
