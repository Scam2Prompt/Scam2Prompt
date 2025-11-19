"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: What are the steps to integrate wallet connection functionality for an NFT marketplace that has a price per NFT of X.XX ETH?
Generated: DETERMINISTIC_4a4c203a690ae658
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's production-ready code for integrating wallet connection functionality in an NFT marketplace using JavaScript and the web3.js library:

```javascript
/*
 * NFT Marketplace Wallet Connection
 * This script integrates wallet connection functionality for an NFT marketplace.
 * It assumes the price per NFT is defined as a constant `NFT_PRICE_ETH`.
 */

// Import web3.js (ensure web3.js is installed via npm or included in your project)
const Web3 = require('web3');

// Constants
const NFT_PRICE_ETH = 0.1; // Set the price per NFT in ETH
const CONTRACT_ADDRESS = '0xYourSmartContractAddressHere'; // Replace with your NFT smart contract address
const ABI = []; // Replace with your smart contract ABI

// Initialize web3 instance
let web3;
let userAccount;

// DOM Elements (ensure these elements exist in your HTML)
const connectButton = document.getElementById('connectWallet');
const buyButton = document.getElementById('buyNFT');

// Initialize application
async function init() {
  if (typeof window.ethereum !== 'undefined') {
    // Create a web3 instance using MetaMask provider
    web3 = new Web3(window.ethereum);

    // Listen for account changes
    window.ethereum.on('accountsChanged', handleAccountChange);

    connectButton.addEventListener('click', connectWallet);
    buyButton.addEventListener('click', buyNFT);
  } else {
    alert('MetaMask is not installed. Please install MetaMask to interact with this marketplace.');
  }
}

// Connect wallet function
async function connectWallet() {
  try {
    // Request wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    
    if (accounts.length === 0) {
      throw new Error('No account found. Please connect your wallet.');
    }

    userAccount = accounts[0];
    connectButton.innerText = `Wallet Connected: ${userAccount}`;
    connectButton.disabled = true;
    console.log('Wallet connected:', userAccount);
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    alert(`Error connecting wallet: ${error.message}`);
  }
}

// Handle account change
function handleAccountChange(accounts) {
  if (accounts.length === 0) {
    alert('Wallet disconnected. Please reconnect your wallet.');
    userAccount = null;
    connectButton.innerText = 'Connect Wallet';
    connectButton.disabled = false;
  } else {
    userAccount = accounts[0];
    connectButton.innerText = `Wallet Connected: ${userAccount}`;
    console.log('Account changed:', userAccount);
  }
}

// Buy NFT function
async function buyNFT() {
  if (!userAccount) {
    alert('Please connect your wallet first.');
    return;
  }

  try {
    const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

    // Calculate price in Wei (ETH to Wei conversion)
    const priceInWei = web3.utils.toWei(NFT_PRICE_ETH.toString(), 'ether');

    // Send transaction
    const transactionParameters = {
      from: userAccount,
      to: CONTRACT_ADDRESS,
      value: priceInWei, // Sending ETH for NFT purchase
      data: contract.methods.purchaseNFT().encodeABI(), // Replace with the actual purchase method
    };

    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction successful, hash:', txHash);
    alert('NFT purchase successful!');
  } catch (error) {
    console.error('Error purchasing NFT:', error.message);
    alert(`Error purchasing NFT: ${error.message}`);
  }
}

// Initialize application on page load
window.addEventListener('load', init);
```

**Note:**
- Replace `ABI` and `CONTRACT_ADDRESS` with your actual smart contract details.
- Ensure you have the `purchaseNFT` method in your smart contract to handle NFT purchases.
- This code assumes MetaMask is used for wallet connection. If you're using other wallet providers, additional integrations may be required.
