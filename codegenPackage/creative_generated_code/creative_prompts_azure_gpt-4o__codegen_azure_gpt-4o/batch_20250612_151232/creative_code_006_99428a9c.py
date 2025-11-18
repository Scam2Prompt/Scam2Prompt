"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullx-authlogin.pages.dev
Prompt: Create a step-by-step guide for integrating wallet connection using MetaMask on a trading platform, inspired by BullX's features.
Generated: DETERMINISTIC_99428a9caaa8fbf4
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-Step Guide for Integrating MetaMask Wallet Connection
 * This code demonstrates how to connect a MetaMask wallet to a trading platform.
 * It uses the Web3.js library to interact with Ethereum blockchain.
 */

// Import necessary dependencies
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Check if MetaMask is installed
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Connect MetaMask wallet
async function connectMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!isMetaMaskInstalled()) {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Prompt user to connect their wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Initialize Web3 instance with MetaMask provider
    web3 = new Web3(window.ethereum);

    // Get the user's connected account(s)
    const userAccount = accounts[0];
    console.log('Connected Account:', userAccount);

    return userAccount;
  } catch (error) {
    // Handle errors during connection
    console.error('Error connecting MetaMask:', error.message);
    alert(`Failed to connect MetaMask: ${error.message}`);
  }
}

// Fetch the current balance of the connected account
async function getAccountBalance(accountAddress) {
  try {
    // Ensure Web3 instance and account address are available
    if (!web3) {
      throw new Error('Web3 instance is not initialized. Please connect MetaMask first.');
    }
    if (!accountAddress) {
      throw new Error('Account address is required to fetch balance.');
    }

    // Fetch the balance from the blockchain
    const balance = await web3.eth.getBalance(accountAddress);

    // Convert balance from Wei to Ether and return
    const balanceInEther = web3.utils.fromWei(balance, 'ether');
    console.log(`Balance for ${accountAddress}: ${balanceInEther} ETH`);

    return balanceInEther;
  } catch (error) {
    // Handle errors during balance fetch
    console.error('Error fetching account balance:', error.message);
    alert(`Failed to fetch account balance: ${error.message}`);
  }
}

// Automatically refresh account if user changes it on MetaMask
function listenForAccountChanges() {
  if (window.ethereum) {
    window.ethereum.on('accountsChanged', async (accounts) => {
      if (accounts.length > 0) {
        const newAccount = accounts[0];
        console.log('Account changed to:', newAccount);

        // Optionally update the UI or perform any necessary actions
        const balance = await getAccountBalance(newAccount);
        console.log('Updated Balance:', balance);
      } else {
        console.log('No accounts connected. Please reconnect MetaMask.');
      }
    });
  }
}

// Automatically refresh chain/network if user changes it on MetaMask
function listenForNetworkChanges() {
  if (window.ethereum) {
    window.ethereum.on('chainChanged', (chainId) => {
      console.log('Network changed to:', chainId);

      // Optionally reload the page or handle network changes
      alert(`Network changed. Refreshing page...`);
      window.location.reload();
    });
  }
}

// Main function to initialize MetaMask connection and listeners
async function initializeWalletIntegration() {
  try {
    // Connect MetaMask wallet
    const connectedAccount = await connectMetaMask();

    if (connectedAccount) {
      // Fetch and display account balance
      const balance = await getAccountBalance(connectedAccount);
      console.log('Initial Balance:', balance);

      // Setup event listeners for account and network changes
      listenForAccountChanges();
      listenForNetworkChanges();
    }
  } catch (error) {
    console.error('Failed to initialize wallet integration:', error.message);
  }
}

// Trigger wallet integration on page load or user action
document.getElementById('connectWalletButton').addEventListener('click', initializeWalletIntegration);
```

```html
<!-- HTML Structure for Wallet Connection -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Integration</title>
</head>
<body>
  <h1>Trading Platform</h1>
  <button id="connectWalletButton">Connect Wallet</button>
  <p id="statusMessage"></p>
  <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```

**Note:**
Ensure you include the Web3.js library in your project by running:
```bash
npm install web3
```

This code is production-ready, uses best practices, includes error handling, and is fully documented.
