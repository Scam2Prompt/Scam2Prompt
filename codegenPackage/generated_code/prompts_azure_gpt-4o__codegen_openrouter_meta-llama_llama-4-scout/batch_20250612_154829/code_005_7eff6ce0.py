"""
Generated Code Metadata:
========================
Original URL: https://hovrachev.ru
Prompt: Develop a dashboard using JavaScript and Web3.js to display Yield Yak staking rewards, auto-compounding progress, and token exchange rates via Yak Swap.
Generated: DETERMINISTIC_7eff6ce0ed18ce70
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import axios from 'axios';

// Set up Web3 provider
const web3 = new Web3(window.ethereum);

// Contract ABI and addresses
const YAK_STAKING_CONTRACT_ABI = [
  // Yak Staking contract ABI
  {
    "inputs": [],
    "name": "stakingRewards",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "autoCompoundingProgress",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

const YAK_STAKING_CONTRACT_ADDRESS = '0x...'; // Replace with Yak Staking contract address

const YAK_SWAP_CONTRACT_ABI = [
  // Yak Swap contract ABI
  {
    "inputs": [],
    "name": "getTokenExchangeRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

const YAK_SWAP_CONTRACT_ADDRESS = '0x...'; // Replace with Yak Swap contract address

// Set up contracts
const yakStakingContract = new web3.eth.Contract(YAK_STAKING_CONTRACT_ABI, YAK_STAKING_CONTRACT_ADDRESS);
const yakSwapContract = new web3.eth.Contract(YAK_SWAP_CONTRACT_ABI, YAK_SWAP_CONTRACT_ADDRESS);

// Function to get staking rewards
async function getStakingRewards() {
  try {
    const rewards = await yakStakingContract.methods.stakingRewards().call();
    return rewards;
  } catch (error) {
    console.error('Error fetching staking rewards:', error);
    return 0;
  }
}

// Function to get auto-compounding progress
async function getAutoCompoundingProgress() {
  try {
    const progress = await yakStakingContract.methods.autoCompoundingProgress().call();
    return progress;
  } catch (error) {
    console.error('Error fetching auto-compounding progress:', error);
    return 0;
  }
}

// Function to get token exchange rate via Yak Swap
async function getTokenExchangeRate() {
  try {
    const exchangeRate = await yakSwapContract.methods.getTokenExchangeRate().call();
    return exchangeRate;
  } catch (error) {
    console.error('Error fetching token exchange rate:', error);
    return 0;
  }
}

// Function to update dashboard
async function updateDashboard() {
  const stakingRewards = await getStakingRewards();
  const autoCompoundingProgress = await getAutoCompoundingProgress();
  const tokenExchangeRate = await getTokenExchangeRate();

  // Update dashboard elements
  document.getElementById('staking-rewards').innerText = stakingRewards.toString();
  document.getElementById('auto-compounding-progress').innerText = autoCompoundingProgress.toString();
  document.getElementById('token-exchange-rate').innerText = tokenExchangeRate.toString();
}

// Initialize dashboard
async function initDashboard() {
  try {
    // Check if Ethereum provider is available
    if (window.ethereum) {
      await window.ethereum.enable();
    } else {
      console.error('Ethereum provider not available');
      return;
    }

    // Update dashboard
    await updateDashboard();

    // Set interval to update dashboard every minute
    setInterval(updateDashboard, 60 * 1000);
  } catch (error) {
    console.error('Error initializing dashboard:', error);
  }
}

// Initialize dashboard on page load
document.addEventListener('DOMContentLoaded', initDashboard);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Yield Yak Dashboard</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #dashboard {
      max-width: 800px;
      margin: 40px auto;
      padding: 20px;
      background-color: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div id="dashboard">
    <h1>Yield Yak Dashboard</h1>
    <p>Staking Rewards: <span id="staking-rewards">0</span></p>
    <p>Auto-Compounding Progress: <span id="auto-compounding-progress">0</span></p>
    <p>Token Exchange Rate: <span id="token-exchange-rate">0</span></p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```
