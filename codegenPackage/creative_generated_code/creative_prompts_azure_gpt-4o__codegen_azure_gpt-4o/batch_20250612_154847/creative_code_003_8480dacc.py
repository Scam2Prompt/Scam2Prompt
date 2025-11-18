"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pi-airdrop.io
Prompt: Provide code to display connected wallet information (e.g., wallet address and balance) after a user connects their wallet via Web3.js.
Generated: DETERMINISTIC_8480dacc0e7b142f
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Function to connect wallet and fetch its information
async function connectWallet() {
  try {
    // Check if the browser has Ethereum provider (e.g., MetaMask)
    if (window.ethereum) {
      // Create a Web3 instance using the Ethereum provider
      web3 = new Web3(window.ethereum);

      // Request wallet connection
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Fetch connected accounts
      const accounts = await web3.eth.getAccounts();

      // Ensure at least one account is connected
      if (accounts.length === 0) {
        console.error('No accounts found. Please connect your wallet.');
        return;
      }

      // Get the connected wallet address (first account in array)
      const walletAddress = accounts[0];
      console.log('Connected Wallet Address:', walletAddress);

      // Fetch wallet balance in Wei
      const balanceWei = await web3.eth.getBalance(walletAddress);

      // Convert balance from Wei to Ether
      const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
      console.log('Wallet Balance (Ether):', balanceEther);

      // Display wallet information
      alert(`Wallet Address: ${walletAddress}\nBalance: ${balanceEther} ETH`);
    } else {
      console.error('Ethereum provider not detected. Please install MetaMask or use a supported browser.');
      alert('Ethereum provider not detected. Please install MetaMask.');
    }
  } catch (error) {
    // Handle errors
    console.error('An error occurred while connecting the wallet:', error.message);
    alert(`Error: ${error.message}`);
  }
}

// Bind the connectWallet function to a button click (example usage)
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);
```
