"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://besureofme.pages.dev
Prompt: Generate a step-by-step guide for connecting a wallet and interacting with ListaDAO's staking and lending protocols via Web3 APIs.
Generated: DETERMINISTIC_bf9a24dd4904b660
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import required libraries
const Web3 = require('web3'); // Web3.js library for Ethereum interaction
const { abi: stakingAbi } = require('./StakingContract.json'); // ABI of the staking contract
const { abi: lendingAbi } = require('./LendingContract.json'); // ABI of the lending contract

// Configuration Constants
const PROVIDER_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Infura or other provider URL
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress'; // Replace with ListaDAO staking contract address
const LENDING_CONTRACT_ADDRESS = '0xYourLendingContractAddress'; // Replace with ListaDAO lending contract address

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(PROVIDER_URL));

// Function to connect wallet using MetaMask
async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed. Please install it to connect your wallet.');
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected wallet address:', accounts[0]);
    return accounts[0]; // Return the connected wallet address
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    throw error; // Rethrow error for the caller to handle
  }
}

// Function to interact with staking protocol (stake tokens)
async function stakeTokens(walletAddress, amount) {
  try {
    // Initialize staking contract instance
    const stakingContract = new web3.eth.Contract(stakingAbi, STAKING_CONTRACT_ADDRESS);

    // Convert amount to Wei (smallest denomination)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Send stake transaction
    const tx = await stakingContract.methods.stake(amountInWei).send({
      from: walletAddress,
    });

    console.log('Staked successfully:', tx);
    return tx; // Return transaction details
  } catch (error) {
    console.error('Error staking tokens:', error.message);
    throw error; // Rethrow error for the caller to handle
  }
}

// Function to interact with lending protocol (borrow tokens)
async function borrowTokens(walletAddress, collateralAmount, borrowAmount) {
  try {
    // Initialize lending contract instance
    const lendingContract = new web3.eth.Contract(lendingAbi, LENDING_CONTRACT_ADDRESS);

    // Convert amounts to Wei
    const collateralInWei = web3.utils.toWei(collateralAmount.toString(), 'ether');
    const borrowInWei = web3.utils.toWei(borrowAmount.toString(), 'ether');

    // Send borrow transaction
    const tx = await lendingContract.methods.borrow(collateralInWei, borrowInWei).send({
      from: walletAddress,
    });

    console.log('Borrowed successfully:', tx);
    return tx; // Return transaction details
  } catch (error) {
    console.error('Error borrowing tokens:', error.message);
    throw error; // Rethrow error for the caller to handle
  }
}

// Example Usage:
// (Uncomment the following lines and replace placeholders with real values)

// (async function main() {
//   try {
//     const walletAddress = await connectWallet(); // Step 1: Connect wallet
//
//     // Step 2: Stake tokens
//     const stakeTx = await stakeTokens(walletAddress, 1); // Stake 1 token
//
//     // Step 3: Borrow tokens
//     const borrowTx = await borrowTokens(walletAddress, 1, 0.5); // Use 1 token as collateral to borrow 0.5 token
//
//     console.log('All operations completed successfully!');
//   } catch (error) {
//     console.error('Error during operations:', error.message);
//   }
// })();
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"`, `stakingAbi`, `lendingAbi`, and contract addresses with real values from your project setup.
