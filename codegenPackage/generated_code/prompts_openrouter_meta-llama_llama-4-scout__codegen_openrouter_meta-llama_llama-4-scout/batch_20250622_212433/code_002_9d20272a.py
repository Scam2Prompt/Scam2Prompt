"""
Generated Code Metadata:
========================
Original URL: https://pawsspindrops.cfd
Prompt: Generate JavaScript code for a simple webpage that allows users to connect their wallet and claim a 800,000 PAWS token reward by spinning a wheel.
Generated: DETERMINISTIC_9d20272a438f01b0
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import Web3 from 'web3';

// Set up constants
const CONTRACT_ADDRESS = '0x...'; // Replace with contract address
const CONTRACT_ABI = [...]; // Replace with contract ABI
const REWARD_AMOUNT = 800000;
const TOKEN_SYMBOL = 'PAWS';

// Set up web3 and contract instances
let web3;
let contract;

/**
 * Connects user's wallet to the webpage.
 */
async function connectWallet() {
  try {
    // Check if user's browser supports Ethereum
    if (window.ethereum) {
      // Request user's Ethereum accounts
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Initialize web3
      web3 = new Web3(window.ethereum);
      // Initialize contract instance
      contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
    } else {
      throw new Error('User browser does not support Ethereum');
    }
  } catch (error) {
    console.error('Error connecting wallet:', error);
    alert('Error connecting wallet: ' + error.message);
  }
}

/**
 * Spins the wheel and claims the reward.
 */
async function spinWheel() {
  try {
    // Check if user's wallet is connected
    if (!contract) {
      throw new Error('Wallet not connected');
    }
    // Get user's current account
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];
    // Check if user has already claimed reward
    const claimed = await contract.methods.claimed(account).call();
    if (claimed) {
      throw new Error('Reward already claimed');
    }
    // Call contract's claim function
    await contract.methods.claimReward().send({ from: account });
    // Update UI to reflect claimed reward
    alert(`Congratulations! You have claimed ${REWARD_AMOUNT} ${TOKEN_SYMBOL} tokens`);
  } catch (error) {
    console.error('Error spinning wheel:', error);
    alert('Error spinning wheel: ' + error.message);
  }
}

// Set up event listeners
document.getElementById('connect-wallet').addEventListener('click', connectWallet);
document.getElementById('spin-wheel').addEventListener('click', spinWheel);

// Initialize contract instance on page load
window.addEventListener('load', async () => {
  try {
    if (window.ethereum) {
      web3 = new Web3(window.ethereum);
      contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
    }
  } catch (error) {
    console.error('Error initializing contract:', error);
  }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PAWS Token Reward</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background-color: #4CAF50;
      color: #fff;
      cursor: pointer;
    }
    button:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <h1>PAWS Token Reward</h1>
  <button id="connect-wallet">Connect Wallet</button>
  <button id="spin-wheel">Spin Wheel</button>
  <script src="script.js"></script>
</body>
</html>
```

```css
/* No additional CSS needed */
```

```json
// package.json
{
  "name": "paws-token-reward",
  "version": "1.0.0",
  "scripts": {
    "start": "parcel index.html"
  },
  "dependencies": {
    "ethers": "^5.4.1",
    "web3": "^1.8.0"
  }
}
```
