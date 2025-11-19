"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Write a code snippet that demonstrates how to connect a dapp to MetaMask for Ethereum transactions.
Generated: DETERMINISTIC_bac5d0530c35ef92
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js for interacting with Ethereum blockchain
import { ethers } from 'ethers';

// Function to connect the DApp to MetaMask
async function connectToMetaMask() {
  try {
    // Check if MetaMask is installed (window.ethereum is injected by MetaMask)
    if (!window.ethereum) {
      console.error('MetaMask is not installed. Please install MetaMask.');
      alert('MetaMask is not installed. Please install MetaMask.');
      return;
    }

    // Request user to connect their wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    
    // Get the connected account (usually the first one)
    const userAccount = accounts[0];
    console.log(`Connected wallet address: ${userAccount}`);

    // Create a new ethers provider instance using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (used for sending transactions)
    const signer = provider.getSigner();

    // Log successful connection
    console.log('MetaMask successfully connected to the DApp.');
    console.log('Signer:', signer);

    // Example: Display the user's balance in Ether (optional)
    const balance = await provider.getBalance(userAccount);
    console.log(`Wallet balance: ${ethers.utils.formatEther(balance)} ETH`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Failed to connect to MetaMask:', error.message);
    alert(`Error connecting to MetaMask: ${error.message}`);
  }
}

// Event listener to initiate connection when a button is clicked
document.getElementById('connectButton').addEventListener('click', connectToMetaMask);

// HTML element for demonstration (ensure you have this in your HTML file)
// <button id="connectButton">Connect to MetaMask</button>
```

**Dependencies:** Ensure you have the `ethers` library installed in your project (`npm install ethers`).
