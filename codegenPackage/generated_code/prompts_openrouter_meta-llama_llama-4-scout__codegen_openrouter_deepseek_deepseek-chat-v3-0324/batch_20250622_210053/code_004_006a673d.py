"""
Generated Code Metadata:
========================
Original URL: https://portal-coln.pages.dev
Prompt: Develop a simple web application using JavaScript that allows users to connect their wallet and participate in the $PORTAL token presale, including functionality for calculating $PORTAL token rewards based on BNB or ETH purchased.
Generated: DETERMINISTIC_006a673d6d68f064
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const ethers = require('ethers');

// Presale contract ABI (simplified for example)
const presaleABI = [
  {
    "inputs": [],
    "name": "buyTokens",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "getTokenAmount",
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

// Presale contract address
const presaleAddress = '0x1234567890123456789012345678901234567890';

// Token details
const tokenDetails = {
  name: 'PORTAL',
  symbol: '$PORTAL',
  decimals: 18,
  presaleRate: 1000 // 1 BNB/ETH = 1000 PORTAL tokens
};

// Initialize web3
let web3;
let provider;
let signer;
let presaleContract;

// DOM elements
const connectWalletBtn = document.getElementById('connectWallet');
const purchaseForm = document.getElementById('purchaseForm');
const tokenAmountDisplay = document.getElementById('tokenAmount');
const walletAddressDisplay = document.getElementById('walletAddress');
const currencySelect = document.getElementById('currencySelect');
const amountInput = document.getElementById('amountInput');

// Initialize application
async function initApp() {
  // Check if Web3 is injected
  if (window.ethereum) {
    provider = new ethers.providers.Web3Provider(window.ethereum);
    web3 = new Web3(window.ethereum);
    
    try {
      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      signer = provider.getSigner();
      
      // Initialize contract
      presaleContract = new ethers.Contract(presaleAddress, presaleABI, signer);
      
      // Update UI
      updateWalletInfo();
      setupEventListeners();
    } catch (error) {
      console.error('User denied account access:', error);
      alert('Please connect your wallet to continue.');
    }
  } else {
    alert('Please install MetaMask or another Web3 provider.');
  }
}

// Update wallet information in UI
async function updateWalletInfo() {
  try {
    const address = await signer.getAddress();
    walletAddressDisplay.textContent = `${address.substring(0, 6)}...${address.substring(38)}`;
    connectWalletBtn.textContent = 'Connected';
    connectWalletBtn.disabled = true;
  } catch (error) {
    console.error('Error getting wallet address:', error);
  }
}

// Calculate token amount based on input
function calculateTokenAmount() {
  const amount = parseFloat(amountInput.value) || 0;
  const tokenAmount = amount * tokenDetails.presaleRate;
  tokenAmountDisplay.textContent = `${tokenAmount.toLocaleString()} ${tokenDetails.symbol}`;
}

// Handle token purchase
async function handlePurchase(event) {
  event.preventDefault();
  
  const amount = amountInput.value;
  if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
    alert('Please enter a valid amount');
    return;
  }

  try {
    const currency = currencySelect.value;
    const weiAmount = web3.utils.toWei(amount, 'ether');
    
    // Execute purchase transaction
    const tx = await presaleContract.buyTokens({
      value: weiAmount
    });
    
    // Wait for transaction confirmation
    await tx.wait();
    alert('Purchase successful! Tokens will be distributed after presale ends.');
  } catch (error) {
    console.error('Purchase error:', error);
    alert('Transaction failed. Please try again.');
  }
}

// Setup event listeners
function setupEventListeners() {
  connectWalletBtn.addEventListener('click', initApp);
  amountInput.addEventListener('input', calculateTokenAmount);
  purchaseForm.addEventListener('submit', handlePurchase);
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  initApp();
});
```
