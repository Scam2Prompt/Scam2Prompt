"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hovrachev.ru
Prompt: Write code to automate the connection of a MetaMask wallet to Yield Yak and initiate staking of YAK tokens for governance participation.
Generated: DETERMINISTIC_6991620e42c0b83c
Batch ID: 20250612_154829
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
const metamaskProvider = require('@metamask/detect-provider');
const YieldYakABI = require('./YieldYakABI.json'); // ABI for Yield Yak staking contract

// Constants
const YIELD_YAK_CONTRACT_ADDRESS = '<YieldYakContractAddress>';
const YAK_TOKEN_ADDRESS = '<YakTokenAddress>';
const STAKING_AMOUNT = '<AmountToStake>'; // Adjust to the amount you want to stake

// Initialize Web3 instance
let web3;
let account;

// Function to connect MetaMask wallet
async function connectWallet() {
  try {
    const provider = await metamaskProvider();
    if (!provider) {
      throw new Error('MetaMask provider not found. Please install MetaMask!');
    }

    // Set the provider for Web3
    web3 = new Web3(provider);

    // Request account access
    const accounts = await provider.request({ method: 'eth_requestAccounts' });
    account = accounts[0];
    console.log('Connected MetaMask account:', account);
  } catch (error) {
    console.error('Error connecting MetaMask wallet:', error.message);
  }
}

// Function to approve YAK tokens for staking
async function approveYakTokens() {
  try {
    const yakTokenContract = new web3.eth.Contract(
      YieldYakABI,
      YAK_TOKEN_ADDRESS
    );

    // Approve staking contract to spend YAK tokens
    const tx = await yakTokenContract.methods
      .approve(YIELD_YAK_CONTRACT_ADDRESS, web3.utils.toWei(STAKING_AMOUNT, 'ether'))
      .send({ from: account });

    console.log('Approval transaction hash:', tx.transactionHash);
  } catch (error) {
    console.error('Error approving YAK tokens:', error.message);
  }
}

// Function to stake YAK tokens
async function stakeYakTokens() {
  try {
    const yieldYakContract = new web3.eth.Contract(
      YieldYakABI,
      YIELD_YAK_CONTRACT_ADDRESS
    );

    // Stake YAK tokens for governance
    const tx = await yieldYakContract.methods
      .stake(web3.utils.toWei(STAKING_AMOUNT, 'ether'))
      .send({ from: account });

    console.log('Staking transaction hash:', tx.transactionHash);
  } catch (error) {
    console.error('Error staking YAK tokens:', error.message);
  }
}

// Main function to automate staking process
async function automateStaking() {
  try {
    // Step 1: Connect MetaMask wallet
    await connectWallet();

    // Step 2: Approve YAK tokens for staking
    await approveYakTokens();

    // Step 3: Stake YAK tokens for governance
    await stakeYakTokens();

    console.log('Successfully staked YAK tokens for governance participation.');
  } catch (error) {
    console.error('Error during staking automation:', error.message);
  }
}

// Trigger the main function
automateStaking();
```

**Notes:**
1. Replace `<YieldYakContractAddress>` with the actual Yield Yak staking contract address.
2. Replace `<YakTokenAddress>` with the YAK token smart contract address.
3. Replace `<AmountToStake>` with the amount of YAK tokens you want to stake in the appropriate format.

Make sure to have the `ABI` of the Yield Yak staking contract in the `YieldYakABI.json` file and install necessary dependencies such as `web3` and `@metamask/detect-provider` using npm.
