"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepelive.com
Prompt: Provide an example of how to set up a wallet integration for buying and staking WEPE tokens, including compatibility with popular wallets like MetaMask.
Generated: DETERMINISTIC_e4e333d3a9da2d8e
Batch ID: 20250612_153812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const Web3 = require('web3'); // Web3.js library for interacting with Ethereum blockchain
const { ethers } = require('ethers'); // Ethers.js library for wallet compatibility
require('dotenv').config(); // Load environment variables from `.env` file

// Load environment variables
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Infura project ID for Ethereum node access
const TOKEN_CONTRACT_ADDRESS = process.env.TOKEN_CONTRACT_ADDRESS; // WEPE token contract address
const STAKING_CONTRACT_ADDRESS = process.env.STAKING_CONTRACT_ADDRESS; // Staking contract address
const PRIVATE_KEY = process.env.PRIVATE_KEY; // User's private key for signing transactions

// Initialize Web3 and provider
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);

// ABI for WEPE token contract (simplified for ERC-20 standard)
const tokenABI = [
  {
    constant: true,
    inputs: [{ name: '_owner', type: 'address' }],
    name: 'balanceOf',
    outputs: [{ name: 'balance', type: 'uint256' }],
    payable: false,
    stateMutability: 'view',
    type: 'function',
  },
  {
    constant: false,
    inputs: [{ name: '_to', type: 'address' }, { name: '_value', type: 'uint256' }],
    name: 'transfer',
    outputs: [{ name: '', type: 'bool' }],
    payable: false,
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    constant: false,
    inputs: [
      { name: '_spender', type: 'address' },
      { name: '_value', type: 'uint256' },
    ],
    name: 'approve',
    outputs: [{ name: '', type: 'bool' }],
    payable: false,
    stateMutability: 'nonpayable',
    type: 'function',
  },
];

// ABI for Staking contract (simplified for staking functionality)
const stakingABI = [
  {
    constant: false,
    inputs: [{ name: '_amount', type: 'uint256' }],
    name: 'stakeTokens',
    outputs: [],
    payable: false,
    stateMutability: 'nonpayable',
    type: 'function',
  },
];

// Initialize contracts
const tokenContract = new web3.eth.Contract(tokenABI, TOKEN_CONTRACT_ADDRESS);
const stakingContract = new web3.eth.Contract(stakingABI, STAKING_CONTRACT_ADDRESS);

// Function to buy WEPE tokens
async function buyTokens(receiverAddress, amount) {
  try {
    const transaction = {
      to: TOKEN_CONTRACT_ADDRESS, // Token contract address
      value: web3.utils.toWei(amount.toString(), 'ether'), // Convert amount to Wei
      gas: 21000, // Gas limit
    };

    const signedTx = await web3.eth.accounts.signTransaction(transaction, PRIVATE_KEY);

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Error buying tokens:', error.message);
  }
}

// Function to approve staking contract to spend WEPE tokens
async function approveStakingContract(amount) {
  try {
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    const data = tokenContract.methods
      .approve(STAKING_CONTRACT_ADDRESS, web3.utils.toWei(amount.toString(), 'ether'))
      .encodeABI();

    const transaction = {
      from: account.address,
      to: TOKEN_CONTRACT_ADDRESS,
      gas: 100000, // Gas limit for approval transactions
      data,
    };

    const signedTx = await web3.eth.accounts.signTransaction(transaction, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Approval successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Error approving tokens:', error.message);
  }
}

// Function to stake WEPE tokens
async function stakeTokens(amount) {
  try {
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    const data = stakingContract.methods
      .stakeTokens(web3.utils.toWei(amount.toString(), 'ether'))
      .encodeABI();

    const transaction = {
      from: account.address,
      to: STAKING_CONTRACT_ADDRESS,
      gas: 100000, // Gas limit for staking transactions
      data,
    };

    const signedTx = await web3.eth.accounts.signTransaction(transaction, PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Staking successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Error staking tokens:', error.message);
  }
}

// Export functions for use in other parts of the application
module.exports = {
  buyTokens,
  approveStakingContract,
  stakeTokens,
};
```

**Note:** 
- Replace the `.env` variables (`INFURA_PROJECT_ID`, `TOKEN_CONTRACT_ADDRESS`, `STAKING_CONTRACT_ADDRESS`, `PRIVATE_KEY`) with your actual values.
- Ensure you manage the user's private keys securely.
